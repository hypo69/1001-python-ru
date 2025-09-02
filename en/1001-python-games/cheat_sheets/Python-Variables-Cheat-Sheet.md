**Variables in Python: what they are and why they are needed**

Variables are named containers for storing data in computer memory. They allow you to access data by name, instead of using it directly.

Example:
```python
x = 10
y = 'Hello, world!'
```
Here `x` and `y` are variables. `x` stores the number 10, and `y` stores the string 'Hello, world!'.

### **How do variables work in Python?**
1. **Dynamic typing**:
   In Python, you don't need to specify the type of a variable when you create it — it's done automatically. For example:
   ```python
   a = 42      # Integer (int)
   b = 3.14    # Floating-point number (float)
   c = 'Text' # String (str)
   ```

2. **Reference model of data storage**:
   Variables in Python are references to objects in memory. For example:
   ```python
   x = 5
   y = x  # y now also points to object 5
   x = 10 # x now points to another object 10, and y still points to 5
   ```

---

### **Variable naming rules**
1. **Mandatory rules**:
   - A variable name can consist of letters, digits, and the `_` symbol, but cannot start with a digit.
     ✅ Examples: `my_var`, `_data`, `var123`
     ❌ Incorrect: `123var`, `my-var`
   - Variable names are case-sensitive.
     Example: `age` and `Age` are different variables.

2. **Recommendations for meaningful names**:
   - Use names that reflect the essence of the data.
     ❌ Bad: `a = 100`, `b = 'Name'`
     ✅ Good: `salary = 100`, `username = 'Name'`
   - For multi-word names, use **snake_case** style:
     Example: `user_age`, `total_cost`.

3. **Reserved words**:
   You cannot use Python keywords (e.g., `if`, `for`, `while`) as variable names.

   To see a list of keywords, run:
   ```python
   import keyword
   print(keyword.kwlist)
   ```

---

### **Features of data type storage**
1. **Python data types**:
   - **Numbers**: `int`, `float`, `complex`
   - **Strings**: `str`
   - **Lists**: `list`
   - **Tuples**: `tuple`
   - **Sets**: `set`
   - **Dictionaries**: `dict`

2. **Mutable and immutable types**:
   - **Mutable**: `list`, `dict`, `set`.
     Example:
     ```python
     lst = [1, 2, 3]
     lst.append(4)  # List modified
     ```
   - **Immutable**: `int`, `float`, `str`, `tuple`.
     Example:
     ```python
     name = 'Alice'
     name[0] = 'B'  # Error, strings are immutable
     ```

3. **`type` function for type checking**:
   ```python
   x = 10
   print(type(x))  # <class 'int'>
   ```

---

### **Tips for beginners**
1. Use meaningful variable names to make your code understandable.
2. Remember that Python does not require variable type declaration, but be careful not to get confused with data types.
3. Learn built-in functions for working with variables, such as `type()`, `id()`, and modules, such as `sys`, to better understand how Python manages memory.

---

  [To Table of Contents](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
