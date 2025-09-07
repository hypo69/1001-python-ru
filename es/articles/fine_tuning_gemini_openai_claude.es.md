## Hoja de trucos. Personalización de LLM: Prompts, ajuste fino de modelos, ejemplos de código.

En este artículo:

1.  Cómo se crea el "efecto memoria" en los LLM (breve resumen).
2.  Por qué y cuándo es necesario el ajuste fino (Fine-tuning) de un modelo.
3.  Cuándo el ajuste fino no es la mejor solución.
4.  Preparación de datos.
5.  Ejemplos de ajuste fino para **OpenAI (GPT)**, **Google (Gemini)** y **Anthropic (Claude)** (difiere).

### 1. Cómo los LLM "recuerdan" y "se adaptan": La ilusión del contexto

Antes de hablar del ajuste fino, es importante entender cómo los LLM logran crear una sensación de personalización.
Esto es importante para no apresurarse a un ajuste fino costoso si la tarea se puede resolver con métodos más simples:

*   A través de la **Ventana de Contexto (Memoria a Corto Plazo):** Dentro de un solo diálogo, usted envía al modelo no solo una nueva pregunta, sino también **toda o parte de la conversación anterior**. El modelo procesa todo este texto como un único "contexto". Es gracias a esto que "recuerda" las observaciones anteriores y continúa el pensamiento. La limitación aquí es la longitud de la ventana de contexto (número de tokens).
*   Componiendo **Instrucciones del Sistema (System Prompt):** Puede establecer el rol, el tono y las reglas de comportamiento del modelo al comienzo de cada diálogo. Por ejemplo: "Eres un experto en Python, responde concisamente."
*   Incluyendo varios ejemplos del comportamiento deseado en la solicitud **Few-Shot Learning:** (pares de entrada/salida) permite que el modelo "aprenda" este patrón directamente dentro de la solicitud actual.
*   **Gestión de estado del lado de la aplicación:** La forma más potente. La aplicación (que accede a la API) puede almacenar información sobre el usuario (preferencias, historial, datos de perfil) y agregarla dinámicamente al prompt antes de enviarla al modelo.


### 2.

El ajuste fino es el proceso de entrenar aún más un LLM base ya existente en su propio conjunto de datos específico. Esto permite que el modelo:

*   **Adapte el estilo y el tono:** El modelo hablará "su idioma", ya sea estrictamente científico, amigable de marketing o la jerga de una comunidad específica.
*   **Siga instrucciones y formatos específicos:** Si necesita respuestas en una estructura JSON estrictamente definida, o siempre con un conjunto específico de campos.
*   **Comprenda el lenguaje específico del dominio:** El entrenamiento con su documentación interna o textos de la industria ayudará al modelo a manejar mejor la terminología de su nicho.
*   **Mejore el rendimiento en tareas específicas:** Para ciertos tipos de consultas (por ejemplo, clasificación de sentimientos, generación de código en un marco específico), el ajuste fino puede proporcionar respuestas más precisas y relevantes que el modelo base.
*   **Reduzca la longitud del prompt:** Si el modelo ya "conoce" el comportamiento deseado a través del ajuste, no necesita recordárselo cada vez en el prompt, lo que ahorra tokens y reduce la latencia.


### 3.

El ajuste fino es una herramienta potente pero no universal. No debe usarla si:

*   **El modelo necesita acceso a nuevos conocimientos:** El ajuste fino cambia los pesos del modelo, pero no "carga" nuevos hechos en él en tiempo real. Si su tarea es responder preguntas basadas en una base de conocimientos en constante cambio (documentos de la empresa, últimas noticias), es mejor usar **Generación Aumentada por Recuperación (RAG)**. Aquí, el modelo base recibe el contexto de su base de datos *en el momento de la consulta*.
*   **Una tarea simple se resuelve con ingeniería de prompts:** Siempre comience con la ingeniería de prompts más efectiva. Si la tarea se puede resolver con instrucciones simples y ejemplos de pocas tomas, el ajuste fino es redundante y más costoso.
*   **No tiene suficientes datos de alta calidad:** Datos malos = modelo mal ajustado.


### 4. Preparación de datos.

La calidad y cantidad de sus datos son de vital importancia. El modelo aprende de sus ejemplos, por lo que deben ser precisos, diversos y consistentes.

*   **Formato:** La mayoría de las veces JSON Lines (`.jsonl`) o CSV (`.csv`).
*   **Estructura de datos:** Depende de la tarea.
    *   **Ajuste de Instrucciones (Instrucción-Respuesta):** Adecuado para tareas generalizadas como "pregunta-respuesta", parafraseo, resumen.
        ```json
        {"input_text": "Перефразируй предложение: 'Технология ИИ стремительно развивается.'", "output_text": "Искусственный интеллект демонстрирует стремительный прогресс."}
        {"input_text": "Назови столицу Франции.", "output_text": "Столица Франции — Париж."}
        ```
    *   **Ajuste de Chat (Chat):** Ideal para entrenar al modelo para mantener un diálogo en un rol o estilo específico.
        ```json
        {"messages": [{"author": "user", "content": "Привет! Что порекомендуешь на ужин?"}, {"author": "model", "content": "Добрый вечер! Сегодня отличный день для пасты Карбонара, или, если вы предпочитаете что-то легкое, салат Цезарь."}]}
        {"messages": [{"author": "user", "content": "Расскажи про новые фичи в Python 3.12."}, {"author": "model", "content": "В Python 3.12 появились f-строки с отступами, новый синтаксис для универсальных генериков и улучшенная обработка ошибок Unicode."}]}
        ```
*   **Cantidad:** Mínimo 100-200 ejemplos de alta calidad, pero cuantos más, mejor (miles para tareas serias).
*   **Calidad:** Precisión, estilo consistente, tono, formato en todo el conjunto de datos.


### 5. Modelos y Plataformas


#### 5.1. OpenAI

OpenAI proporciona una API bastante simple e intuitiva para el ajuste fino.

**Proceso:**

1.  Prepare los datos en formato JSONL, donde cada línea es un objeto con una matriz `messages` (como en la API de Chat Completions).
2.  Suba el archivo de datos a través de la API.
3.  Cree un trabajo de ajuste fino, especificando el archivo subido y el modelo base.
4.  Supervise el progreso.
5.  Use el nuevo modelo ajustado por su ID.

**Ejemplo de datos (archivo `training_data.jsonl`):**

```json
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I apologize for the inconvenience! Let's try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the on-screen instructions."}]}
```

**Ejemplo de código Python:**

Instale previamente: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Establezca su clave API de OpenAI. Se recomienda usar una variable de entorno.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Subir archivo de datos
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Archivo subido con éxito. ID del archivo: {file_id}")
except openai.APIStatusError as e:
    print(f"Error al subir el archivo: {e.status_code} - {e.response}")
    exit()

# 2. Crear trabajo de ajuste fino
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Puede especificar una versión específica, p. ej., "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Trabajo de ajuste fino creado. ID del trabajo: {job_id}")
    print("Supervise el estado del trabajo a través de la API o en OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Error al crear el trabajo: {e.status_code} - {e.response}")
    exit()

# Ejemplo de supervisión del estado y obtención del nombre del modelo (ejecutar después de la creación del trabajo):
# # job_id = "ftjob-..." # Reemplace con su ID de trabajo
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Estado actual del trabajo: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Nombre del modelo ajustado: {fine_tuned_model_name}")

# 3. Usar el modelo ajustado (después de que esté listo)
# # Reemplace con el nombre real de su modelo, obtenido después de un ajuste fino exitoso
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "Tengo un problema de inicio de sesión."}
# #             ]
# #         )
# #         print("\nRespuesta del modelo ajustado:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Error al usar el modelo: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **no proporciona una API pública para el ajuste fino de sus modelos Claude 3 (Opus, Sonnet, Haiku) de la misma manera que OpenAI o Google.**

Anthropic se centra en crear modelos base muy potentes que, según afirman, funcionan excelentemente con ingeniería de prompts avanzada y patrones RAG, minimizando la necesidad de ajuste fino en la mayoría de los casos.
Para grandes clientes corporativos o socios, puede haber programas para crear modelos "personalizados" o integraciones especializadas, pero esta no es una característica de ajuste fino disponible públicamente a través de la API.

Si está trabajando con Claude 3, su enfoque principal debe ser:

*   **Ingeniería de prompts de alta calidad:** Experimente con instrucciones del sistema, ejemplos de pocas tomas, formato claro de las solicitudes. Claude es conocido por su capacidad para seguir estrictamente las instrucciones, especialmente en las etiquetas XML.
*   **Sistemas RAG:** Utilice bases de conocimiento externas para proporcionar al modelo un contexto relevante.

#### 5.3. Google (Gemini)

Google está desarrollando activamente capacidades de ajuste fino a través de su plataforma **Google Cloud Vertex AI**.
Esta es una plataforma de ML completa que proporciona herramientas para la preparación de datos, la ejecución de trabajos de entrenamiento y la implementación de modelos.
El ajuste fino está disponible para la familia de modelos Gemini.

**Proceso:**

1.  Prepare los datos (JSONL o CSV) en formato `input_text`/`output_text` (para ajuste de instrucciones) o `messages` (para ajuste de chat).
2.  Suba los datos a Google Cloud Storage (GCS).
3.  Cree y ejecute un trabajo de ajuste fino a través de la Consola o SDK de Vertex AI.
4.  Implemente el modelo ajustado en un Endpoint.
5.  Use el modelo ajustado a través de este Endpoint.

**Ejemplo de datos (archivo `gemini_tuning_data.jsonl`):**

```json
{"input_text": "Summarize the main ideas of this book: 'The book tells the story of a hero's journey, who overcomes obstacles and finds himself.'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and achieving self-discovery."}
{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to replicate the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}
```

**Ejemplo de código Python (requiere `google-cloud-aiplatform`):**

Instale previamente: `pip install google-cloud-aiplatform` y `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Configuración ---
# REEMPLACE con sus valores:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Elija una región que admita Gemini y Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Nombre de su bucket de GCS (debe crearse previamente)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Fin de la configuración ---

# Inicializar Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Crear archivo de datos (si no existe)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Summarize the main ideas of this book: \'The book tells the story of a hero\'s journey, who overcomes obstacles and finds himself.\'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and achieving self-discovery."}\n')
    f.write('{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to replicate the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}\n')
print(f"Archivo de datos '{DATA_FILE_LOCAL_PATH}' creado.")


# 2. Subir datos a Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Sube un archivo al bucket de GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Archivo '{source_file_name}' subido a 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Error al subir el archivo a GCS. Asegúrese de que el bucket existe y tiene permisos: {e}")
    exit()

# 3. Crear y ejecutar trabajo de ajuste fino
print(f"\nIniciando ajuste fino del modelo '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` inicia el trabajo y devuelve el modelo ajustado al finalizar
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Modelo base Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Número de pasos de entrenamiento. El valor óptimo depende del tamaño de los datos.
        # batch_size=16, # Se puede especificar
        # learning_rate_multiplier=1.0 # Se puede especificar
    )
    print(f"Modelo '{TUNED_MODEL_DISPLAY_NAME}' ajustado con éxito. ID del modelo: {tuned_model.name}")
    print("El proceso de ajuste fino puede llevar un tiempo considerable.")
except Exception as e:
    print(f"Error de ajuste fino. Verifique los registros en la Consola de Vertex AI: {e}")
    exit()

# 4. Implementar el modelo ajustado (para usar)
print(f"\nImplementando el modelo ajustado '{TUNED_MODEL_DISPLAY_NAME}' en el endpoint...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Tipo de máquina para el endpoint. Elija el adecuado.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Modelo implementado en el endpoint: {endpoint.name}")
    print("La implementación también puede llevar varios minutos.")
except Exception as e:
    print(f"Error al implementar el modelo: {e}")
    exit()

# 5. Usar el modelo ajustado
print("\nProbando el modelo ajustado...")
prompt = "Háblame de tus capacidades después del entrenamiento."
instances = [{"prompt": prompt}] # Para ajuste de instrucciones. Si es ajuste de chat, entonces {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nRespuesta del modelo ajustado:")
    print(response.predictions[0])
except Exception as e:
    print(f"Error al usar el modelo ajustado: {e}")

# Después de finalizar, no olvide eliminar el endpoint y el modelo para evitar costos innecesarios:
# # endpoint.delete()
# # tuned_model.delete()
```

### 6. Recomendaciones generales

*   **Empiece poco a poco:** No intente entrenar el modelo con miles de ejemplos de inmediato. Comience con un conjunto de datos pequeño pero de alta calidad.
*   **Itere:** El ajuste fino es un proceso iterativo. Entrene, evalúe, ajuste los datos o los hiperparámetros, repita.
*   **Monitoreo:** Supervise cuidadosamente las métricas de entrenamiento (pérdidas) y use un conjunto de datos de validación para evitar el sobreajuste.
*   **Evaluación:** Siempre pruebe el modelo ajustado con datos que *nunca haya visto* durante el entrenamiento para evaluar su capacidad de generalización.
*   **Costo:** Recuerde que el ajuste fino y la implementación de endpoints son de pago. Tenga esto en cuenta en su presupuesto.
*   **Documentación:** Consulte siempre la documentación oficial del proveedor de LLM. Las API y las capacidades evolucionan constantemente.
