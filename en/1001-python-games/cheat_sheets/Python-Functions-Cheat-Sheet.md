# Functions in Python

Functions in Python are named blocks of code that perform a specific task. They allow you to organize code, make it more structured, and facilitate its reuse.

# Table of Contents

1. [Function Declaration](#function-declaration)
2. [Function Parameters](#function-parameters)
   - [Types of Parameters](#types-of-parameters)
3. [Return Value](#return-value)
4. [Local and Global Variables](#local-and-global-variables)
5. [Nested Functions](#nested-functions)
6. [Recursion](#recursion)
7. [Exception Handling with `try` and `except`](#exception-handling-with-try-and-except)
8. [Function Usage Example](#function-usage-example)

## Function Declaration

A function is declared using the `def` keyword, followed by the function name, a list of parameters in parentheses, and a colon. The function body is written with an indent.

```python
def function_name(parameters):
    # actions
    return result
```

### Example:
```python
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b
```

Here:
- `a: int` and `b: int` — function parameters with type annotations.
- `-> int` — return value type annotation.

## Function Parameters

Functions can accept parameters, which are input data. They are specified in parentheses after the function name.

Example with one parameter:
```python
def greeting(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}!"
```

### Types of parameters:
1. **Required parameters** — must be passed when calling the function.
2. **Optional parameters** — can have default values.
   ```python
   def greeting(name: str, age: int = 18) -> str:
       return f"Hello, {name}! You are {age} years old."
   ```

## Return Value

A function can return a value using the `return` keyword. If `return` is not used, the function returns `None` by default.

Example:
```python
def multiply(a: int, b: int) -> int:
    """Returns the product of two numbers."""
    return a * b
```

## Local and Global Variables

- **Local variable** — a variable that exists only inside a function. It is created and destroyed with each function call.
- **Global variable** — a variable that is accessible throughout the code, including functions.

Example of using a global variable:
```python
x = 10  # Global variable

def show_x() -> int:
    return x  # Accessing the global variable
```

If you need to change a global variable inside a function, you must use the `global` keyword:
```python
x = 10  # Global variable

def change_x() -> None:
    global x
    x = 20
```

## Nested Functions

In Python, functions can be nested, meaning one function can be defined inside another. A nested function can access variables of the outer function.

Example:
```python
def outer(a: int, b: int) -> int:
    """A function that uses a nested function to calculate the difference."""
    
    def nested(x: int, y: int) -> int:
        """Nested function returning the difference."""
        return x - y
    
    return nested(a, b)
```

## Recursion

Recursion is when a function calls itself. This is useful for tasks that can be broken down into smaller, similar tasks (e.g., factorial).

Example of recursion:
```python
def factorial(n: int) -> int:
    """Calculates the factorial of a number using recursion."""
    if n == 0:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive call
```

## Exception Handling with `try` and `except`

Python provides an error handling mechanism using `try` and `except` blocks. Code that may cause an error is placed in the `try` block, and errors are handled in the `except` block.

Example of error handling:
```python
def divide(a: int, b: int) -> float:
    """Divides one number by another, handling possible errors."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: division by zero"
    except Exception as e:
        return f"An error occurred: {e}"
    return result
```

Here:
- The `try` block attempts to perform the division operation.
- The `except ZeroDivisionError` block catches the division by zero error.
- The `except Exception as e` block catches other exceptions and prints an error message.

## Function Usage Example

```python
# Adding two numbers
print(add(5, 3))  # 8

# Nested function
print(outer(10, 4))  # 6

# Recursion for factorial calculation
print(factorial(5))  # 120

# Exception handling for division
print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error: division by zero
```
---

  [To Table of Contents](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
