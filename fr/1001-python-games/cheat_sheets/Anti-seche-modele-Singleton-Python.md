# Singleton (modèle de conception) en `Python`

En `Python`, le singleton est un modèle de conception qui garantit qu'une classe n'aura qu'une seule instance et fournit un point d'accès global à cette instance. Cela signifie que lorsque vous tentez de créer un nouvel objet de cette classe, vous obtiendrez toujours le même objet.

Les singletons sont utiles lorsque vous devez limiter le nombre d'instances d'une classe, par exemple :

*   Pour gérer la connexion à une base de données (afin de ne pas ouvrir de nombreuses connexions).
*   Pour stocker la configuration globale de l'application (afin que toutes les parties de l'application utilisent la même configuration).
*   Pour la journalisation (afin que tous les messages aillent dans un seul fichier).

Plusieurs façons d'implémenter un singleton en `Python`.

<hr>

**Méthodes d'implémentation du singleton :**

1.  **Par redéfinition de la méthode `__new__`**

    *   La méthode `__new__` est responsable de la création d'une instance de classe. En la redéfinissant, je peux contrôler ce processus.
    *   Dans cet exemple, je stockerai l'instance unique de la classe dans la variable `_instance`.
    *   Si l'instance n'existe pas encore, je la créerai, sinon je renverrai l'instance déjà existante.
    *   **Code `Python` :**

        ```python
        class Singleton:
            _instance = None  # Stocke l'instance unique

            def __new__(cls, *args, **kwargs):
                """
                Redéfinit la méthode __new__ pour contrôler la création d'instance.

                Args:
                    cls: La classe pour laquelle l'instance est créée.
                    *args: Arguments positionnels pour le constructeur.
                    **kwargs: Arguments nommés pour le constructeur.

                Returns:
                    L'instance unique de la classe.
                """
                if not cls._instance: # Si l'instance n'a pas encore été créée
                    cls._instance = super().__new__(cls, *args, **kwargs) # Crée une nouvelle instance
                return cls._instance # Renvoie l'instance existante

        # Exemple d'utilisation
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Affichera True, car c'est le même objet
        ```
<hr>

2.  **Via un décorateur**

    *   Un décorateur est une fonction qui modifie une classe.
    *   Dans cet exemple, je crée une fonction décoratrice `singleton` qui prend une classe et renvoie sa version enveloppée.
    *   À l'intérieur du décorateur, je stocke les instances de classe dans le dictionnaire `instances`.
    *   Si l'instance de classe n'a pas encore été créée, je la créerai et la stockerai dans le dictionnaire, sinon je renverrai l'instance existante.
    *   **Code `Python` :**

        ```python
        def singleton(cls):
            """
            Décorateur pour créer un singleton.

            Args:
                cls: La classe à transformer en singleton.

            Returns:
                La classe modifiée, qui est un singleton.
            """
            instances = {} # Stocke les instances

            def wrapper(*args, **kwargs):
                """
                Fonction d'enveloppe qui renvoie l'instance unique de la classe.

                Args:
                   *args: Arguments positionnels pour le constructeur.
                   **kwargs: Arguments nommés pour le constructeur.

                Returns:
                    L'instance unique de la classe.
                """
                if cls not in instances: # Si l'instance n'a pas encore été créée
                    instances[cls] = cls(*args, **kwargs) # Crée une instance et l'enregistre
                return instances[cls] # Renvoie l'instance existante
            return wrapper

        @singleton # Applique le décorateur à la classe
        class MyClass:
            pass

        # Exemple d'utilisation
        obj1 = MyClass()
        obj2 = MyClass()

        print(obj1 is obj2)  # Affichera True, car c'est le même objet
        ```
<hr>

3.  **Via une métaclasse**

    *   Une métaclasse permet de contrôler la création de classes.
    *   Dans cet exemple, je vais créer une métaclasse `SingletonMeta` qui surveillera la création d'instances.
    *   La métaclasse stocke les instances de classe dans le dictionnaire `_instances`.
    *   Lors de la création d'une nouvelle instance, je vérifie si elle est déjà dans le dictionnaire ; si ce n'est pas le cas, je la crée ; sinon, je renvoie l'instance existante.
    *   **Code `Python` :**

        ```python
        class SingletonMeta(type):
            """
            Métaclasse pour créer un singleton.
            """
            _instances = {} # Stocke les instances

            def __call__(cls, *args, **kwargs):
                """
                Redéfinit la méthode __call__ pour contrôler la création d'instance.

                Args:
                    cls: La classe pour laquelle l'instance est créée.
                    *args: Arguments positionnels pour le constructeur.
                    **kwargs: Arguments nommés pour le constructeur.

                Returns:
                    L'instance unique de la classe.
                """
                if cls not in cls._instances: # Si l'instance n'a pas encore été créée
                    cls._instances[cls] = super().__call__(*args, **kwargs) # Crée une nouvelle instance
                return cls._instances[cls] # Renvoie l'instance existante

        class Singleton(metaclass=SingletonMeta):
            """
            Classe qui est un singleton.
            """
            pass

        # Exemple d'utilisation
        s1 = Singleton()
        s2 = Singleton()

        print(s1 is s2)  # Affichera True, car c'est le même objet
             ```
  <hr> 

4.  **Via un module**

    *   En `Python`, un module est un singleton en soi.
    *   Je peux créer un objet dans un module, et ce sera la seule instance.
    *   **Code `Python` :**
        ```python
        # Fichier singleton.py
        class Singleton:
            pass

        instance = Singleton()
        ```
        ```python
        # Dans un autre fichier
        from singleton import instance

        obj1 = instance
        obj2 = instance

        print(obj1 is obj2)  # Affichera True, car c'est le même objet
        ```

**Avantages du singleton :**

*   **Garantie d'une instance unique :** Le singleton garantit qu'une classe n'aura qu'une seule instance. C'est utile pour gérer des ressources qui doivent être uniques.
*   **Accès global :** Le singleton fournit un point d'accès global à l'instance de la classe, ce qui simplifie l'utilisation de cette instance dans n'importe quelle partie du programme.

**Inconvénients du singleton :**

*   **État global :** Le singleton peut entraîner l'utilisation d'un état global, ce qui peut provoquer des effets secondaires inattendus et compliquer les tests.
*   **Violation des principes de la POO :** Le singleton peut violer le principe de responsabilité unique et l'encapsulation.

**Quand utiliser le singleton ?**

*   Lorsque vous avez besoin qu'un objet existe en une seule instance (par exemple, configuration, journalisation, connexion à une base de données).
*   Lorsque vous avez besoin d'un accès global à cet objet.
