# Singleton en `Python`

En `Python`, un singleton es un patrón de diseño que garantiza que una clase tendrá solo una instancia y proporciona un punto de acceso global a esa instancia. Esto significa que al intentar crear un nuevo objeto de esta clase, siempre obtendrá el mismo objeto.

Los singletons son útiles cuando necesita limitar el número de instancias de una clase, por ejemplo:

*   Para gestionar una conexión a la base de datos (para evitar abrir muchas conexiones).
*   Para almacenar la configuración global de la aplicación (para que todas las partes de la aplicación utilicen la misma configuración).
*   Para el registro (para que todos los mensajes vayan a un solo archivo).

Varias formas de implementar un singleton en `Python`.

<hr>

**Formas de implementar un singleton:**

1.  **Mediante la sobrescritura del método `__new__`**

    *   El método `__new__` es responsable de crear una instancia de clase. Al sobrescribirlo, puedo controlar este proceso.
    *   En este ejemplo, almacenaré la única instancia de la clase en la variable `_instance`.
    *   Si la instancia aún no existe, la crearé; de lo contrario, devolveré la instancia existente.
    *   **Código `Python`:**

        ```python
        class Singleton:
            _instance = None  # Almacena la única instancia

            def __new__(cls, *args, **kwargs):
                """
                Sobrescribe el método __new__ para controlar la creación de instancias.

                Args:
                    cls: La clase para la que se está creando la instancia.
                    *args: Argumentos posicionales para el constructor.
                    **kwargs: Argumentos de palabra clave para el constructor.

                Returns:
                    La única instancia de la clase.
                """
                if not cls._instance: # Si la instancia aún no se ha creado
                    cls._instance = super().__new__(cls, *args, **kwargs) # Crea una nueva instancia
                return cls._instance # Devuelve la instancia existente

        # Ejemplo de uso
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Imprimirá True, ya que es el mismo objeto
        ```
<hr>

2.  **Mediante un decorador**

    *   Un decorador es una función que modifica una clase.
    *   En este ejemplo, crearé una función decoradora `singleton` que toma una clase y devuelve su versión envuelta.
    *   Dentro del decorador, almaceno las instancias de clase en el diccionario `instances`.
    *   Si aún no se ha creado una instancia de clase, la crearé y la almacenaré en el diccionario; de lo contrario, devolveré la instancia existente.
    *   **Código `Python`:**

        ```python
        def singleton(cls):
            """
            Decorador para crear un singleton.

            Args:
                cls: La clase a convertir en singleton.

            Returns:
                La clase modificada, que es un singleton.
            """
            instances = {} # Almacena instancias de clase

            def wrapper(*args, **kwargs):
                """
                Función envoltorio que devuelve la única instancia de la clase.

                Args:
                   *args: Argumentos posicionales para el constructor.
                   **kwargs: Argumentos de palabra clave para el constructor.

                Returns:
                    La única instancia de la clase.
                """
                if cls not in instances: # Si la instancia aún no se ha creado
                    instances[cls] = cls(*args, **kwargs) # Crea una instancia y la almacena
                return instances[cls] # Devuelve la instancia existente
            return wrapper

        @singleton # Aplica el decorador a la clase
        class MyClass:
            pass

        # Ejemplo de uso
        obj1 = MyClass()
        obj2 = MyClass()

        print(obj1 is obj2)  # Imprimirá True, ya que es el mismo objeto
        ```
<hr>

3.  **Mediante una metaclase**

    *   Una metaclase permite controlar la creación de clases.
    *   En este ejemplo, crearé una metaclase `SingletonMeta` que supervisará la creación de instancias.
    *   La metaclase almacena las instancias de clase en el diccionario `_instances`.
    *   Al crear una nueva instancia, compruebo si ya existe en el diccionario; si no, la creo; de lo contrario, devuelvo la instancia existente.
    *   **Código `Python`:**

        ```python
        class SingletonMeta(type):
            """
            Metaclase para crear un singleton.
            """
            _instances = {} # Almacena instancias

            def __call__(cls, *args, **kwargs):
                """
                Sobrescribe el método __call__ para controlar la creación de instancias.

                Args:
                    cls: La clase para la que se está creando la instancia.
                    *args: Argumentos posicionales para el constructor.
                    **kwargs: Argumentos de palabra clave para el constructor.

                Returns:
                    La única instancia de la clase.
                """
                if cls not in cls._instances: # Si la instancia aún no se ha creado
                    cls._instances[cls] = super().__call__(*args, **kwargs) # Crea una nueva instancia
                return cls._instances[cls] # Devuelve la instancia existente

        class Singleton(metaclass=SingletonMeta):
            """
            Clase que es un singleton.
            """
            pass

        # Ejemplo de uso
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Imprimirá True, ya que es el mismo objeto
             ```
  <hr> 

4.  **Mediante un módulo**

    *   En `Python`, un módulo es en sí mismo un singleton.
    *   Puedo crear un objeto en un módulo, y será la única instancia.
    *   **Código `Python`:**
        ```python
        # Archivo singleton.py
        class Singleton:
            pass

        instance = Singleton()
        ```
        ```python
        # En otro archivo
        from singleton import instance

        obj1 = instance
        obj2 = instance

        print(obj1 is obj2)  # Imprimirá True, ya que es el mismo objeto
        ```

**Ventajas del singleton:**

*   **Garantía de instancia única:** Un singleton garantiza que una clase tendrá solo una instancia. Esto es útil para gestionar recursos que deben ser únicos.
*   **Acceso global:** Un singleton proporciona un punto de acceso global a la instancia de la clase, lo que simplifica el uso de esta instancia en cualquier parte del programa.

**Desventajas del singleton:**

*   **Estado global:** Un singleton puede llevar al uso de estado global, lo que puede causar efectos secundarios inesperados y complicar las pruebas.
*   **Violación de los principios de la POO:** Un singleton puede violar el principio de responsabilidad única y la encapsulación.

**¿Cuándo usar un singleton?**

*   Cuando necesita que un objeto exista como una única instancia (por ejemplo, configuración, registrador, conexión a la base de datos).
*   Cuando necesita acceso global a este objeto.

