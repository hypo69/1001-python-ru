# Importing Modules in Python

Importing libraries in Python allows you to use external or your own modules and functions defined in other files or libraries. This helps organize code, improve its readability, and avoid duplication.

### What are Modules?
A module in Python is simply a file with a `.py` extension that contains code (functions, classes, variables, etc.). When you want to use code from another module, you need to import it into the current file.

### External and Internal Modules
1. **External modules** — these are modules that are not part of the Python standard library and need to be installed separately. For example, modules for working with web servers, data processing, or machine learning, such as `numpy`, `requests`, and others.

2. **Internal modules** — these are modules that are already included in the Python standard library. For example, modules for working with files, time, mathematical operations: `os`, `math`, `datetime`.

### Installing External Modules with pip
To install an external module, we use the `pip` command — this is a tool for managing Python packages. For example, to install the `requests` library, you need to run the following command in the terminal:
```bash
pip install requests
```
This command will download and install the library into your project.

### Importing Modules
When you want to use a module in Python, you need to import it:
1. **Import the entire module**:
   ```python
   import os
   ```
   After that, you can use all functions and variables from the module, for example:
   ```python
   os.listdir()  # list files in directory
   ```

2. **Import specific elements from a module**:
   ```python
   from math import sqrt
   ```
   Now you can use the `sqrt` function without needing to refer to the `math` module.

3. **Import with an alias**:
   ```python
   import pandas as pd
   ```
   In this case, to use the functions of the `pandas` library, you will write `pd`, not the full name `pandas`.

### Importing Your Own Modules
If you are writing multiple files in one project, you can create your own modules. For example, if you have a `utils.py` file with useful functions, you can import it into other files like this:
```python
import utils
```
Or import a specific function:
```python
from utils import my_function
```

### Why create one module and import it into other parts of the project?
1. **Code organization**: Separating logic into different modules helps avoid clutter in a large project. For example, you can create a module for working with data, another for handling requests, and a third for the interface.
   
2. **Code reuse**: When logic is separated into modules, it can be used in different parts of the project. This reduces code duplication and facilitates maintenance.

3. **Readability and maintainability**: When code is separated into modules, other developers (or you yourself in the future) will be able to understand and maintain the project more easily.

Example:
```python
# utils.py
def greet(name):
    return f"Hello, {name}!"
    
# main.py
from utils import greet

print(greet("Alice"))
```

In this example, the `greet` function is defined in one module (`utils.py`), but used in another (`main.py`), which improves the structure and makes the code more modular and easier to change.

---

  [To Table of Contents](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
