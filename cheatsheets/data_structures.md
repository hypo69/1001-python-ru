
**1. Списки (Lists)**

*   **Определение:** Списки в Python – это упорядоченные, изменяемые коллекции элементов. Это значит, что ты можешь добавлять, удалять и изменять элементы в списке, и порядок элементов имеет значение.
*   **Представление:** Списки создаются с помощью квадратных скобок `[]`, а элементы разделяются запятыми.

*   **Примеры:**

    ```python
    # Создание списка
    boris_list = ["Борис", "Москва", 30, "инженер"]
    print(f"Создание списка: {boris_list}")

    # Доступ по индексу
    print(f"Элемент по индексу 0: {boris_list[0]}")

    # Изменение элемента
    boris_list[2] = 31
    print(f"Изменение элемента: {boris_list}")

    # Добавление элемента в конец
    boris_list.append("женат")
    print(f"Добавление в конец: {boris_list}")

    # Вставка элемента по индексу
    boris_list.insert(1, "Россия")
    print(f"Вставка элемента: {boris_list}")

    # Удаление элемента по значению
    boris_list.remove("инженер")
    print(f"Удаление элемента по значению: {boris_list}")

    # Удаление элемента по индексу
    del boris_list[2]
    print(f"Удаление элемента по индексу: {boris_list}")

    # Расширение списка другим списком
    boris_list.extend(["хобби", "рыбалка"])
    print(f"Расширение списка: {boris_list}")

    # Удаление элемента с конца
    boris_list.pop()
    print(f"Удаление элемента с конца: {boris_list}")

    ```

**2. Словари (Dictionaries)**

*   **Определение:** Словари в Python – это неупорядоченные коллекции элементов, где каждый элемент состоит из пары "ключ-значение".
*   **Представление:** Словари создаются с помощью фигурных скобок `{}`, а пары "ключ-значение" разделяются двоеточием `:`.

*   **Примеры:**
    ```python
    # Создание словаря
    alice_dict = {"name": "Алиса", "age": 25, "city": "Лондон", "occupation": "художница"}
    print(f"Создание словаря: {alice_dict}")

    # Доступ по ключу
    print(f"Значение по ключу 'name': {alice_dict['name']}")

    # Изменение значения
    alice_dict["age"] = 26
    print(f"Изменение значения: {alice_dict}")

    # Добавление пары ключ-значение
    alice_dict["hobby"] = "рисование"
    print(f"Добавление пары: {alice_dict}")

    # Удаление пары по ключу
    del alice_dict["city"]
    print(f"Удаление пары: {alice_dict}")

    # Удаление пары методом pop (с возвращением значения)
    hobby = alice_dict.pop("hobby")
    print(f"Удаление с возвратом значения: {alice_dict}, значение: {hobby}")

    # Проверка наличия ключа
    print(f"Наличие ключа 'name': {'name' in alice_dict}")
    ```

**3. Кортежи (Tuples)**

*   **Определение:** Кортежи в Python – это упорядоченные, **неизменяемые** коллекции элементов.
*   **Представление:** Кортежи создаются с помощью круглых скобок `()`, а элементы разделяются запятыми.

*   **Примеры:**

    ```python
    # Создание кортежа
    boris_tuple = ("Борис", "Москва", 30, "инженер")
    print(f"Создание кортежа: {boris_tuple}")

    # Доступ по индексу
    print(f"Элемент по индексу 2: {boris_tuple[2]}")

    # Нельзя изменить элемент
    # boris_tuple[0] = "Борис" # Это вызовет ошибку: TypeError: 'tuple' object does not support item assignment

    # Нельзя добавить элемент
    # boris_tuple.append(4) # Это вызовет ошибку: AttributeError: 'tuple' object has no attribute 'append'

    # Нельзя удалить элемент
    # del boris_tuple[0]  # Это вызовет ошибку: TypeError: 'tuple' object doesn't support item deletion
    ```

**4. SimpleNamespace**

*   **Определение:** `SimpleNamespace` из модуля `types` - это простой класс, позволяющий создавать объекты, у которых атрибуты (свойства) можно задавать как при создании, так и потом.
*   **Представление:** Для создания объекта `SimpleNamespace` нужно импортировать его из `types` и передать в него именованные аргументы (или не передать их):
     ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="Алиса", age=25, city="Лондон")
    ```
*  **Особенности:**
    *  Позволяет создавать объекты с динамическими атрибутами (похоже на словарь).
    *  Удобен для создания простых объектов для хранения данных.
    *  Атрибуты доступны через точку, как у обычных объектов: `alice_namespace.name`
    *  В отличие от словарей, порядок атрибутов сохраняется.
    *  Поля можно менять, но нельзя добавлять новые поля

*  **Примеры:**
    ```python
    from types import SimpleNamespace

    # Создание SimpleNamespace
    alice_namespace = SimpleNamespace(name="Алиса", age=25, city="Лондон")
    print(f"Создание SimpleNamespace: {alice_namespace}")

    # Доступ к атрибуту
    print(f"Атрибут 'name': {alice_namespace.name}")

    # Изменение атрибута
    alice_namespace.age = 26
    print(f"Изменение атрибута: {alice_namespace}")

    # Нельзя добавить новый атрибут
    # alice_namespace.occupation = "художница" # Это вызовет ошибку: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

   # Добавление через setattr
    setattr(alice_namespace, "occupation", "художница")
    print(f"Добавление атрибута: {alice_namespace}")

    # Удаление через delattr
    delattr(alice_namespace, "city")
    print(f"Удаление атрибута: {alice_namespace}")
    ```
