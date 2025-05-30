### `question_205.md`

**Вопрос 205.** Какое ключевое слово в Python используется для указания, что переменная должна быть глобальной внутри функции?

A. `local`
B. `global`
C. `self`
D. `nonlocal`

**Правильный ответ: B**

**Объяснение:**

В Python ключевое слово `global` используется внутри функции, чтобы объявить, что переменная, к которой обращается функция, находится в глобальной области видимости.

*   **Вариант A** не верен: `local` не является ключевым словом для работы с областями видимости.
*   **Вариант B** верен: `global` используется для доступа к глобальной переменной.
*  **Вариант C** не верен: `self` используется для доступа к экземпляру объекта в методах класса.
*  **Вариант D** не верен: `nonlocal` используется для доступа к переменным внешней неглобальной функции.

**Как работает `global`:**

1. По умолчанию, переменные, объявленные внутри функции, являются локальными.
2. Чтобы изменить значение переменной в глобальной области видимости изнутри функции, ее необходимо объявить как `global` внутри этой функции.
3. Без использования `global` будет создана новая локальная переменная с таким же именем.

**Пример:**

```python
global_var: int = 10  # Глобальная переменная

def modify_global_variable():
    global global_var  # Объявляем global_var как глобальную переменную
    global_var = 20
    print(f"Значение внутри функции: {global_var}")

modify_global_variable()
print(f"Значение вне функции: {global_var}")
# Вывод:
# Значение внутри функции: 20
# Значение вне функции: 20
```

**В результате:**

* Функция `modify_global_variable` изменяет значение глобальной переменной `global_var`, поскольку она была объявлена с использованием `global`.

Таким образом, **вариант B** является правильным.
