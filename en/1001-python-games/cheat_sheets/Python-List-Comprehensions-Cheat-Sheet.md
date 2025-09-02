**What are list comprehensions?**

In its simplest form, a list comprehension is a concise way to create a new list based on an existing one (or any iterable object). Instead of using a traditional `for` loop and adding elements to the list one by one, you can do it in a single line of code.


*   **Conciseness:** They allow you to write less code.
*   **Readability:** Once you get used to their syntax, you will find them easier to understand than equivalent `for` loops.
*   **Performance:** In some cases, list comprehensions can be faster than `for` loops.


Here's the basic syntax of a list comprehension:

```python
new_list = [expression for item in iterable]
```

*   **`expression`**: An expression that defines how each element of the new list will be calculated. This can be anything: a simple value, a mathematical operation, a function call.
*   **`item`**: A variable that takes the value of each element from `iterable` in turn.
*   **`iterable`**: An iterable object, such as a list, tuple, string, or the result of `range()`.

**Example:**

Suppose you have a list of numbers, and you want to create a new list containing the squares of those numbers.

**Without list comprehension:**

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number**2)
print(squares)  # Output: [1, 4, 9, 16, 25]
```

**With list comprehension:**

```python
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares) # Output: [1, 4, 9, 16, 25]
```

List comprehension makes the code shorter and clearer!

**Adding a condition**

List comprehensions also allow you to add conditions to select elements that will be included in the new list.

```python
new_list = [expression for item in iterable if condition]
```

* **`condition`**: a condition that must be met for an element to be included in the new list.

**Example:**

Let's create a list of squares of only even numbers from our original `numbers` list.

**Without list comprehension:**

```python
numbers = [1, 2, 3, 4, 5]
even_squares = []
for number in numbers:
    if number % 2 == 0:
        even_squares.append(number**2)
print(even_squares) # Output: [4, 16]
```

**With list comprehension:**

```python
numbers = [1, 2, 3, 4, 5]
even_squares = [number**2 for number in numbers if number % 2 == 0]
print(even_squares) # Output: [4, 16]
```

I added `if number % 2 == 0` to the list comprehension to filter only even numbers.

**Multi-line list comprehensions**

When list comprehensions become more complex, they can be broken into multiple lines for better readability.

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
squared_odds = [
    number**2
    for number in numbers
    if number % 2 != 0
]
print(squared_odds) # Output: [1, 9, 25]
```
This makes the code more understandable, especially when you have long conditions or complex expressions.





**Exercise 1: Temperature Conversion**

You have a list of temperatures in Celsius, and you need to convert them to Fahrenheit. The formula for conversion is: `F = (C * 9/5) + 32`.

Here's your list of temperatures in Celsius:

```python
celsius_temperatures = [0, 10, 20, 30, 40]
```

**Task:**

1.  Using a list comprehension, create a new list `fahrenheit_temperatures` containing temperatures from `celsius_temperatures`, converted to Fahrenheit.
2.  Print the resulting `fahrenheit_temperatures` list to the screen.

**Hint:**

*   Use the formula `(celsius * 9/5) + 32` as the expression in the list comprehension.
*   Think about what is `iterable` and what is `item` in this case.

Try to write the code.

My solution:
```python
# Original list of temperatures in Celsius
celsius_temperatures = [0, 10, 20, 30, 40]

# Use list comprehension to convert to Fahrenheit
fahrenheit_temperatures = [
    (celsius * 9/5) + 32  # Expression: conversion formula
    for celsius in celsius_temperatures # Iterate over list elements
]

# Print the result
print(fahrenheit_temperatures) # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
```

**Code breakdown:**

1.  **`celsius_temperatures = [0, 10, 20, 30, 40]`**: This is the original list of temperatures in Celsius.
2.  **`fahrenheit_temperatures = [...]`**: Here we create a new list using a list comprehension.
3.  **`(celsius * 9/5) + 32`**: This is the expression that is executed for each element. It converts the temperature from Celsius to Fahrenheit.
4.  **`for celsius in celsius_temperatures`**: This part of the list comprehension iterates over each element in the `celsius_temperatures` list, assigning its value to the `celsius` variable in each iteration.
5.  **`print(fahrenheit_temperatures)`**: Prints the resulting list of temperatures in Fahrenheit.

**Important notes:**

*   In this case, `celsius_temperatures` is the `iterable`, and `celsius` is the `item`.
*   I use multi-line formatting for the list comprehension to improve code readability.
*   Inside the expression, I directly apply the conversion formula using the current `celsius` value.



**Exercise 2: String Filtering and Transformation**

You have a list of words, and you need to do the following:

1.  Filter out words that start with the letter "a" (case-insensitive).
2.  Convert all remaining words to uppercase.

Here's your list of words:

```python
words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]
```

**Task:**

1.  Using a list comprehension, create a new list `transformed_words` containing only those words from the `words` list that do not start with the letter "a" (or "A"), and are converted to uppercase.
2.  Print the resulting `transformed_words` list to the screen.

**Hints:**

*   Use the string method `startswith()` to check if a word starts with a specific letter. Don't forget about case! Convert everything to lowercase.
*   Use the string method `upper()` to convert a string to uppercase.
*   Think about the order of operations. First filter, then transform.

My solution:

```python
# Original list of words
words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]

# Use list comprehension for filtering and transformation
transformed_words = [
    word.upper() # Convert to uppercase
    for word in words # Iterate over words in the list
    if not word.lower().startswith("a") # Filter words that do not start with 'a'
]

# Print the result
print(transformed_words) # Output: ['BANANA', 'KIWI', 'ORANGE']
```

**Code breakdown:**

1.  **`words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]`**: This is the original list of words.
2.  **`transformed_words = [...]`**: Create a new list using a list comprehension.
3.  **`word.upper()`**: This is the expression that is executed for each filtered word. It converts the word to uppercase.
4.  **`for word in words`**: Iterate over all words in the `words` list.
5.  **`if not word.lower().startswith("a")`**: This is the filtering condition.
    *   `word.lower()`: First, we convert the word to lowercase so that the comparison is case-insensitive.
    *   `startswith("a")`: Then we check if the word starts with the letter "a".
    *   `not`: Invert the result to keep only those words that *do not* start with the letter "a".
6.  **`print(transformed_words)`**: Prints the resulting list of transformed words.

**Key points:**

*   String methods `lower()`, `upper()`, and `startswith()` in the expression and condition of the list comprehension.
*   The filtering condition `if not word.lower().startswith("a")` ensures that only words not starting with "a" (regardless of case) are included in the new list.
*   Filtering is applied first, then conversion to uppercase.
*   Again, I use multi-line formatting for readability.


**Exercise 3: Creating a Dictionary from a List of Tuples**

You have a list of tuples, where each tuple contains two elements: a person's name and age.

```python
people_data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 28),
]
```

**Task:**

1. Using a list comprehension, create a dictionary `people_dict`, where the keys are the names of the people, and the values are their ages.
2. Print the `people_dict` dictionary to the screen.

**Hints:**

*   List comprehensions create lists, but they can be used to create lists of tuples, which can then be passed to the `dict()` constructor.
*   Think about how to extract the name and age from each tuple.
*   Remember that a dictionary is a data structure that stores key-value pairs.

**A little explanation:**

In Python, you can create a dictionary from a list of tuples, where each tuple consists of two elements (key, value).
To do this, I use the `dict()` constructor. For example:
```python
my_list = [("a", 1), ("b", 2)]
my_dict = dict(my_list)
print(my_dict) # Output {'a': 1, 'b': 2}
```
Your task is to use a list comprehension to create this list of tuples, which will then be used to create the dictionary.

My solution:

```python
# Original list of tuples with people data
people_data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 28),
]

# I use a list comprehension to create a list of tuples, which I then convert to a dictionary
people_dict = dict(
    [
      (name, age) # Create a tuple (name, age)
      for name, age in people_data # Iterate over tuples in people_data
    ]
)

# Print the resulting dictionary
print(people_dict) # Output: {'Alice': 30, 'Bob': 25, 'Charlie': 35, 'David': 28}
```

**Code breakdown:**

1.  **`people_data = [...]`**: This is the original list of tuples, where each tuple contains a person's name and age.
2.  **`people_dict = dict(...)`**: We use the `dict()` constructor to create a dictionary from a list of tuples.
3.  **`[ (name, age) for name, age in people_data ]`**: This is a list comprehension that creates a list of tuples.
    *   `(name, age)`: This expression creates a tuple from two elements: `name` and `age`.
    *   `for name, age in people_data`: This part iterates over all tuples in the `people_data` list. In each iteration, the tuple is unpacked into two variables: `name` and `age`.
4. **`print(people_dict)`**: Prints the created dictionary.

**Key points:**

*   List comprehension creates a list of tuples.
*   The `dict()` constructor converts a list of tuples into a dictionary, using the first element of the tuple as the key and the second as the value.
*   Unpacking tuples in the loop `for name, age in people_data` makes the code more readable.
*   List comprehension in this example is used to prepare data for the dictionary.
