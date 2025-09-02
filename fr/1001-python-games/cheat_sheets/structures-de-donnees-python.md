**1. Listes**

*   **Définition :** Les listes en Python sont des collections ordonnées et mutables d'éléments. Cela signifie que vous pouvez ajouter, supprimer et modifier des éléments dans une liste, et l'ordre des éléments est important.
*   **Représentation :** Les listes sont créées à l'aide de crochets `[]`, et les éléments sont séparés par des virgules.

*   **Exemples :**

    ```python
    # Création d'une liste
    boris_list = ["Boris", "Moscou", 30, "ingénieur"]
    print(f"Création d'une liste : {boris_list}")

    # Accès par index
    print(f"Élément à l'index 0 : {boris_list[0]}")

    # Modification d'un élément
    boris_list[2] = 31
    print(f"Modification d'un élément : {boris_list}")

    # Ajout d'un élément à la fin
    boris_list.append("marié")
    print(f"Ajout à la fin : {boris_list}")

    # Insertion d'un élément par index
    boris_list.insert(1, "Russie")
    print(f"Insertion d'un élément : {boris_list}")

    # Suppression d'un élément par valeur
    boris_list.remove("ingénieur")
    print(f"Suppression d'un élément par valeur : {boris_list}")

    # Suppression d'un élément par index
    del boris_list[2]
    print(f"Suppression d'un élément par index : {boris_list}")

    # Extension d'une liste avec une autre liste
    boris_list.extend(["hobby", "pêche"])
    print(f"Extension d'une liste : {boris_list}")

    # Suppression d'un élément de la fin
    boris_list.pop()
    print(f"Suppression d'un élément de la fin : {boris_list}")

    ```

**2. Dictionnaires**

*   **Définition :** Les dictionnaires en Python sont des collections non ordonnées d'éléments, où chaque élément est constitué d'une paire "clé-valeur".
*   **Représentation :** Les dictionnaires sont créés à l'aide d'accolades `{}`, et les paires "clé-valeur" sont séparées par deux points `:`.

*   **Exemples :**
    ```python
    # Création d'un dictionnaire
    alice_dict = {"name": "Alice", "age": 25, "city": "Londres", "occupation": "artiste"}
    print(f"Création d'un dictionnaire : {alice_dict}")

    # Accès par clé
    print(f"Valeur pour la clé 'name' : {alice_dict['name']}")

    # Modification d'une valeur
    alice_dict["age"] = 26
    print(f"Modification d'une valeur : {alice_dict}")

    # Ajout d'une paire clé-valeur
    alice_dict["hobby"] = "dessin"
    print(f"Ajout d'une paire : {alice_dict}")

    # Suppression d'une paire par clé
    del alice_dict["city"]
    print(f"Suppression d'une paire : {alice_dict}")

    # Suppression d'une paire par la méthode pop (avec valeur de retour)
    hobby = alice_dict.pop("hobby")
    print(f"Suppression avec valeur de retour : {alice_dict}, valeur : {hobby}")

    # Vérification de l'existence d'une clé
    print(f"La clé 'name' existe : {'name' in alice_dict}")
    ```

**3. Tuples**

*   **Définition :** Les tuples en Python sont des collections ordonnées et **immuables** d'éléments.
*   **Représentation :** Les tuples sont créés à l'aide de parenthèses `()`, et les éléments sont séparés par des virgules.

*   **Exemples :**

    ```python
    # Création d'un tuple
    boris_tuple = ("Boris", "Moscou", 30, "ingénieur")
    print(f"Création d'un tuple : {boris_tuple}")

    # Accès par index
    print(f"Élément à l'index 2 : {boris_tuple[2]}")

    # Impossible de modifier un élément
    # boris_tuple[0] = "Boris" # Cela lèvera une erreur : TypeError: 'tuple' object does not support item assignment

    # Impossible d'ajouter un élément
    # boris_tuple.append(4) # Cela lèvera une erreur : AttributeError: 'tuple' object has no attribute 'append'

    # Impossible de supprimer un élément
    # del boris_tuple[0]  # Cela lèvera une erreur : TypeError: 'tuple' object doesn't support item deletion
    ```

**4. SimpleNamespace**

*   **Définition :** `SimpleNamespace` du module `types` est une classe simple permettant de créer des objets dont les attributs (propriétés) peuvent être définis à la création et ultérieurement.
*   **Représentation :** Pour créer un objet `SimpleNamespace`, vous devez l'importer depuis `types` et lui passer des arguments nommés (ou ne rien passer) :
     ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="Alice", age=25, city="Londres")
    ```
*  **Caractéristiques :**
    *  Permet de créer des objets avec des attributs dynamiques (similaire à un dictionnaire).
    *  Pratique pour créer des objets simples pour le stockage de données.
    *  Les attributs sont accessibles via la notation par points, comme les objets ordinaires : `alice_namespace.name`
    *  Contrairement aux dictionnaires, l'ordre des attributs est préservé.
    *  Les champs peuvent être modifiés, mais de nouveaux champs ne peuvent pas être ajoutés.

*  **Exemples :**
    ```python
    from types import SimpleNamespace

    # Création de SimpleNamespace
    alice_namespace = SimpleNamespace(name="Alice", age=25, city="Londres")
    print(f"Création de SimpleNamespace : {alice_namespace}")

    # Accès à un attribut
    print(f"Attribut 'name' : {alice_namespace.name}")

    # Modification d'un attribut
    alice_namespace.age = 26
    print(f"Modification d'un attribut : {alice_namespace}")

    # Impossible d'ajouter un nouvel attribut
    # alice_namespace.occupation = "artiste" # Cela lèvera une erreur : AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

   # Ajout via setattr
    setattr(alice_namespace, "occupation", "artiste")
    print(f"Ajout d'un attribut : {alice_namespace}")

    # Suppression via delattr
    delattr(alice_namespace, "city")
    print(f"Suppression d'un attribut : {alice_namespace}")
    ```