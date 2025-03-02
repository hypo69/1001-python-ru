# Создание интеллектуальных агентов с TinyTroupe: Пошаговое руководство

## Введение

**Что такое TinyTroupe?**

TinyTroupe — это экспериментальная Python-библиотека от Microsoft, предназначенная для моделирования людей с определёнными личностными характеристиками, интересами и целями. Эти искусственные агенты, называемые «TinyPerson», могут взаимодействовать между собой и с окружающей средой, имитируя реалистичное поведение.

**Что такое TinyPerson?**

В основе TinyTroupe лежит класс `TinyPerson`. Представьте его как чертеж для смоделированной личности. Каждая `TinyPerson` обладает:

*   **Имя:** Уникальный идентификатор.
*   **Когнитивные состояния:** Внутренние переменные, представляющие внимание, эмоции, цели и другие ментальные аспекты, влияющие на поведение.
*   **Память:** Разделенная на `episodic_memory` (конкретные события) и `semantic_memory` (общие знания), отражая структуру человеческой памяти.
*   **Поведенческие абстракции:** Методы `listen()` и `act()` имеют решающее значение для взаимодействия, моделируя циклы стимул-реакция.

## Установка
```bash
pip install git+https://github.com/microsoft/TinyTroupe.git@main
```


**Далее...**

**1. Imports и конфигурация**

```python
import os
import json
import textwrap
import datetime
import chevron
import logging
logger = logging.getLogger("tinytroupe")
import tinytroupe.utils as utils
from tinytroupe.utils import post_init
from tinytroupe.control import transactional
from rich import print
import copy
from tinytroupe.utils import JsonSerializableRegistry

from typing import Any, TypeVar, Union

Self = TypeVar("Self", bound="TinyPerson")
AgentOrWorld = Union[Self, "TinyWorld"]

config = utils.read_config_file()

default = {}
default["embedding_model"] = config["OpenAI"].get("EMBEDDING_MODEL", "text-embedding-3-small")
default["max_content_display_length"] = config["OpenAI"].getint("MAX_CONTENT_DISPLAY_LENGTH", 1024)
```

Этот блок кода импортирует необходимые библиотеки и считывает настройки конфигурации из файла `config.ini`. Ключевые настройки включают в себя: модель для встраивания (embedding_model), например `text-embedding-3-small`, и максимальную длину контента для отображения (`max_content_display_length`).

**2. Класс `TinyPerson`**

```python
@post_init
class TinyPerson(JsonSerializableRegistry):
    """A simulated person in the TinyTroupe universe."""

    MAX_ACTIONS_BEFORE_DONE = 15
    PP_TEXT_WIDTH = 100
    serializable_attributes = ["name", "episodic_memory", "semantic_memory", "_mental_faculties", "_configuration"]
    all_agents = {}
    communication_style:str="simplified"
    communication_display:bool=True

    def __init__(self, name:str=None, 
                 episodic_memory=None,
                 semantic_memory=None,
                 mental_faculties:list=None):
        # ... (Initialization logic) ...

    def _post_init(self, **kwargs):
        # ... (Настройка значений по умолчанию и обработка десериализации) ...

    # ... (Другие методы для взаимодействия, памяти и конфигурации) ...
```

`TinyPerson` - это основной класс для моделирования агентов. Он включает в себя:
*   `JsonSerializableRegistry`: Для загрузки и сохранения агентов в формате JSON.
*   `MAX_ACTIONS_BEFORE_DONE`: Ограничивает количество действий агента.
*   `serializable_attributes`: Список атрибутов для сериализации.
*   `__init__`: Конструктор, принимающий основные компоненты агента.
*   `_post_init`: Настройка значений по умолчанию, создание памяти, конфигурации и регистрация агента.

**3. Методы взаимодействия**

*   **`act()`**: Определяет поведение агента, запрашивая у LLM действие на основе памяти и когнитивного состояния.
*   **`listen()`**:  Моделирует получение сообщения от другого агента или среды, сохраняя информацию в памяти.
*   **`_observe()`**:  Записывает стимулы (события, ощущения) во внутреннюю память агента.

**4. Управление памятью**

`TinyPerson` использует `episodic_memory` и `semantic_memory`:
*   **`episodic_memory`**: Хранит конкретные события, организует их по времени и ограничивает количество используемых записей с помощью параметров `fixed_prefix_length` и `lookback_length`.
*   **`semantic_memory`**: Хранит общие знания, индексируя текстовые документы с помощью `llama_index`.

**5. Внутреннее состояние и конфигурация**

*   `_update_cognitive_state()`: Изменяет цели, внимание, эмоции и другие внутренние переменные.
*   `define()`: Устанавливает или обновляет параметры конфигурации агента.
*   `reset_prompt()`: Пересоздает системный промпт для LLM на основе текущей конфигурации и памяти агента.

**6. Создание TinyPerson**

```python
from tinytroupe.agent import TinyPerson

# Create a TinyPerson instance
john = TinyPerson(name="John")

# Define some characteristics
john.define("age", 35)
john.define("occupation", "Software Engineer")
john.define("nationality", "American")
john.define_several("skills", [{"skill": "Coding in python"}])

# Interact with the agent
john.listen("Hello, John! How are you today?")
john.act()
john.pp_current_interactions()
```

Этот пример создает агента, задает его характеристики, инициирует взаимодействие и показывает историю взаимодействия.

**Вывод**

`TinyPerson` - это основной строительный блок для создания сложных, управляемых LLM агентов.  Экспериментируйте с различными промптами, конфигурациями памяти и ментальными способностями, чтобы раскрыть весь потенциал моделирования человеческого поведения с помощью `TinyTroupe`.
