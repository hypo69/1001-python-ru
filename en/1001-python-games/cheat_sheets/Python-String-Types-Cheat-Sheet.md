In Python, strings are one of the most important and frequently used data types. Here's a brief overview of different string types and their features:

---

### 1. **Regular strings**
Regular strings are created using single `'` or double quotes `"`.

**Example:**
```python
s1 = 'Hello, world!'
s2 = "Python is cool!"
```

They are identical, but it's important to be consistent in using one style.

---

### 2. **Multi-line strings**
Multi-line strings are enclosed in triple quotes `'''` or `"""`. They allow you to write text on multiple lines.

**Example:**
```python
s3 = '''This is a string
on multiple
lines.'''
```

---

### 3. **f-strings (formatted strings)**
f-strings (or formatted strings) are used to embed variable values and expressions directly inside a string. The `f` character is added before the start of the string.

**Example:**
```python
name = 'Boris'
age = 25
s4 = f'My name is {name}, I am {age} years old.'
print(s4)  # My name is Boris, I am 25 years old.
```

The advantage of f-strings is that they are simple and readable.
In new versions of Python (starting from **3.8**), a convenient feature appeared: using expressions like `f'{name=}'` in f-strings. This construct outputs not only the variable's value but also its name, which is especially useful for debugging.

### Example of using `f'{name=}'`:
```python
name = 'Boris'
age = 25

# Output variable name and its value
print(f'{name=}, {age=}')
# Result: name='Boris', age=25
```

### Features:
1. **Automatic variable name indication**: 
   Python automatically substitutes the variable name and its value, separating them with the `=` symbol.
   
2. **Works with expressions**: 
   You can use expressions inside an f-string, and they will also be shown.

**Example:**
```python
x = 10
y = 5
print(f'{x + y=}')
# Result: x + y=15
```

3. **Application to string functions**: 
   You can output the result of methods or operations on strings.

**Example:**
```python
s = 'Python'
print(f'{s.upper()=}')
# Result: s.upper()='PYTHON'
```

### Why this is useful:
- **Debugging code**: Quickly check the values of variables and expressions.
- **Readability**: Clearly shows which variable the value belongs to.


---


### 4. **r-strings (raw strings)**
r-strings (raw strings) are created by adding the `r` character before the string. They are used for working with characters that are usually interpreted as special, such as newline characters (`\n`) or tabs (`\t`).

**Example:**
```python
s5 = r'C:\new_folder\test'
print(s5)  # C:\new_folder\test
```

Without `r`, this string would be interpreted with `\n` replaced by a newline.

---


### 5. **u-strings (Unicode strings)**
u-strings were important in Python 2 for working with Unicode, but in Python 3, strings are Unicode by default, so adding `u` is no longer necessary.

**Example:**
```python
s6 = u'Hello, world!'
```

---


### 6. **b-strings (byte strings)**
Byte strings are used for working with binary data. Such strings start with `b`. They do not support Unicode characters, only bytes.

**Example:**
```python
# Byte string representing a PNG file header
image_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

# Check that the data matches the PNG format
if image_bytes.startswith(b'\x89PNG'):
    print('This is a PNG image.')
else:
    print('Unknown format.')

```

---


### 7. **Strings with escaping**
To include special characters in a string, escape sequences with a backslash (`\`) are used.

**Example:**
```python
s8 = 'This is a string with quotes: \'single\' and "double".'
```

---


### 8. **Combination of f-strings and r-strings**
You can combine string types. For example, f-strings and raw strings:

**Example:**
```python
path = 'new_folder'
s9 = fr'C:\{path}\test'
print(s9)  # C:\new_folder\test
```

---


### Summary
In Python, strings are flexible and convenient. The choice of string type depends on the task:
- For regular text — `'` or `"`.
- For multi-line text — `'''` or `"""`.
- For value substitution — `f`.
- For paths or regular expressions — `r`.
- For binary data — `b`.

---

  [To Table of Contents](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)
