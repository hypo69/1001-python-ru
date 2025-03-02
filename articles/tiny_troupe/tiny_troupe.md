# Создание интеллектуальных агентов с TinyTroupe: Пошаговое руководство

## Введение

**Что такое TinyTroupe?**

TinyTroupe — это экспериментальная Python-библиотека от Microsoft, предназначенная для моделирования людей с определёнными личностными характеристиками, интересами и целями. Эти искусственные агенты, называемые «TinyPerson», могут взаимодействовать между собой и с окружающей средой, имитируя реалистичное поведение.

**Что такое TinyPerson?**

В основе TinyTroupe лежит класс `TinyPerson`. 
`TinyPerson` - это основной строительный блок для создания сложных, управляемых LLM агентов.  
Экспериментируйте с различными промптами, конфигурациями памяти и ментальными способностями, 
чтобы раскрыть весь потенциал моделирования человеческого поведения.

Представьте его как чертеж для смоделированной личности. Каждая `TinyPerson` обладает:

*   **Имя:** Уникальный идентификатор.
*   **Когнитивные состояния:** Внутренние переменные, представляющие внимание, эмоции, цели и другие ментальные аспекты, влияющие на поведение.
*   **Память:** Разделенная на `episodic_memory` (конкретные события) и `semantic_memory` (общие знания), отражая структуру человеческой памяти.
*   **Поведенческие абстракции:** Методы `listen()` и `act()` имеют решающее значение для взаимодействия, моделируя циклы стимул-реакция.

## Установка

В папке ваших проектов выполните команду 

```bash
git clone https://github.com/microsoft/TinyTroupe.git
cd TinyTroupe
python -m venv venv
venv\Scripts\activate
pip install git+https://github.com/microsoft/TinyTroupe.git@main
```
Переименыйте файл .env.example в .env и добавьте в него свой ключ OpenAI API


## Примеры использования


**6. Создание TinyPerson**

Внутри директории проекта создайте файл `my_person.py` и добавьте следующий код: 

```python
import os
from dotenv import load_dotenv
# Если ключ хранится в файле .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from tinytroupe.agent import TinyPerson

# Create a TinyPerson instance
john = TinyPerson(name="John")

# Define some characteristics
john.define("age", 35)
john.define("occupation", "Software Engineer")
john.define("nationality", "American")
john.define("skills", [{"skill": "Coding in python"}])

# Interact with the agent
john.listen("Hello, John! How are you today?")
john.act()
john.pp_current_interactions()
```

Этот пример создает агента, задает его характеристики, инициирует взаимодействие и показывает историю взаимодействия.
