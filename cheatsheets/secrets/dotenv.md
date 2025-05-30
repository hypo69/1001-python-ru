# Безопасное хранение ключей и паролей в Python с помощью `.env` файлов

Когда мы пишем код, особенно для проектов, взаимодействующих с внешними сервисами, нам приходится использовать чувствительные данные: пароли, ключи API, токены доступа и т.д. Вшивать такие значения прямо в код — **опасно и недопустимо**. Вместо этого стоит использовать `.env` файл.

## Что такое `.env` файл?

`.env` — это простой текстовый файл, в котором каждая строка содержит переменную окружения в формате:

```
API_KEY=your-secret-api-key
DB_PASSWORD=super-secret-password
```

Этот файл **не попадает в систему контроля версий** (Git) и используется только локально для конфигурации.

## Почему нельзя хранить секреты в коде?

Примеры плохой практики:

```python
API_KEY = "sk-1234567890abcdef"  # ❌
```

Если такой код попадёт в публичный репозиторий — вы случайно раскрываете секреты. Даже если удалите файл позже — история коммитов сохранит ключ.

## Установка python-dotenv

Для работы с `.env` в Python чаще всего используют библиотеку [`python-dotenv`](https://github.com/theskumar/python-dotenv).

Установите её:

```bash
pip install python-dotenv
```

## Как использовать `.env` в Python

1. Создайте файл `.env` в корне проекта:

```
API_KEY=sk-1234567890abcdef
DB_PASSWORD=my_db_password
```

2. Добавьте `.env` в `.gitignore`, чтобы он не попал в Git:

```
.env
```

3. Загрузите переменные в Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # загружает переменные из .env

api_key = os.getenv("API_KEY")
db_password = os.getenv("DB_PASSWORD")
```

Теперь переменные `api_key` и `db_password` доступны в вашем коде без явного указания значений.

## Продвинутый пример

Если вы хотите загрузить `.env` из конкретного пути:

```python
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / 'config' / '.env'
load_dotenv(dotenv_path=env_path)

token = os.getenv("TG_BOT_TOKEN")
```

## Альтернатива: переменные окружения в системе

Вы можете также установить переменные окружения напрямую в ОС (например, в CI/CD или Docker-контейнере), и использовать `os.getenv()` без `python-dotenv`.

## Лучшие практики

* Никогда не коммитьте `.env` файл — добавьте его в `.gitignore`.
* Храните `.env.example` с пустыми значениями как шаблон:

```
# .env.example
API_KEY=
DB_PASSWORD=
```

* Используйте разные `.env` файлы для разных окружений:

  * `.env.dev`
  * `.env.prod`
  * `.env.test`

И загружайте нужный по контексту.

## Заключение

Использование `.env` файлов — это простой, но важный шаг к повышению безопасности и гибкости проекта. Он помогает:

* отделить конфигурацию от кода,
* защитить чувствительные данные,
* упростить развертывание в разных средах.

Не храните секреты в коде. Используйте `.env`, и пусть ваш проект будет не только функциональным, но и безопасным.
