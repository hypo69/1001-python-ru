## Шпаргалка. Персоналізація LLM: промпти, тонке налаштування моделей, приклади коду.

У цій статті:

1.  Як створюється "ефект пам'яті" в LLM (короткий огляд).
2.  Навіщо і коли потрібне тонке налаштування (Fine-tuning) моделі.
3.  Коли тонке налаштування – не найкраще рішення.
4.  Підготовка даних.
5.  Приклади тонкого налаштування для **OpenAI (GPT)**, **Google (Gemini)** та **Anthropic (Claude)** (відрізняється).

### 1. Як LLM "пам'ятає" та "підлаштовується": Ілюзія контексту

Перш ніж говорити про тонке налаштування, важливо зрозуміти, як LLM взагалі вдається створювати відчуття персоналізації.
Це важливо, щоб не кидатися в дороге тонке налаштування, якщо завдання вирішується простішими способами:

*   Через **Контекстне вікно (Short-Term Memory):** У рамках одного діалогу ви надсилаєте моделі не лише нове запитання, а й **всю або частину попереднього листування**. Модель обробляє весь цей текст як єдиний "контекст". Саме завдяки цьому вона "пам'ятає" попередні репліки та продовжує думку. Обмеження тут — довжина контекстного вікна (кількість токенів).
*   Складання **Системних інструкцій (System Prompt):** Ви можете задати моделі роль, тон, правила поведінки на початку кожного діалогу. Наприклад: "Ти – експерт з Python, відповідай коротко".
*   Включення в запит кількох прикладів бажаної поведінки **Few-Shot Learning:** (пари вхід/вихід) дозволяє моделі "навчитися" цьому патерну прямо в рамках поточного запиту.
*   **Керування станом на стороні програми:** Найпотужніший спосіб. Програма (яка звертається до API) може зберігати інформацію про користувача (переваги, історію, дані профілю) та динамічно додавати її в промпт перед надсиланням моделі.

### 2.

Тонке налаштування – це процес донавчання вже готової базової LLM на вашому власному, специфічному наборі даних. Це дозволяє моделі:

*   **Адаптувати стиль та тон:** Модель буде говорити "вашою мовою" – будь то строгий науковий, доброзичливий маркетинговий або сленг певного співтовариства.
*   **Дотримуватися специфічних інструкцій та форматів:** Якщо вам потрібні відповіді в строго визначеній JSON-структурі, або завжди з певним набором полів.
*   **Розуміти домен-специфічну мову:** Навчання на вашій внутрішній документації або галузевих текстах допоможе моделі краще справлятися з термінологією вашої ніші.
*   **Покращити продуктивність на вузьких завданнях:** Для певних типів запитів (наприклад, класифікація відгуків, генерація коду в специфічному фреймворку) тонке налаштування може дати більш точні та релевантні відповіді, ніж базова модель.
*   **Скоротити довжину промптів:** Якщо модель вже "знає" бажану поведінку завдяки налаштуванню, вам не потрібно щоразу нагадувати їй про це в промпті, що економить токени та знижує затримку.

### 3.

Тонке налаштування – потужний, але не універсальний інструмент. Не варто використовувати його, якщо:

*   **Модель повинна отримувати доступ до нових знань:** Тонке налаштування змінює ваги моделі, але не "завантажує" в неї нові факти в реальному часі. Якщо ваше завдання – відповідати на запитання за постійно змінною базою знань (документи компанії, останні новини), краще використовувати **Retrieval Augmented Generation (RAG)**. Тут базова модель отримує контекст з вашої бази даних *під час виконання запиту*.
*   **Просте завдання вирішується промпт-інжинірингом:** Завжди починайте з максимально ефективного промпт-інжинірингу. Якщо завдання вирішується простими інструкціями та few-shot прикладами, тонке налаштування надмірне та дорожче.
*   **У вас немає достатньої кількості високоякісних даних:** Погані дані = погано налаштована модель.

### 4. Підготовка даних.

Якість та кількість ваших даних є критично важливими. Модель навчається на ваших прикладах, тому вони повинні бути точними, різноманітними та послідовними.

*   **Формат:** Найчастіше JSON Lines (<code>.jsonl</code>) або CSV (<code>.csv</code>).
*   **Структура даних:** Залежить від завдання.
    *   **Instruction Tuning (Інструкція-Відповідь):** Підходить для узагальнених завдань типу "питання-відповідь", перефразування, узагальнення.
        ```json
        {"input_text": "Перефразуй речення: 'Технологія ШІ стрімко розвивається.'", "output_text": "Штучний інтелект демонструє стрімкий прогрес."}
        {"input_text": "Назви столицю Франції.", "output_text": "Столиця Франції — Париж."}
        ```
    *   **Chat Tuning (Чат):** Ідеально для навчання моделі веденню діалогу в певній ролі або стилі.
        ```json
        {"messages": [{"author": "user", "content": "Привіт! Що порекомендуєш на вечерю?"}, {"author": "model", "content": "Добрий вечір! Сьогодні чудовий день для пасти Карбонара, або, якщо ви віддаєте перевагу чомусь легкому, салат Цезар."}]}
        {"messages": [{"author": "user", "content": "Розкажи про нові фічі в Python 3.12."}, {"author": "model", "content": "У Python 3.12 з'явилися f-рядки з відступами, новий синтаксис для універсальних генериків та покращена обробка помилок Unicode."}]}
        ```
*   **Кількість:** Мінімум 100-200 якісних прикладів, але чим більше, тим краще (тисячі для серйозних завдань).
*   **Якість:** Точність, послідовність стилю, тону, формату в усьому наборі даних.

### 5. Моделі та платформи

#### 5.1. OpenAI

OpenAI надає досить простий та інтуїтивно зрозумілий API для тонкого налаштування.

**Процес:**

1.  Підготовка даних у форматі JSONL, де кожен рядок — це об'єкт з масивом <code>messages</code> (як у Chat Completions API).
2.  Завантаження файлу даних через API.
3.  Створення завдання на тонке налаштування, вказавши завантажений файл та базову модель.
4.  Відстеження прогресу.
5.  Використання нової, налаштованої моделі за її ID.

**Приклад даних (файл <code>training_data.jsonl</code>):**

```json
{"messages": [{"role": "system", "content": "Ти - дружелюбний асистент з підтримки клієнтів IT-компанії."}, {"role": "user", "content": "Мій інтернет не працює."}, {"role": "assistant", "content": "Ох, вибачте за незручності! Давайте спробуємо розібратися. Яким чином ви підключені до інтернету – по Wi-Fi чи через кабель?"}]}
{"messages": [{"role": "system", "content": "Ти - дружелюбний асистент з підтримки клієнтів IT-компанії."}, {"role": "user", "content": "Як я можу скинути пароль?"}, {"role": "assistant", "content": "Звісно! Щоб скинути пароль, перейдіть, будь ласка, на сторінку входу та натисніть 'Забули пароль?' під полем для введення. Далі дотримуйтесь інструкцій на екрані."}]
```

**Приклад Python коду:**

Попередньо встановіть: <code>pip install openai</code>

```python
import openai
from openai import OpenAI
import os

# Встановіть ваш API-ключ OpenAI. Рекомендується використовувати змінну середовища.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Завантаження файлу даних
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Файл успішно завантажено. ID файлу: {file_id}")
except openai.APIStatusError as e:
    print(f"Помилка завантаження файлу: {e.status_code} - {e.response}")
    exit()

# 2. Створення завдання на тонке налаштування
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Можна вказати конкретну версію, наприклад, "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Завдання на тонке налаштування створено. ID завдання: {job_id}")
    print("Відстежуйте статус завдання через API або в OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Помилка створення завдання: {e.status_code} - {e.response}")
    exit()

# Приклад відстеження статусу та отримання імені моделі (виконувати після створення завдання):
# # job_id = "ftjob-..." # Замініть на ID вашого завдання
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Поточний статус завдання: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Ім'я налаштованої моделі: {fine_tuned_model_name}")

# 3. Використання налаштованої моделі (після її готовності)
# # Замініть на реальне ім'я вашої моделі, отримане після успішного тонкого налаштування
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "У мене проблема з логіном."}
# #             ]
# #         )
# #         print("\nВідповідь налаштованої моделі:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Помилка при використанні моделі: {e.status_code} - {e.response}")
```</pre>
<h4>5.2. Anthropic</h4>
<p>Anthropic <strong>не надає публічного API для тонкого налаштування своїх моделей Claude 3 (Opus, Sonnet, Haiku) у тому ж сенсі, як це робить OpenAI або Google.</strong></p>
<p>Anthropic зосереджений на створенні дуже потужних базових моделей, які, за їхніми твердженнями, чудово працюють з просунутим промпт-інжинірингом та RAG-патернами, мінімізуючи необхідність у тонкому налаштуванні для більшості випадків.
Для великих корпоративних клієнтів або партнерів можуть існувати програми зі створення "кастомних" моделей або спеціалізованих інтеграцій, але це не є загальнодоступною функцією тонкого налаштування через API.</p>
<p>If you are working with Claude 3, your primary focus should be on:</p>
<ul>
<li><strong>High-quality prompt engineering:</strong> Experiment with system instructions, few-shot examples, clear request formatting. Claude is known for its ability to strictly follow instructions, especially in XML tags.</li>
<li><strong>RAG systems:</strong> Use external knowledge bases to provide the model with relevant context.</li>
</ul>
<h4>5.3. Google (Gemini)</h4>
<p>Google активно розвиває можливості тонкого налаштування через свою платформу <strong>Google Cloud Vertex AI</strong>.
This is a full-fledged ML platform that provides tools for data preparation, running training jobs, and deploying models.
Fine-tuning is available for the Gemini family of models.</p>
<p><strong>Process:</strong></p>
<ol>
<li>Prepare data (JSONL or CSV) in <code>input_text</code>/<code>output_text</code> format (for instruction tuning) or <code>messages</code> (for chat tuning).</li>
<li>Upload data to Google Cloud Storage (GCS).</li>
<li>Create and run a fine-tuning job via the Vertex AI Console or SDK.</li>
<li>Deploy the fine-tuned model to an Endpoint.</li>
<li>Use the fine-tuned model via this Endpoint.</li>
</ol>
<p><strong>Example data (file <code>gemini_tuning_data.jsonl</code>):</strong></p>
<pre class="line-numbers"><code class="language-json">{"input_text": "Узагальни основні ідеї цієї книги: 'Книга розповідає про подорож героя, який долає перешкоди та знаходить себе.'", "output_text": "Головний герой книги вирушає в трансформаційну подорож, стикаючись з труднощами та здобуваючи самопізнання."}
{"input_text": "Поясни принцип роботи термоядерного реактора простими словами.", "output_text": "Термоядерний реактор намагається відтворити процес, що відбувається на Сонці: злиття легких атомних ядер при дуже високих температурах, вивільняючи величезну кількість енергії."}
</code></pre>
<p><strong>Example Python code (потребує <code>google-cloud-aiplatform</code>):</strong></p>
<p>Попередньо встановіть: <code>pip install google-cloud-aiplatform</code> та <code>pip install google-cloud-storage</code></p>
<pre class="line-numbers"><code class="language-python">import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Налаштування ---
# ЗАМІНІТЬ на свої значення:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Виберіть регіон, що підтримує Gemini та Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Ім'я вашого бакету GCS (має бути створений заздалегідь)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Кінець налаштувань ---

# Ініціалізація Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Створення файлу з даними (якщо його немає)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Узагальни основні ідеї цієї книги: \'Книга розповідає про подорож героя, який долає перешкоди та знаходить себе.\'", "output_text": "Головний герой книги вирушає в трансформаційну подорож, стикаючись з труднощами та здобуваючи самопізнання."}\n')
    f.write('{"input_text": "Поясни принцип роботи термоядерного реактора простими словами.", "output_text": "Термоядерний реактор намагається відтворити процес, що відбувається на Сонці: злиття легких атомних ядер при дуже високих температурах, вивільняючи величезну кількість енергії."}\n')
print(f"Файл даних '{DATA_FILE_LOCAL_PATH}' створено.")


# 2. Завантаження даних у Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Завантажує файл у бакет GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Файл '{source_file_name}' завантажено в 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Помилка завантаження файлу в GCS. Переконайтеся, що бакет існує і у вас є права: {e}")
    exit()

# 3. Створення та запуск завдання на тонке налаштування
print(f"\nЗапуск тонкого налаштування моделі '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` запускає завдання та повертає налаштовану модель після завершення
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Базова модель Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Кількість кроків навчання. Оптимальне значення залежить від розміру даних.
        # batch_size=16, # Можна вказати
        # learning_rate_multiplier=1.0 # Можна вказати
    )
    print(f"Модель '{TUNED_MODEL_DISPLAY_NAME}' успішно налаштована. ID моделі: {tuned_model.name}")
    print("Процес тонкого налаштування може зайняти значний час.")
except Exception as e:
    print(f"Помилка тонкого налаштування. Перевірте логи в Vertex AI Console: {e}")
    exit()

# 4. Розгортання налаштованої моделі (для використання)
print(f"\nРозгортання налаштованої моделі '{TUNED_MODEL_DISPLAY_NAME}' на кінцеву точку...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Тип машини для кінцевої точки. Виберіть відповідний.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Модель розгорнута на кінцеву точку: {endpoint.name}")
    print("Розгортання також може зайняти кілька хвилин.")
except Exception as e:
    print(f"Помилка розгортання моделі: {e}")
    exit()

# 5. Використання налаштованої моделі
print("\nТестування налаштованої моделі...")
prompt = "Розкажи мені про свої можливості після навчання."
instances = [{"prompt": prompt}] # Для Instruction Tuning. Якщо Chat Tuning, то {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nВідповідь налаштованої моделі:")
    print(response.predictions[0])
except Exception as e:
    print(f"Помилка при використанні налаштованої моделі: {e}")

# Після завершення роботи, не забудьте видалити кінцеву точку та модель, щоб уникнути зайвих витрат:
# endpoint.delete()
# tuned_model.delete()
</code></pre>
<h3>6. Загальні рекомендації</h3>
<ul>
<li><strong>Почніть з малого:</strong> Не намагайтеся відразу навчити модель на тисячах прикладів. Почніть з невеликого, але якісного набору даних.</li>
<li><strong>Ітеруйте:</strong> Тонке налаштування — це ітераційний процес. Навчайте, оцінюйте, коригуйте дані або гіперпараметри, повторюйте.</li>
<li><strong>Моніторинг:</strong> Уважно відстежуйте метрики навчання (втрати) та використовуйте набір валідаційних даних, щоб уникнути перенавчання.</li>
<li><strong>Оцінка:</strong> Завжди тестуйте налаштовану модель на даних, які вона *ніколи не бачила* під час навчання, щоб оцінити її узагальнюючу здатність.</li>
<li><strong>Вартість:</strong> Пам'ятайте, що тонке налаштування та розгортання кінцевих точок платні. Враховуйте це в бюджеті.</li>
<li><strong>Документація:</strong> Завжди звіряйтеся з офіційною документацією постачальника LLM. API та можливості постійно розвиваються.</li>
</ul>