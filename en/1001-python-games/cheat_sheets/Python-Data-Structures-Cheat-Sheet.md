**1. Lists**

*   **Definition:** Lists in Python are ordered, mutable collections of items. This means you can add, remove, and change items in the list, and the order of items matters.
*   **Representation:** Lists are created using square brackets `[]`, and items are separated by commas.

*   **Examples:**

    ```python
    # Creating a list
    boris_list = ["Boris", "Moscow", 30, "engineer"]
    print(f"Creating a list: {boris_list}")

    # Access by index
    print(f"Element at index 0: {boris_list[0]}")

    # Modifying an element
    boris_list[2] = 31
    print(f"Modifying an element: {boris_list}")

    # Adding an element to the end
    boris_list.append("married")
    print(f"Adding to the end: {boris_list}")

    # Inserting an element by index
    boris_list.insert(1, "Russia")
    print(f"Inserting an element: {boris_list}")

    # Removing an element by value
    boris_list.remove("engineer")
    print(f"Removing an element by value: {boris_list}")

    # Removing an element by index
    del boris_list[2]
    print(f"Removing an element by index: {boris_list}")

    # Extending a list with another list
    boris_list.extend(["hobby", "fishing"])
    print(f"Extending a list: {boris_list}")

    # Removing an element from the end
    boris_list.pop()
    print(f"Removing an element from the end: {boris_list}")

    ```

**2. Dictionaries**

*   **Definition:** Dictionaries in Python are unordered collections of items, where each item consists of a "key-value" pair.
*   **Representation:** Dictionaries are created using curly braces `{}`, and "key-value" pairs are separated by a colon `:`.

*   **Examples:**
    ```python
    # Creating a dictionary
    alice_dict = {"name": "Alice", "age": 25, "city": "London", "occupation": "artist"}
    print(f"Creating a dictionary: {alice_dict}")

    # Access by key
    print(f"Value for key 'name': {alice_dict['name']}")

    # Modifying a value
    alice_dict["age"] = 26
    print(f"Modifying a value: {alice_dict}")

    # Adding a key-value pair
    alice_dict["hobby"] = "drawing"
    print(f"Adding a pair: {alice_dict}")

    # Removing a key-value pair by key
    del alice_dict["city"]
    print(f"Removing a pair: {alice_dict}")

    # Removing a pair using pop method (with value return)
    hobby = alice_dict.pop("hobby")
    print(f"Removing with value return: {alice_dict}, value: {hobby}")

    # Checking for key existence
    print(f"Key 'name' exists: {'name' in alice_dict}")
    ```

**3. Tuples**

*   **Definition:** Tuples in Python are ordered, **immutable** collections of items.
*   **Representation:** Tuples are created using parentheses `()`, and items are separated by commas.

*   **Examples:**

    ```python
    # Creating a tuple
    boris_tuple = ("Boris", "Moscow", 30, "engineer")
    print(f"Creating a tuple: {boris_tuple}")

    # Access by index
    print(f"Element at index 2: {boris_tuple[2]}")

    # Cannot modify an element
    # boris_tuple[0] = "Boris" # This will raise an error: TypeError: 'tuple' object does not support item assignment

    # Cannot add an element
    # boris_tuple.append(4) # This will raise an error: AttributeError: 'tuple' object has no attribute 'append'

    # Cannot remove an element
    # del boris_tuple[0]  # This will raise an error: TypeError: 'tuple' object doesn't support item deletion
    ```

**4. SimpleNamespace**

*   **Definition:** `SimpleNamespace` from the `types` module is a simple class that allows creating objects whose attributes (properties) can be set both at creation and later.
*   **Representation:** To create a `SimpleNamespace` object, you need to import it from `types` and pass named arguments to it (or not pass them):
     ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="Alice", age=25, city="London")
    ```
*  **Features:**
    *  Allows creating objects with dynamic attributes (similar to a dictionary).
    *  Convenient for creating simple objects for data storage.
    *  Attributes are accessible via dot notation, like regular objects: `alice_namespace.name`
    *  Unlike dictionaries, the order of attributes is preserved.
    *  Fields can be changed, but new fields cannot be added directly.

*  **Examples:**
    ```python
    from types import SimpleNamespace

    # Creating SimpleNamespace
    alice_namespace = SimpleNamespace(name="Alice", age=25, city="London")
    print(f"Creating SimpleNamespace: {alice_namespace}")

    # Accessing an attribute
    print(f"Attribute 'name': {alice_namespace.name}")

    # Modifying an attribute
    alice_namespace.age = 26
    print(f"Modifying an attribute: {alice_namespace}")

    # Cannot add a new attribute directly
    # alice_namespace.occupation = "artist" # This will raise an error: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

   # Adding via setattr
    setattr(alice_namespace, "occupation", "artist")
    print(f"Adding an attribute: {alice_namespace}")

    # Deleting via delattr
    delattr(alice_namespace, "city")
    print(f"Deleting an attribute: {alice_namespace}")
    ```
