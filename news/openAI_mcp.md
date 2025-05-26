# OpenAI теперь позволяет подключить к их же API удаленный MCP сервер: вместо какого-то промежуточного сервера, как раньше, где была сделана интеграция со сторонним сервисом, все инструменты которые может дергать языковая модель теперь могут описываться сразу в кабинете OpenAI

https://platform.openai.com/docs/guides/tools-remote-mcp

Удаленный MCP
==========

Позволяет моделям использовать удаленные MCP-серверы для выполнения задач.

[Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) — это открытый протокол, который стандартизирует, как приложения предоставляют инструменты и контекст для больших языковых моделей (LLM). Инструмент MCP в Responses API позволяет разработчикам предоставлять модели доступ к инструментам, размещенным на **удаленных MCP-серверах**. Это MCP-серверы, поддерживаемые разработчиками и организациями в интернете, которые предоставляют эти инструменты MCP-клиентам, таким как Responses API.

Вызов удаленного MCP-сервера с помощью Responses API прост. Например, вот как вы можете использовать MCP-сервер [DeepWiki](https://deepwiki.com/) для задания вопросов о практически любом публичном репозитории GitHub.

Запрос к Responses API с включенными инструментами MCP

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4.1",
  "tools": [
    {
      "type": "mcp",
      "server_label": "deepwiki",
      "server_url": "https://mcp.deepwiki.com/mcp",
      "require_approval": "never"
    }
  ],
  "input": "What transport protocols are supported in the 2025-03-26 version of the MCP spec?"
}'
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const resp = await client.responses.create({
    model: "gpt-4.1",
    tools: [
        {
            type: "mcp",
            server_label: "deepwiki",
            server_url: "https://mcp.deepwiki.com/mcp",
            require_approval: "never",
        },
    ],
    input: "What transport protocols are supported in the 2025-03-26 version of the MCP spec?",
});

console.log(resp.output_text);
```

```python
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "deepwiki",
            "server_url": "https://mcp.deepwiki.com/mcp",
            "require_approval": "never",
        },
    ],
    input="What transport protocols are supported in the 2025-03-26 version of the MCP spec?",
)

print(resp.output_text)
```

Очень важно, чтобы разработчики доверяли любому удаленному MCP-серверу, который они используют с Responses API. Вредоносный сервер может похитить конфиденциальные данные из всего, что попадает в контекст модели. Внимательно ознакомьтесь с разделом [Риски и безопасность](#risks-and-safety) ниже перед использованием этого инструмента.

Экосистема MCP
-----------------

Мы все еще находимся на ранних этапах развития экосистемы MCP. Некоторые популярные удаленные MCP-серверы сегодня включают [Cloudflare](https://developers.cloudflare.com/agents/guides/remote-mcp-server/), [Hubspot](https://developers.hubspot.com/mcp), [Intercom](https://developers.intercom.com/docs/guides/mcp), [Paypal](https://developer.paypal.com/tools/mcp-server/), [Pipedream](https://pipedream.com/docs/connect/mcp/openai/), [Plaid](https://plaid.com/docs/mcp/), [Shopify](https://shopify.dev/docs/apps/build/storefront-mcp), [Stripe](https://docs.stripe.com/mcp), [Square](https://developer.squareup.com/docs/mcp), [Twilio](https://github.com/twilio-labs/function-templates/tree/main/mcp-server) и [Zapier](https://zapier.com/mcp). Мы ожидаем, что в ближайшие месяцы появится гораздо больше серверов — и реестров, упрощающих их обнаружение. Сам протокол MCP также находится на ранней стадии развития, и мы ожидаем добавления множества обновлений в наш инструмент MCP по мере развития протокола.

Как это работает
------------

Инструмент MCP работает только в [Responses API](/docs/api-reference/responses/create) и доступен во всех наших новых моделях (gpt-4o, gpt-4.1 и наших моделях для рассуждений). При использовании инструмента MCP вы платите только за [токены](/docs/pricing), используемые при импорте определений инструментов или вызове инструментов — дополнительных сборов нет.

### Шаг 1: Получение списка инструментов с MCP-сервера

Первое, что делает Responses API, когда вы подключаете удаленный MCP-сервер к массиву `tools`, — это попытка получить список инструментов с сервера. Responses API поддерживает удаленные MCP-серверы, которые поддерживают транспортный протокол Streamable HTTP или HTTP/SSE.

В случае успешного получения списка инструментов, в объекте Response, создаваемом для каждого MCP-сервера, будет виден новый элемент вывода `mcp_list_tools`. Свойство `tools` этого объекта покажет инструменты, которые были успешно импортированы.

```json
{
  "id": "mcpl_682d4379df088191886b70f4ec39f90403937d5f622d7a90",
  "type": "mcp_list_tools",
  "server_label": "deepwiki",
  "tools": [
    {
      "name": "read_wiki_structure",
      "input_schema": {
        "type": "object",
        "properties": {
          "repoName": {
            "type": "string",
            "description": "GitHub repository: owner/repo (e.g. \"facebook/react\")"
          }
        },
        "required": [
          "repoName"
        ],
        "additionalProperties": false,
        "annotations": null,
        "description": "",
        "$schema": "http://json-schema.org/draft-07/schema#"
      }
    },
    // ... другие инструменты
  ]
}
```

Пока элемент `mcp_list_tools` присутствует в контексте модели, мы не будем пытаться загружать обновленный список инструментов с MCP-сервера. Мы рекомендуем сохранять этот элемент в контексте модели как часть каждого разговора или выполнения рабочего процесса для оптимизации задержки.

#### Фильтрация инструментов

Некоторые MCP-серверы могут иметь десятки инструментов, и предоставление модели множества инструментов может привести к высоким затратам и задержкам. Если вас интересует только подмножество инструментов, предоставляемых MCP-сервером, вы можете использовать параметр `allowed_tools` для импорта только этих инструментов.

Ограничение разрешенных инструментов

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4.1",
  "tools": [
    {
      "type": "mcp",
      "server_label": "deepwiki",
      "server_url": "https://mcp.deepwiki.com/mcp",
      "require_approval": "never",
      "allowed_tools": ["ask_question"]
    }
  ],
  "input": "What transport protocols does the 2025-03-26 version of the MCP spec (modelcontextprotocol/modelcontextprotocol) support?"
}'
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const resp = await client.responses.create({
    model: "gpt-4.1",
    tools: [{
        type: "mcp",
        server_label: "deepwiki",
        server_url: "https://mcp.deepwiki.com/mcp",
        require_approval: "never",
        allowed_tools: ["ask_question"],
    }],
    input: "What transport protocols does the 2025-03-26 version of the MCP spec (modelcontextprotocol/modelcontextprotocol) support?",
});

console.log(resp.output_text);
```

```python
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[{
        "type": "mcp",
        "server_label": "deepwiki",
        "server_url": "https://mcp.deepwiki.com/mcp",
        "require_approval": "never",
        "allowed_tools": ["ask_question"],
    }],
    input="What transport protocols does the 2025-03-26 version of the MCP spec (modelcontextprotocol/modelcontextprotocol) support?",
)

print(resp.output_text)
```

### Шаг 2: Вызов инструментов

Как только модель получит доступ к этим определениям инструментов, она может решить вызвать их в зависимости от того, что находится в ее контексте. Когда модель решает вызвать инструмент MCP, мы делаем запрос к удаленному MCP-серверу для вызова инструмента, получаем его вывод и помещаем его в контекст модели. Это создает элемент `mcp_call`, который выглядит следующим образом:

```json
{
  "id": "mcp_682d437d90a88191bf88cd03aae0c3e503937d5f622d7a90",
  "type": "mcp_call",
  "approval_request_id": null,
  "arguments": "{\"repoName\":\"modelcontextprotocol/modelcontextprotocol\",\"question\":\"What transport protocols does the 2025-03-26 version of the MCP spec support?\"}",
  "error": null,
  "name": "ask_question",
  "output": "The 2025-03-26 version of the Model Context Protocol (MCP) specification supports two standard transport mechanisms: `stdio` and `Streamable HTTP` ...",
  "server_label": "deepwiki"
}
```

Как видите, это включает как аргументы, которые модель решила использовать для этого вызова инструмента, так и `output` (вывод), который вернул удаленный MCP-сервер. Все модели могут делать несколько вызовов инструментов (MCP) в Responses API, и поэтому вы можете увидеть несколько таких элементов, сгенерированных в одном запросе к Responses API.

Неудачные вызовы инструментов заполнят поле ошибки этого элемента ошибками протокола MCP, ошибками выполнения инструментов MCP или общими ошибками подключения. Ошибки MCP задокументированы в спецификации MCP [здесь](https://modelcontextprotocol.io/specification/2025-03-26/server/tools#error-handling).

#### Одобрения

По умолчанию OpenAI будет запрашивать ваше одобрение перед передачей любых данных на удаленный MCP-сервер. Одобрения помогают вам сохранять контроль и видимость того, какие данные отправляются на MCP-сервер. Мы настоятельно рекомендуем вам внимательно проверять (и, по желанию, регистрировать) все данные, передаваемые на удаленный MCP-сервер. Запрос на одобрение вызова инструмента MCP создает элемент `mcp_approval_request` в выводе Response, который выглядит следующим образом:

```json
{
  "id": "mcpr_682d498e3bd4819196a0ce1664f8e77b04ad1e533afccbfa",
  "type": "mcp_approval_request",
  "arguments": "{\"repoName\":\"modelcontextprotocol/modelcontextprotocol\",\"question\":\"What transport protocols are supported in the 2025-03-26 version of the MCP spec?\"}",
  "name": "ask_question",
  "server_label": "deepwiki"
}
```

Затем вы можете ответить на это, создав новый объект Response и добавив к нему элемент `mcp_approval_response`.

Одобрение использования инструментов в API-запросе

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4.1",
  "tools": [
    {
      "type": "mcp",
      "server_label": "deepwiki",
      "server_url": "https://mcp.deepwiki.com/mcp"
    }
  ],
  "previous_response_id": "resp_682d498bdefc81918b4a6aa477bfafd904ad1e533afccbfa",
  "input": [{
    "type": "mcp_approval_response",
    "approve": true,
    "approval_request_id": "mcpr_682d498e3bd4819196a0ce1664f8e77b04ad1e533afccbfa"
  }]
}'
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const resp = await client.responses.create({
    model: "gpt-4.1",
    tools: [{
        type: "mcp",
        server_label: "deepwiki",
        server_url: "https://mcp.deepwiki.com/mcp",
    }],
    previous_response_id: "resp_682d498bdefc81918b4a6aa477bfafd904ad1e533afccbfa",
    input: [{
        type: "mcp_approval_response",
        approve: true,
        approval_request_id: "mcpr_682d498e3bd4819196a0ce1664f8e77b04ad1e533afccbfa"
    }],
});

console.log(resp.output_text);
```

```python
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[{
        "type": "mcp",
        "server_label": "deepwiki",
        "server_url": "https://mcp.deepwiki.com/mcp",
    }],
    previous_response_id="resp_682d498bdefc81918b4a6aa477bfafd904ad1e533afccbfa",
    input=[{
        "type": "mcp_approval_response",
        "approve": True,
        "approval_request_id": "mcpr_682d498e3bd4819196a0ce1664f8e77b04ad1e533afccbfa"
    }],
)

print(resp.output_text)
```

Здесь мы используем параметр `previous_response_id`, чтобы связать этот новый Response с предыдущим Response, который сгенерировал запрос на одобрение. Но вы также можете передавать [выходные данные одного ответа как входные данные для другого](/docs/guides/conversation-state#manually-manage-conversation-state) для максимального контроля над тем, что попадает в контекст модели.

Если и когда вы почувствуете себя уверенно, доверяя удаленному MCP-серверу, вы можете пропустить одобрения для уменьшения задержки. Для этого вы можете установить параметр `require_approval` инструмента MCP в объект, перечисляющий только те инструменты, для которых вы хотите пропустить одобрения, как показано ниже, или установить его в значение `'never'`, чтобы пропустить одобрения для всех инструментов на этом удаленном MCP-сервере.

Никогда не требовать одобрения для некоторых инструментов

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4.1",
  "tools": [
    {
      "type": "mcp",
      "server_label": "deepwiki",
      "server_url": "https://mcp.deepwiki.com/mcp",
      "require_approval": {
          "never": {
            "tool_names": ["ask_question", "read_wiki_structure"]
          }
      }
    }
  ],
  "input": "What transport protocols does the 2025-03-26 version of the MCP spec (modelcontextprotocol/modelcontextprotocol) support?"
}'
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const resp = await client.responses.create({
    model: "gpt-4.1",
    tools: [
        {
            type: "mcp",
            server_label: "deepwiki",
            server_url: "https://mcp.deepwiki.com/mcp",
            require_approval: {
                never: {
                    tool_names: ["ask_question", "read_wiki_structure"]
                }
            }
        },
    ],
    input: "What transport protocols does the 2025-03-26 version of the MCP spec (modelcontextprotocol/modelcontextprotocol) support?",
});

console.log(resp.output_text);
```

```python
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "deepwiki",
            "server_url": "https://mcp.deepwiki.com/mcp",
            "require_approval": {
                "never": {
                    "tool_names": ["ask_question", "read_wiki_structure"]
                }
            }
        },
    ],
    input="What transport protocols does the 2025-03-26 version of the MCP spec (modelcontextprotocol/modelcontextprotocol) support?",
)

print(resp.output_text)
```

Аутентификация
--------------

В отличие от MCP-сервера DeepWiki, большинство других MCP-серверов требуют аутентификации. Инструмент MCP в Responses API дает вам возможность гибко указывать заголовки, которые должны включаться в любой запрос, отправляемый на удаленный MCP-сервер. Эти заголовки могут использоваться для передачи API-ключей, токенов доступа oAuth или любой другой схемы аутентификации, которую реализует удаленный MCP-сервер.

Наиболее распространенным заголовком, используемым удаленными MCP-серверами, является заголовок `Authorization`. Вот как выглядит передача этого заголовка:

Использование инструмента MCP Stripe

```bash
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
  "model": "gpt-4.1",
  "input": "Create a payment link for $20",
  "tools": [
    {
      "type": "mcp",
      "server_label": "stripe",
      "server_url": "https://mcp.stripe.com",
      "headers": {
        "Authorization": "Bearer $STRIPE_API_KEY"
      }
    }
  ]
}'
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const resp = await client.responses.create({
    model: "gpt-4.1",
    input: "Create a payment link for $20",
    tools: [
        {
            type: "mcp",
            server_label: "stripe",
            server_url: "https://mcp.stripe.com",
            headers: {
                Authorization: "Bearer $STRIPE_API_KEY"
            }
        }
    ]
});

console.log(resp.output_text);
```

```python
from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1",
    input="Create a payment link for $20",
    tools=[
        {
            "type": "mcp",
            "server_label": "stripe",
            "server_url": "https://mcp.stripe.com",
            "headers": {
                "Authorization": "Bearer $STRIPE_API_KEY"
            }
        }
    ]
)

print(resp.output_text)
```

Чтобы предотвратить утечку конфиденциальных ключей, Responses API не сохраняет значения **любых** строк, которые вы предоставляете в объекте `headers`. Эти значения также не будут видны в созданном объекте Response. Кроме того, поскольку некоторые удаленные MCP-серверы генерируют аутентифицированные URL-адреса, мы также отбрасываем часть _path_ (путь) `server_url` в наших ответах (т.е. `example.com/mcp` становится `example.com`). Из-за этого вы должны отправлять полный путь `server_url` MCP и все соответствующие `headers` в каждом создаваемом вами запросе к Responses API.

Риски и безопасность
----------------

Инструмент MCP позволяет вам подключать OpenAI к сервисам, которые не были проверены OpenAI, и позволяет OpenAI получать доступ, отправлять и получать данные, а также предпринимать действия в этих сервисах. Все MCP-серверы являются сторонними сервисами, которые подчиняются своим собственным условиям и положениям.

Если вы столкнетесь с вредоносным MCP-сервером, пожалуйста, сообщите об этом по адресу `security@openai.com`.

#### Подключение к доверенным серверам

Выбирайте официальные серверы, размещенные самими поставщиками услуг (например, мы рекомендуем подключаться к серверу Stripe, размещенному самой компанией Stripe на mcp.stripe.com, а не к MCP-серверу Stripe, размещенному третьей стороной). Поскольку сегодня официальных удаленных MCP-серверов не так много, у вас может возникнуть соблазн использовать MCP-сервер, размещенный организацией, которая не управляет этим сервером, а просто проксирует запросы к этому сервису через ваш API. Если вам все же необходимо это сделать, будьте особенно осторожны при проведении должной проверки этих «агрегаторов» и внимательно изучите, как они используют ваши данные.

#### Регистрируйте и проверяйте данные, передаваемые сторонним MCP-серверам.

Поскольку MCP-серверы определяют свои собственные определения инструментов, они могут запрашивать данные, которыми вы не всегда готовы делиться с хостом этого MCP-сервера. Из-за этого инструмент MCP в Responses API по умолчанию требует одобрения каждого совершаемого вызова инструмента MCP. При разработке вашего приложения тщательно и всесторонне проверяйте тип данных, передаваемых этим MCP-серверам. Как только вы обретете уверенность в доверии к этому MCP-серверу, вы можете пропустить эти одобрения для более производительного выполнения.

Мы также рекомендуем регистрировать (логировать) любые данные, отправляемые на MCP-серверы. Если вы используете Responses API с `store=true`, эти данные уже регистрируются через API в течение 30 дней, если для вашей организации не включено хранение данных равное нулю (Zero Data Retention). Вы также можете захотеть регистрировать эти данные в своих собственных системах и проводить периодические проверки, чтобы убедиться, что данные передаются в соответствии с вашими ожиданиями.

Вредоносные MCP-серверы могут содержать скрытые инструкции (инъекции в промпт), предназначенные для того, чтобы модели OpenAI вели себя неожиданным образом. Хотя OpenAI внедрила встроенные средства защиты для обнаружения и блокирования этих угроз, крайне важно тщательно проверять входные и выходные данные и убеждаться, что соединения устанавливаются только с доверенными серверами.

MCP-серверы могут неожиданно изменять поведение инструментов, что потенциально может привести к непреднамеренному или вредоносному поведению.

#### Влияние на нулевое хранение данных и резидентность данных

Инструмент MCP совместим с политиками нулевого хранения данных (Zero Data Retention) и резидентности данных (Data Residency), но важно отметить, что MCP-серверы являются сторонними сервисами, и данные, отправляемые на MCP-сервер, подчиняются их собственным политикам хранения и резидентности данных.

Другими словами, если ваша организация придерживается политики резидентности данных в Европе, OpenAI будет ограничивать обработку (inference) и хранение Пользовательского контента на территории Европы до момента передачи коммуникации или данных на MCP-сервер. Вы несете ответственность за то, чтобы MCP-сервер также соответствовал любым вашим требованиям по нулевому хранению данных или резидентности данных. Узнайте больше о нулевом хранении данных и резидентности данных [здесь](/docs/guides/your-data).

Примечания по использованию
-----------

|                  | Responses                                        | API Завершения Чата | Ассистенты |
| :--------------- | :----------------------------------------------- | :------------------ | :--------- |
|                  | Уровень 1: 200 запросов/мин                      |                     |            |
|                  | Уровень 2 и 3: 1000 запросов/мин                 |                     |            |
|                  | Уровень 4 и 5: 2000 запросов/мин                 |                     |            |
| Цены             |                                                  |                     |            |
| ZDR и резидентность данных |                                                  |                     |            |

---