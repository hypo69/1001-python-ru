## Chuleta. Personalización de LLMs: Prompts, ajuste fino de modelos, ejemplos de código.


En este artículo:

1. Cómo se crea el "efecto memoria" en los LLMs (una breve descripción).
2. Por qué y cuándo es necesario el ajuste fino (Fine-tuning) del modelo.
3. Cuándo el ajuste fino no es la mejor solución.
4. Preparación de datos.
5. Ejemplos de ajuste fino para **OpenAI (GPT)**, **Google (Gemini)** y **Anthropic (Claude)** (difiere).

### 1. Cómo los LLMs "recuerdan" y "se adaptan": La ilusión del contexto

Antes de hablar de ajuste fino, es importante entender cómo los LLMs logran crear una sensación de personalización en primer lugar.
Esto es importante para no precipitarse en un costoso ajuste fino si la tarea se puede resolver de maneras más sencillas:

* A través de la **Ventana de contexto (Memoria a corto plazo):** Dentro de un solo diálogo, envías al modelo no solo una nueva pregunta, sino también **toda o parte de la correspondencia anterior**. El modelo procesa todo este texto como un único "contexto". Es gracias a esto que "recuerda" las observaciones anteriores y continúa el pensamiento. La limitación aquí es la longitud de la ventana de contexto (el número de tokens).
* Creación de **Instrucciones del sistema (System Prompt):** Puedes establecer el rol, el tono y las reglas de conducta del modelo al principio de cada diálogo. Por ejemplo: "Eres un experto en Python, responde brevemente".
* La inclusión en la consulta de varios ejemplos del comportamiento deseado **Aprendizaje de pocos disparos (Few-Shot Learning):** (pares de entrada/salida) permite al modelo "aprender" este patrón directamente dentro de la consulta actual.
* **Gestión del estado en el lado de la aplicación:** La forma más poderosa. La aplicación (que accede a la API) puede almacenar información sobre el usuario (preferencias, historial, datos de perfil) y añadirla dinámicamente al prompt antes de enviarla al modelo.


### 2. 

El ajuste fino es el proceso de reentrenamiento de un LLM base ya preparado en tu propio conjunto de datos específico. Esto permite que el modelo:

* **Adapte el estilo y el tono:** El modelo hablará "en tu idioma", ya sea un estricto lenguaje científico, un marketing amigable o la jerga de una comunidad específica.
* **Siga instrucciones y formatos específicos:** Si necesitas respuestas en una estructura JSON estrictamente definida, o siempre con un conjunto específico de campos.
* **Comprenda el lenguaje específico del dominio:** El entrenamiento en tu documentación interna o en textos de la industria ayudará al modelo a manejar mejor la terminología de tu nicho.
* **Mejore el rendimiento en tareas específicas:** Para ciertos tipos de consultas (por ejemplo, clasificación de reseñas, generación de código en un marco específico), el ajuste fino puede proporcionar respuestas más precisas y relevantes que el modelo base.
* **Reduzca la longitud de los prompts:** Si el modelo ya "conoce" el comportamiento deseado gracias al ajuste, no es necesario que se lo recuerdes cada vez en el prompt, lo que ahorra tokens y reduce la latencia.


### 3. 

El ajuste fino es una herramienta poderosa, pero no universal. No deberías usarlo si:

* **El modelo necesita acceder a nuevos conocimientos:** El ajuste fino cambia los pesos del modelo, pero no "carga" nuevos hechos en él en tiempo real. Si tu tarea es responder preguntas basadas en una base de conocimientos en constante cambio (documentos de la empresa, últimas noticias), es mejor usar la **Generación Aumentada por Recuperación (RAG)**. Aquí, el modelo base recibe el contexto de tu base de datos *en el momento de la consulta*.
* **Una tarea simple se resuelve con ingeniería de prompts:** Empieza siempre con la ingeniería de prompts más eficaz posible. Si la tarea se resuelve con instrucciones simples y ejemplos de pocos disparos, el ajuste fino es redundante y más costoso.
* **No tienes suficientes datos de alta calidad:** Malos datos = mal modelo ajustado.


### 4. Preparación de datos.

La calidad y la cantidad de tus datos son fundamentales. El modelo aprende de tus ejemplos, por lo que deben ser precisos, diversos y coherentes.

* **Formato:** La mayoría de las veces JSON Lines (`.jsonl`) o CSV (`.csv`).
* **Estructura de datos:** Depende de la tarea.
    * **Ajuste de instrucciones (Instruction-Response):** Adecuado para tareas generalizadas como "pregunta-respuesta", parafraseo, resumen.
        ```json
        {"input_text": "Parafrasea la oración: 'La tecnología de IA se está desarrollando rápidamente.'", "output_text": "La inteligencia artificial está demostrando un rápido progreso."}
        {"input_text": "Nombra la capital de Francia.", "output_text": "La capital de Francia es París."}
        ```
    * **Ajuste de chat (Chat Tuning):** Ideal para entrenar al modelo a mantener un diálogo en un rol o estilo específico.
        ```json
        {"messages": [{"author": "user", "content": "¡Hola! ¿Qué me recomiendas para cenar?"}, {"author": "model", "content": "¡Buenas noches! Hoy es un gran día para la pasta a la carbonara o, si prefieres algo ligero, una ensalada César."}]}
        {"messages": [{"author": "user", "content": "Háblame de las nuevas características de Python 3.12."}, {"author": "model", "content": "Python 3.12 introdujo las f-strings con sangría, una nueva sintaxis para genéricos universales y un mejor manejo de los errores de Unicode."}]}
        ```
* **Cantidad:** Un mínimo de 100-200 ejemplos de alta calidad, pero cuantos más, mejor (miles para tareas serias).
* **Calidad:** Precisión, coherencia de estilo, tono y formato en todo el conjunto de datos.


### 5. Modelos y plataformas


#### 5.1. OpenAI

OpenAI proporciona una API bastante simple e intuitiva para el ajuste fino.

**Proceso:**

1.  Prepara los datos en formato JSONL, donde cada línea es un objeto con una matriz de `messages` (como en la API de Chat Completions).
2.  Sube el archivo de datos a través de la API.
3.  Crea un trabajo de ajuste fino, especificando el archivo subido y el modelo base.
4.  Sigue el progreso.
5.  Usa el nuevo modelo ajustado por su ID.

**Ejemplo de datos (archivo `training_data.jsonl`):**

```json
{"messages": [{"role": "system", "content": "Eres un amable asistente de soporte al cliente de una empresa de TI."}, {"role": "user", "content": "Mi internet no funciona."}, {"role": "assistant", "content": "¡Oh, lamento las molestias! Intentemos resolverlo. ¿Cómo estás conectado a Internet, por Wi-Fi o por cable?"}]}
{"messages": [{"role": "system", "content": "Eres un amable asistente de soporte al cliente de una empresa de TI."}, {"role": "user", "content": "¿Cómo puedo restablecer mi contraseña?"}, {"role": "assistant", "content": "¡Por supuesto! Para restablecer tu contraseña, ve a la página de inicio de sesión y haz clic en '¿Olvidaste tu contraseña?' debajo del campo de entrada. Luego, sigue las instrucciones en pantalla."}]}
```

**Ejemplo de código Python:**

Primero, instala: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Establece tu clave de API de OpenAI. Se recomienda usar una variable de entorno.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Subiendo el archivo de datos
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

# 2. Creando un trabajo de ajuste fino
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Puedes especificar una versión concreta, por ejemplo, "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Trabajo de ajuste fino creado. ID del trabajo: {job_id}")
    print("Sigue el estado del trabajo a través de la API o en OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Error al crear el trabajo: {e.status_code} - {e.response}")
    exit()

# Ejemplo de seguimiento del estado y obtención del nombre del modelo (ejecutar después de crear el trabajo):
# # job_id = "ftjob-..." # Reemplaza con el ID de tu trabajo
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Estado actual del trabajo: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Nombre del modelo ajustado: {fine_tuned_model_name}")

# 3. Usando el modelo ajustado (después de que esté listo)
# # Reemplaza con el nombre real de tu modelo, obtenido después de un ajuste fino exitoso
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "Tengo un problema con mi inicio de sesión."}
# #             ]
# #         )
# #         print("\nRespuesta del modelo ajustado:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Error al usar el modelo: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **no proporciona una API pública para el ajuste fino de sus modelos Claude 3 (Opus, Sonnet, Haiku) en el mismo sentido que OpenAI o Google.**

Anthropic se centra en la creación de modelos base muy potentes que, según afirman, funcionan muy bien con la ingeniería de prompts avanzada y los patrones RAG, minimizando la necesidad de ajuste fino en la mayoría de los casos.
Para grandes clientes corporativos o socios, puede haber programas para crear modelos "personalizados" o integraciones especializadas, pero esta no es una función de ajuste fino disponible públicamente a través de la API.

Si trabajas con Claude 3, tu principal objetivo debería ser:

* **Ingeniería de prompts de calidad:** Experimenta con instrucciones del sistema, ejemplos de pocos disparos y un formato de consulta claro. Claude es conocido por su capacidad para seguir estrictamente las instrucciones, especialmente en las etiquetas XML.
* **Sistemas RAG:** Usa bases de conocimiento externas para proporcionar al modelo un contexto actualizado.

#### 5.3. Google (Gemini)

Google está desarrollando activamente capacidades de ajuste fino a través de su plataforma **Google Cloud Vertex AI**.
Se trata de una plataforma de ML completa que proporciona herramientas para la preparación de datos, la ejecución de trabajos de entrenamiento y el despliegue de modelos.
El ajuste fino está disponible para la familia de modelos Gemini.

**Proceso:**

1.  Prepara los datos (JSONL o CSV) en formato `input_text`/`output_text` (para el ajuste de instrucciones) o `messages` (para el ajuste de chat).
2.  Sube los datos a Google Cloud Storage (GCS).
3.  Crea y ejecuta un trabajo de ajuste fino a través de la consola de Vertex AI o el SDK.
4.  Despliega el modelo ajustado en un punto de conexión (Endpoint).
5.  Usa el modelo ajustado a través de este punto de conexión.

**Ejemplo de datos (archivo `gemini_tuning_data.jsonl`):**

```json
{"input_text": "Resume las ideas principales de este libro: 'El libro trata sobre el viaje de un héroe, superando obstáculos y encontrándose a sí mismo.'", "output_text": "El personaje principal del libro emprende un viaje transformador, enfrentándose a dificultades y adquiriendo autoconocimiento."}
{"input_text": "Explica el principio de un reactor termonuclear en términos sencillos.", "output_text": "Un reactor termonuclear intenta reproducir el proceso que ocurre en el Sol: la fusión de núcleos atómicos ligeros a temperaturas muy altas, liberando una enorme cantidad de energía."}
```

**Ejemplo de código Python (requiere `google-cloud-aiplatform`):**

Primero, instala: `pip install google-cloud-aiplatform` y `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Configuración ---
# REEMPLAZA con tus valores:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Elige una región que admita Gemini y Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # El nombre de tu bucket de GCS (debe crearse de antemano)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Fin de la configuración ---

# Inicializar Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Crear un archivo de datos (si no existe)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Resume las ideas principales de este libro: \'El libro trata sobre el viaje de un héroe, superando obstáculos y encontrándose a sí mismo.\'", "output_text": "El personaje principal del libro emprende un viaje transformador, enfrentándose a dificultades y adquiriendo autoconocimiento."}\n')
    f.write('{"input_text": "Explica el principio de un reactor termonuclear en términos sencillos.", "output_text": "Un reactor termonuclear intenta reproducir el proceso que ocurre en el Sol: la fusión de núcleos atómicos ligeros a temperaturas muy altas, liberando una enorme cantidad de energía."}\n')
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
    print(f"Error al subir el archivo a GCS. Asegúrate de que el bucket existe y tienes permisos: {e}")
    exit()

# 3. Crear y ejecutar un trabajo de ajuste fino
print(f"\nIniciando el ajuste fino del modelo '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` inicia el trabajo y devuelve el modelo ajustado después de la finalización
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Modelo base Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Número de pasos de entrenamiento. El valor óptimo depende del tamaño de los datos.
        # batch_size=16, # Puedes especificar
        # learning_rate_multiplier=1.0 # Puedes especificar
    )
    print(f"Modelo '{TUNED_MODEL_DISPLAY_NAME}' ajustado con éxito. ID del modelo: {tuned_model.name}")
    print("El proceso de ajuste fino puede llevar un tiempo considerable.")
except Exception as e:
    print(f"Error de ajuste fino. Comprueba los registros en la consola de Vertex AI: {e}")
    exit()

# 4. Desplegar el modelo ajustado (para su uso)
print(f"\nDesplegando el modelo ajustado '{TUNED_MODEL_DISPLAY_NAME}' en un punto de conexión...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Tipo de máquina para el punto de conexión. Elige uno adecuado.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Modelo desplegado en el punto de conexión: {endpoint.name}")
    print("El despliegue también puede tardar varios minutos.")
except Exception as e:
    print(f"Error al desplegar el modelo: {e}")
    exit()

# 5. Usar el modelo ajustado
print("\nProbando el modelo ajustado...")
prompt = "Háblame de tus capacidades después del entrenamiento."
instances = [{"prompt": prompt}] # Para el ajuste de instrucciones. Si es ajuste de chat, entonces {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nRespuesta del modelo ajustado:")
    print(response.predictions[0])
except Exception as e:
    print(f"Error al usar el modelo ajustado: {e}")

# Después de terminar el trabajo, no olvides eliminar el punto de conexión y el modelo para evitar costes innecesarios:
# endpoint.delete()
# tuned_model.delete()
```

### 6. Recomendaciones generales

* **Empieza poco a poco:** No intentes entrenar un modelo con miles de ejemplos de inmediato. Empieza con un conjunto de datos pequeño pero de alta calidad.
* **Itera:** El ajuste fino es un proceso iterativo. Entrena, evalúa, ajusta los datos o los hiperparámetros, repite.
* **Supervisión:** Supervisa atentamente las métricas de entrenamiento (pérdida) y usa un conjunto de datos de validación para evitar el sobreajuste.
* **Evaluación:** Prueba siempre el modelo ajustado con datos que *nunca ha visto* durante el entrenamiento para evaluar su capacidad de generalización.
* **Coste:** Recuerda que el ajuste fino y el despliegue de puntos de conexión son servicios de pago. Tenlo en cuenta en tu presupuesto.
* **Documentación:** Consulta siempre la documentación oficial del proveedor de LLM. Las API y las capacidades evolucionan constantemente.
