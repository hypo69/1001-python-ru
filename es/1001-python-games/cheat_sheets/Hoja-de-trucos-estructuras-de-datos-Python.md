**1. Listas (Lists)**

*   **Definición:** Las listas en Python son colecciones ordenadas y mutables de elementos. Esto significa que puede agregar, eliminar y cambiar elementos en la lista, y el orden de los elementos importa.
*   **Representación:** Las listas se crean usando corchetes `[]`, y los elementos se separan con comas.

*   **Ejemplos:**

    ```python
    # Creación de una lista
    boris_list = ["Boris", "Moscú", 30, "ingeniero"]
    print(f"Creación de una lista: {boris_list}")

    # Acceso por índice
    print(f"Elemento en el índice 0: {boris_list[0]}")

    # Modificación de un elemento
    boris_list[2] = 31
    print(f"Modificación de un elemento: {boris_list}")

    # Agregar un elemento al final
    boris_list.append("casado")
    print(f"Agregar al final: {boris_list}")

    # Insertar un elemento por índice
    boris_list.insert(1, "Rusia")
    print(f"Insertar un elemento: {boris_list}")

    # Eliminar un elemento por valor
    boris_list.remove("ingeniero")
    print(f"Eliminar un elemento por valor: {boris_list}")

    # Eliminar un elemento por índice
    del boris_list[2]
    print(f"Eliminar un elemento por índice: {boris_list}")

    # Extender una lista con otra lista
    boris_list.extend(["hobby", "pesca"])
    print(f"Extender una lista: {boris_list}")

    # Eliminar un elemento del final
    boris_list.pop()
    print(f"Eliminar un elemento del final: {boris_list}")

    ```

**2. Diccionarios (Dictionaries)**

*   **Definición:** Los diccionarios en Python son colecciones desordenadas de elementos, donde cada elemento consta de un par "clave-valor".
*   **Representación:** Los diccionarios se crean usando llaves `{}`, y los pares "clave-valor" se separan con dos puntos `:`.

*   **Ejemplos:**
    ```python
    # Creación de un diccionario
    alice_dict = {"name": "Alicia", "age": 25, "city": "Londres", "occupation": "artista"}
    print(f"Creación de un diccionario: {alice_dict}")

    # Acceso por clave
    print(f"Valor para la clave 'name': {alice_dict['name']}")

    # Modificación de un valor
    alice_dict["age"] = 26
    print(f"Modificación de un valor: {alice_dict}")

    # Agregar un par clave-valor
    alice_dict["hobby"] = "dibujo"
    print(f"Agregar un par: {alice_dict}")

    # Eliminar un par por clave
    del alice_dict["city"]
    print(f"Eliminar un par: {alice_dict}")

    # Eliminar un par usando el método pop (con retorno de valor)
    hobby = alice_dict.pop("hobby")
    print(f"Eliminar con retorno de valor: {alice_dict}, valor: {hobby}")

    # Comprobar la existencia de una clave
    print(f"La clave 'name' existe: {'name' in alice_dict}")
    ```

**3. Tuplas (Tuples)**

*   **Definición:** Las tuplas en Python son colecciones ordenadas e **inmutables** de elementos.
*   **Representación:** Las tuplas se crean usando paréntesis `()`, y los elementos se separan con comas.

*   **Ejemplos:**

    ```python
    # Creación de una tupla
    boris_tuple = ("Boris", "Moscú", 30, "ingeniero")
    print(f"Creación de una tupla: {boris_tuple}")

    # Acceso por índice
    print(f"Elemento en el índice 2: {boris_tuple[2]}")

    # No se puede modificar un elemento
    # boris_tuple[0] = "Boris" # Esto generará un error: TypeError: 'tuple' object does not support item assignment

    # No se puede agregar un elemento
    # boris_tuple.append(4) # Esto generará un error: AttributeError: 'tuple' object has no attribute 'append'

    # No se puede eliminar un elemento
    # del boris_tuple[0]  # Esto generará un error: TypeError: 'tuple' object doesn't support item deletion
    ```

**4. SimpleNamespace**

*   **Definición:** `SimpleNamespace` del módulo `types` es una clase simple que permite crear objetos cuyos atributos (propiedades) se pueden establecer tanto en la creación como posteriormente.
*   **Representación:** Para crear un objeto `SimpleNamespace`, debe importarlo de `types` y pasarle argumentos con nombre (o no pasarlos):
     ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="Alicia", age=25, city="Londres")
    ```
*  **Características:**
    *  Permite crear objetos con atributos dinámicos (similar a un diccionario).
    *  Conveniente para crear objetos simples para el almacenamiento de datos.
    *  Los atributos son accesibles a través de la notación de puntos, como los objetos normales: `alice_namespace.name`
    *  A diferencia de los diccionarios, el orden de los atributos se conserva.
    *  Los campos se pueden cambiar, pero no se pueden agregar campos nuevos directamente.

*  **Ejemplos:**
    ```python
    from types import SimpleNamespace

    # Creación de SimpleNamespace
    alice_namespace = SimpleNamespace(name="Alicia", age=25, city="Londres")
    print(f"Creación de SimpleNamespace: {alice_namespace}")

    # Acceso a un atributo
    print(f"Atributo 'name': {alice_namespace.name}")

    # Modificación de un atributo
    alice_namespace.age = 26
    print(f"Modificación de un atributo: {alice_namespace}")

    # No se puede agregar un nuevo atributo directamente
    # alice_namespace.occupation = "artista" # Esto generará un error: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

   # Agregar a través de setattr
    setattr(alice_namespace, "occupation", "artista")
    print(f"Agregar un atributo: {alice_namespace}")

    # Eliminar a través de delattr
    delattr(alice_namespace, "city")
    print(f"Eliminar un atributo: {alice_namespace}")
    ```
