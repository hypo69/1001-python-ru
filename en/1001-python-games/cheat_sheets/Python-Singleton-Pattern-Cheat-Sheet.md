# Singleton Pattern in `Python`

In `Python`, the Singleton pattern is a design pattern that ensures a class has only one instance and provides a global point of access to that instance. This means that when you try to create a new object of this class, you will always get the same object.

Singletons are useful when you need to limit the number of instances of a class, for example:

*   To manage database connections (to avoid opening many connections).
*   To store global application configuration (so that all parts of the application use the same configuration).
*   For logging (so that all messages go to one file).

Several ways to implement a singleton in `Python`.

<hr>

**Ways to implement a singleton:**

1.  **By overriding the `__new__` method**

    *   The `__new__` method is responsible for creating a class instance. By overriding it, I can control this process.
    *   In this example, I will store the single instance of the class in the `_instance` variable.
    *   If the instance does not exist yet, I will create it; otherwise, I will return the existing instance.
    *   **`Python` Code:**

        ```python
        class Singleton:
            _instance = None  # Stores the single instance

            def __new__(cls, *args, **kwargs):
                """
                Overrides the __new__ method to control instance creation.

                Args:
                    cls: The class for which the instance is being created.
                    *args: Positional arguments for the constructor.
                    **kwargs: Keyword arguments for the constructor.

                Returns:
                    The single instance of the class.
                """
                if not cls._instance: # If the instance has not been created yet
                    cls._instance = super().__new__(cls, *args, **kwargs) # Create a new instance
                return cls._instance # Return the existing instance

        # Example usage
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Will print True, as it's the same object
        ```
<hr>

2.  **Using a decorator**

    *   A decorator is a function that modifies a class.
    *   In this example, I create a decorator function `singleton` that takes a class and returns its wrapped version.
    *   Inside the decorator, I store class instances in the `instances` dictionary.
    *   If the class instance has not been created yet, I will create it and save it in the dictionary; otherwise, I will return the existing instance.
    *   **`Python` Code:**

        ```python
        def singleton(cls):
            """
            Decorator for creating a singleton.

            Args:
                cls: The class to make a singleton.

            Returns:
                The modified class, which is a singleton.
            """
            instances = {} # Stores instances

            def wrapper(*args, **kwargs):
                """
                Wrapper function that returns the single instance of the class.

                Args:
                   *args: Positional arguments for the constructor.
                   **kwargs: Keyword arguments for the constructor.

                Returns:
                    The single instance of the class.
                """
                if cls not in instances: # If the instance has not been created yet
                    instances[cls] = cls(*args, **kwargs) # Create an instance and save it
                return instances[cls] # Return the existing instance
            return wrapper

        @singleton # Apply the decorator to the class
        class MyClass:
            pass

        # Example usage
        obj1 = MyClass()
        obj2 = MyClass()

        print(obj1 is obj2)  # Will print True, as it's the same object
        ```
<hr>

3.  **Using a metaclass**

    *   A metaclass allows you to control class creation.
    *   In this example, I will create a metaclass `SingletonMeta` that will monitor instance creation.
    *   The metaclass stores class instances in the `_instances` dictionary.
    *   When creating a new instance, I check if it's already in the dictionary; if not, I create it; otherwise, I return the existing instance.
    *   **`Python` Code:**

        ```python
        class SingletonMeta(type):
            """
            Metaclass for creating a singleton.
            """
            _instances = {} # Stores instances

            def __call__(cls, *args, **kwargs):
                """
                Overrides the __call__ method to control instance creation.

                Args:
                    cls: The class for which the instance is being created.
                    *args: Positional arguments for the constructor.
                    **kwargs: Keyword arguments for the constructor.

                Returns:
                    The single instance of the class.
                """
                if cls not in cls._instances: # If the instance has not been created yet
                    cls._instances[cls] = super().__call__(*args, **kwargs) # Create a new instance
                return cls._instances[cls] # Return the existing instance

        class Singleton(metaclass=SingletonMeta):
            """
            A class that is a singleton.
            """
            pass

        # Example usage
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Will print True, as it's the same object
             ```
  <hr> 

4.  **Using a module**

    *   In `Python`, a module itself is a singleton.
    *   I can create an object in a module, and it will be the only instance.
    *   **`Python` Code:**
        ```python
        # singleton.py file
        class Singleton:
            pass

        instance = Singleton()
        ```
        ```python
        # In another file
        from singleton import instance

        obj1 = instance
        obj2 = instance

        print(obj1 is obj2)  # Will print True, as it's the same object
        ```

**Advantages of Singleton:**

*   **Guaranteed single instance:** Singleton ensures that a class will have only one instance. This is useful for managing resources that must be unique.
*   **Global access:** Singleton provides a global point of access to the class instance, which simplifies the use of this instance in any part of the program.

**Disadvantages of Singleton:**

*   **Global state:** Singleton can lead to the use of global state, which can cause unexpected side effects and complicate testing.
*   **Violation of OOP principles:** Singleton can violate the single responsibility principle and encapsulation.

**When to use Singleton?**

*   When you need an object to exist as a single instance (e.g., configuration, logger, database connection).
*   When you need global access to this object.
