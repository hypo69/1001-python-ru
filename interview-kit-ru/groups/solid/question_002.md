### `question_002.md` (SRP - Пример нарушения)

**Вопрос 002.** Какой из следующих примеров кода на Python *наиболее явно* нарушает принцип единственной ответственности (SRP)?

A.
```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
```

B.

```python
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def send_email(self, message):
        # Code to send email
        pass
```

C.

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, password):
        return self.password == password
```

D.

```python
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def save_to_database(self):
        # Code to save user data to database
        pass

    def send_welcome_email(self):
        # Code to send a welcome email to the user
        pass
```

**Правильный ответ: D**

**Объяснение:**

Принцип единственной ответственности (SRP) гласит, что класс должен иметь только одну причину для изменения. В варианте D класс `User` имеет *две явно выраженные* ответственности: управление данными пользователя и взаимодействие с базой данных и отправку приветственного письма.

*   **Вариант A:** Класс `User` отвечает только за хранение и изменение данных пользователя.
*   **Вариант B:** Класс `User` отвечает только за хранение данных пользователя и отправку email.
*   **Вариант C:** Класс `User` отвечает только за хранение данных пользователя и аутентификацию.
*   **Вариант D:** Класс `User` отвечает за:
    *   Управление данными пользователя.
    *   Сохранение данных в базе данных.
    *   Отправку приветственного письма. - *нарушение SRP*

**Пример рефакторинга (упрощенно):**

```python
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def save(self, user: User):
        # Code to save user data to database
        pass

class EmailService:
    def send_welcome_email(self, user: User):
        # Code to send a welcome email to the user
        pass
```
**В результате:**

Наиболее явное нарушение SRP происходит в варианте D, где класс `User` имеет несколько несвязанных обязанностей.

Таким образом, вариант D является правильным.
