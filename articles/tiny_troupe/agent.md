## Создание интеллектуальных агентов с TinyTroupe: Пошаговое руководство

**Введение**

В сфере управляемых искусственным интеллектом симуляций возможность создавать правдоподобных и вовлекающих агентов имеет первостепенное значение. `TinyTroupe` — это Python-библиотека, разработанная именно для этого. В отличие от ИИ-помощников, ориентированных на повышение производительности, `TinyTroupe` ориентирован на моделирование человекоподобного поведения, включающего в себя причуды, эмоции и реалистичные когнитивные процессы. Эта статья проведет вас через основные концепции и код модуля `tinytroupe.agent`, демонстрируя, как создать свою собственную "TinyPerson" - смоделированную личность, готовую населять ваш виртуальный мир.

**Что такое TinyPerson?**

В основе `TinyTroupe` лежит класс `TinyPerson`. Представьте его как чертеж для смоделированной личности. Каждая `TinyPerson` обладает:

*   **Имя:** Уникальный идентификатор.
*   **Когнитивные состояния:** Внутренние переменные, представляющие внимание, эмоции, цели и другие ментальные аспекты, влияющие на поведение.
*   **Память:** Разделенная на `episodic_memory` (конкретные события) и `semantic_memory` (общие знания), отражая структуру человеческой памяти.
*   **Поведенческие абстракции:** Методы `listen()` и `act()` имеют решающее значение для взаимодействия, моделируя циклы стимул-реакция.
*   **Ментальные способности:** Дополнительные надстройки для расширения логики и возможностей обработки агента.

**Настройка вашей среды**

Прежде чем погружаться в код, убедитесь, что у вас установлена и настроена `TinyTroupe`. Обычно это включает в себя настройку вашего ключа OpenAI API (поскольку `TinyTroupe` использует LLM) и потенциальную настройку других параметров в файле `config.ini`. Также убедитесь, что вы установили зависимости, такие как `chevron` и `rich`. Библиотека полагается на `llama-index`, которая кэширует свои LLM локально, поэтому может быть удобно добавить файл `.gitignore` в проект, чтобы избежать коммита кэша. Библиотека уже инициализирует логгер, поэтому дополнительные действия не требуются, нужно просто импортировать его при необходимости (`import logging; logger = logging.getLogger("tinytroupe")`).

**Разбор основного кода: `tinytroupe/agent.py`**

Давайте рассмотрим ключевые разделы модуля `agent.py`, сосредоточив внимание на том, как создаются экземпляры `TinyPerson` и как они взаимодействуют.

**1. Импорт и конфигурация**

Модуль начинается с необходимых импортов, включая библиотеки для работы с JSON, манипулирования текстом и ведения журналов. Важно отметить, что он считывает параметры конфигурации из файла `config.ini`:

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

Эта конфигурация определяет многие поведения по умолчанию, включая модель OpenAI, используемую для встраивания (`text-embedding-3-small` по умолчанию), и максимальную длину отображаемого текста. Секция LlamaIndex предназначена для функциональности семантической памяти, которая может быть включена.

**2. Класс `TinyPerson`**

Этот класс является основной абстракцией. Давайте рассмотрим его структуру:

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
        # ... (Логика инициализации) ...

    def _post_init(self, **kwargs):
        # ... (Настройка значений по умолчанию и обработка десериализации) ...

    # ... (Другие методы для взаимодействия, памяти и конфигурации) ...
```

*   **`JsonSerializableRegistry`:** Этот базовый класс предоставляет функциональность для сохранения и загрузки спецификаций `TinyPerson` в и из JSON.
*   **Атрибуты класса:** `MAX_ACTIONS_BEFORE_DONE` ограничивает количество действий, которые может предпринять агент, предотвращая бесконечные циклы. `serializable_attributes` перечисляет атрибуты, сохраненные в JSON. `all_agents` отслеживает всех созданных агентов.
*   **`__init__`:** Конструктор принимает `name` (обязательно), `episodic_memory`, `semantic_memory` и `mental_faculties` в качестве входных данных. Он выполняет минимальную инициализацию.
*   **`_post_init`:** Этот специальный метод, отмеченный декоратором `@post_init`, вызывается *после* конструктора. Он устанавливает значения по умолчанию для различных внутренних атрибутов, включая:

    *   `current_messages`: Список для хранения истории разговоров.
    *   `environment`: Ссылка на среду, в которой находится агент (изначально `None`).
    *   `_actions_buffer`: Хранит действия, ожидающие обработки средой.
    *   `_accessible_agents`: Агенты, с которыми этот агент может взаимодействовать.
    *   `_configuration`: Словарь, содержащий ключевые характеристики человека, такие как возраст, профессия и текущее эмоциональное состояние.
    *   Конфигурация для работы с LLM.

* Десериализация: обратите внимание, что некоторые `kwargs` также будут присутствовать, связанные с сериализацией и десериализацией.
* Механизм переименования: существует метод `_rename` для обеспечения согласованности имен.

**3. Основные методы взаимодействия**

*   **`act(self, until_done=True, n=None, return_actions=False, max_content_length=default["max_content_display_length"])`:** Это основной метод, который управляет поведением агента. Он запрашивает у LLM создание действия на основе текущего когнитивного состояния и памяти агента.  Он также использует `_produce_message`, описанный ниже, для построения запроса и отправки его в LLM.

    *   Затем `action` добавляется в `_actions_buffer` для обработки средой.
*   **`listen(self, speech, source: AgentOrWorld = None, max_content_length=default["max_content_display_length"])`:** Этот метод имитирует получение агентом сообщения от другого агента или среды. `speech` (содержание сообщения) хранится в эпизодической памяти агента.
*   **`_observe(self, stimulus, max_content_length=default["max_content_display_length"])`:** Это метод более низкого уровня, используемый `listen` и другими методами "чувств" (например, `see`, `socialize`, `think`). Он принимает словарь `stimulus` в качестве входных данных и сохраняет его в эпизодической памяти агента.

**4. Управление памятью**

`TinyPerson` использует `episodic_memory` и `semantic_memory` (более подробно об этом ниже). Метод `reset_prompt()` является центральным:

```python
    def reset_prompt(self):
        # render the template with the current configuration
        self._init_system_message = self.generate_agent_prompt()

        # reset system message
        self.current_messages = [
            {"role": "system", "content": self._init_system_message}
        ]

        # sets up the actual interaction messages to use for prompting
        self.current_messages += self.episodic_memory.retrieve_recent()
```

*   Он восстанавливает системное сообщение агента (`_init_system_message`) с помощью метода `generate_agent_prompt()`, эффективно обновляя контекст LLM на основе текущего состояния агента.
*   Он извлекает последние сообщения из эпизодической памяти, чтобы предоставить контекст для LLM.

**5. Внутреннее состояние и конфигурация**

Метод `_update_cognitive_state()` позволяет вам программно изменять внутреннее состояние агента (цели, контекст, внимание, эмоции). Метод `define()` предоставляет способ установки или обновления параметров конфигурации:

```python
    @transactional
    def define(self, key, value, group=None):
        """
        Define a value to the TinyPerson's configuration.
        If group is None, the value is added to the top level of the configuration.
        Otherwise, the value is added to the specified group.
        """
        # dedent value if it is a string
        if isinstance(value, str):
            value = textwrap.dedent(value)

        if group is None:
            # logger.debug(f"[{self.name}] Defining {key}={value} in the person.")
            self._configuration[key] = value
        else:
            if key is not None:
                # logger.debug(f"[{self.name}] Adding definition to {group} += [ {key}={value} ] in the person.")
                self._configuration[group].append({key: value})
            else:
                # logger.debug(f"[{self.name}] Adding definition to {group} += [ {value} ] in the person.")
                self._configuration[group].append(value)

        # must reset prompt after adding to configuration
        self.reset_prompt()
```

**6. Классы памяти (эпизодическая и семантическая)**

Классы `EpisodicMemory` и `SemanticMemory` предоставляют агенту разные типы памяти:

*   **`EpisodicMemory`:** Хранит конкретные события или эпизоды. Он имеет `fixed_prefix_length` и `lookback_length` для управления тем, какая часть прошлого учитывается в текущем запросе.
*   **`SemanticMemory`:** Хранит общие знания и факты. Он использует LlamaIndex для индексации и извлечения релевантной информации из документов (локальные файлы и веб-страницы).

**7. Ментальные способности**

Агенты TinyTroupe предназначены для обработки информации и выполнения задач самостоятельно, поэтому они поставляются со специальными методами, называемыми "Ментальные способности". Это подключаемые классы, описывающие возможные действия, на которые способен агент. `RecallFaculty` позволяет агентам использовать семантическую память, а `FilesAndWebGroundingFaculty` позволяет загружать внешнюю информацию.

**8. Собираем все вместе: Создание TinyPerson**

Вот основной пример создания `TinyPerson`:

```python
from tinytroupe.agent import TinyPerson, EpisodicMemory

# Create a TinyPerson instance
john = TinyPerson(name="John")

# Define some characteristics
john.define("age", 35)
john.define("occupation", "Software Engineer")
john.define("nationality", "American")

john.related_to(other_agent=another_agent, description="His colleague", symmetric_description="John's colleague")

# add recall abilities
#from tinytroupe.agent import RecallFaculty
#john.add_mental_faculties([RecallFaculty()])

# Interact with the agent
john.listen("Hello, John! How are you today?")
john.act()
john.pp_current_interactions()
```

Этот код создает `TinyPerson` с именем "John", устанавливает его возраст и профессию, определяет отношения с другим агентом, предоставляет исходное сообщение, предлагает Джону действовать и отображает последние взаимодействия.

**Ключевые моменты и соображения**

*   **Промпт-инжиниринг имеет ключевое значение:** Поведение вашей `TinyPerson` во многом зависит от системного промпта, созданного `generate_agent_prompt()`, и от того, как вы структурируете взаимодействия.
*   **Конфигурация:** Поэкспериментируйте с различными настройками `temperature`, чтобы контролировать креативность агента. Настройте `max_tokens`, чтобы ограничить длину ответа.
*   **Управление памятью:** Обратите внимание на `fixed_prefix_length` и `lookback_length` в `EpisodicMemory`, чтобы сбалансировать контекст и использование токенов. Подумайте, как вы хотите организовать и заполнить `SemanticMemory`.
*   **Асинхронное выполнение:** Для более сложных симуляций рассмотрите возможность использования асинхронного программирования для одновременного выполнения действий агента.
*   **Модульные способности:** Список `_mental_faculties` — это мощный способ добавления специализированных возможностей вашим агентам.

**Дальнейшее изучение**

Модуль `tinytroupe.agent` предоставляет прочную основу для создания правдоподобных агентов. Чтобы построить более сложные симуляции, изучите:

*   **Среды:** Узнайте, как создавать экземпляры `TinyWorld`, чтобы предоставить структурированный контекст для взаимодействия агентов.
*   **Инструменты:** Изучите, как оснастить агентов специализированными инструментами, такими как календари или поисковые системы.
*   **Сериализация/Десериализация:** Освойте механизмы сохранения и загрузки JSON для сохранения состояния агента.

Понимая эти концепции и экспериментируя с кодом, вы сможете использовать возможности `TinyTroupe` для создания убедительных симуляций человеческого поведения.
