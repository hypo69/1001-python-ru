## Spickzettel. Personalisierung von LLM: Prompts, Feinabstimmung von Modellen, Codebeispiele.

In diesem Artikel:

1.  Wie der "Memory-Effekt" in LLM erzeugt wird (kurzer Überblick).
2.  Warum und wann eine Feinabstimmung (Fine-tuning) des Modells erforderlich ist.
3.  Wann Feinabstimmung nicht die beste Lösung ist.
4.  Datenvorbereitung.
5.  Beispiele für die Feinabstimmung für **OpenAI (GPT)**, **Google (Gemini)** und **Anthropic (Claude)** (unterscheidet sich).

### 1. Wie LLM "sich erinnert" und "sich anpasst": Die Illusion des Kontexts

Bevor wir über Feinabstimmung sprechen, ist es wichtig zu verstehen, wie LLM es überhaupt schafft, ein Gefühl der Personalisierung zu erzeugen.
Dies ist wichtig, um sich nicht in eine kostspielige Feinabstimmung zu stürzen, wenn die Aufgabe mit einfacheren Methoden gelöst werden kann:

*   Über das **Kontextfenster (Kurzzeitgedächtnis):** Innerhalb eines einzelnen Dialogs senden Sie dem Modell nicht nur eine neue Frage, sondern auch **die gesamte oder einen Teil der vorherigen Korrespondenz**. Das Modell verarbeitet diesen gesamten Text als einen einzigen "Kontext". Dank dessen "erinnert" es sich an frühere Bemerkungen und setzt den Gedanken fort. Die Einschränkung hier ist die Länge des Kontextfensters (Anzahl der Token).
*   Erstellung von **Systemanweisungen (System Prompt):** Sie können dem Modell zu Beginn jedes Dialogs eine Rolle, einen Ton und Verhaltensregeln zuweisen. Zum Beispiel: "Sie sind ein Python-Experte, antworten Sie prägnant."
*   Die Aufnahme mehrerer Beispiele für das gewünschte Verhalten in die Anfrage **Few-Shot Learning:** (Eingabe-/Ausgabe-Paare) ermöglicht es dem Modell, dieses Muster direkt innerhalb der aktuellen Anfrage zu "lernen".
*   **Zustandsverwaltung auf Anwendungsseite:** Der leistungsstärkste Weg. Die Anwendung (die auf die API zugreift) kann Informationen über den Benutzer (Präferenzen, Verlauf, Profildaten) speichern und diese dynamisch zum Prompt hinzufügen, bevor sie an das Modell gesendet werden.


### 2.

Feinabstimmung ist der Prozess des weiteren Trainings eines bereits vorhandenen Basis-LLM auf Ihrem eigenen, spezifischen Datensatz. Dies ermöglicht dem Modell:

*   **Stil und Ton anpassen:** Das Modell spricht "Ihre Sprache" – sei es streng wissenschaftlich, freundlich marketingorientiert oder der Slang einer bestimmten Gemeinschaft.
*   **Spezifische Anweisungen und Formate befolgen:** Wenn Sie Antworten in einer streng definierten JSON-Struktur oder immer mit einem bestimmten Satz von Feldern benötigen.
*   **Domänenspezifische Sprache verstehen:** Das Training mit Ihrer internen Dokumentation oder branchenspezifischen Texten hilft dem Modell, die Terminologie Ihrer Nische besser zu verarbeiten.
*   **Leistung bei engen Aufgaben verbessern:** Für bestimmte Arten von Abfragen (z. B. Sentiment-Klassifizierung, Codegenerierung in einem bestimmten Framework) kann die Feinabstimmung genauere und relevantere Antworten liefern als das Basismodell.
*   **Prompt-Länge reduzieren:** Wenn das Modell das gewünschte Verhalten durch die Abstimmung bereits "kennt", müssen Sie es nicht jedes Mal im Prompt daran erinnern, was Token spart und die Latenz reduziert.

### 3.

Feinabstimmung ist ein mächtiges, aber kein universelles Werkzeug. Sie sollten es nicht verwenden, wenn:

*   **Das Modell Zugriff auf neues Wissen erhalten soll:** Die Feinabstimmung ändert die Gewichte des Modells, aber sie "lädt" keine neuen Fakten in Echtzeit in es. Wenn Ihre Aufgabe darin besteht, Fragen auf der Grundlage einer sich ständig ändernden Wissensbasis (Unternehmensdokumente, neueste Nachrichten) zu beantworten, ist es besser, **Retrieval Augmented Generation (RAG)** zu verwenden. Hier erhält das Basismodell den Kontext aus Ihrer Datenbank *zum Zeitpunkt der Abfrage*.
*   **Eine einfache Aufgabe durch Prompt Engineering gelöst werden kann:** Beginnen Sie immer mit dem effektivsten Prompt Engineering. Wenn die Aufgabe mit einfachen Anweisungen und Few-Shot-Beispielen gelöst werden kann, ist die Feinabstimmung überflüssig und kostspieliger.
*   **Sie nicht über genügend hochwertige Daten verfügen:** Schlechte Daten = schlecht abgestimmtes Modell.

### 4. Datenvorbereitung.

Die Qualität und Quantität Ihrer Daten sind von entscheidender Bedeutung. Das Modell lernt aus Ihren Beispielen, daher müssen diese präzise, vielfältig und konsistent sein.

*   **Format:** Meistens JSON Lines (`.jsonl`) oder CSV (`.csv`).
*   **Datenstruktur:** Abhängig von der Aufgabe.
    *   **Instruction Tuning (Anweisung-Antwort):** Geeignet für verallgemeinerte Aufgaben wie "Frage-Antwort", Paraphrasierung, Zusammenfassung.
        ```json
        {"input_text": "Перефразируй предложение: 'Технология ИИ стремительно развивается.'", "output_text": "Искусственный интеллект демонстрирует стремительный прогресс."}
        {"input_text": "Назови столицу Франции.", "output_text": "Столица Франции — Париж."}
        ```
    *   **Chat Tuning (Chat):** Ideal zum Trainieren des Modells, um einen Dialog in einer bestimmten Rolle oder einem bestimmten Stil zu führen.
        ```json
        {"messages": [{"author": "user", "content": "Привет! Что порекомендуешь на ужин?"}, {"author": "model", "content": "Добрый вечер! Сегодня отличный день для пасты Карбонара, или, если вы предпочитаете что-то легкое, салат Цезарь."}]}
        {"messages": [{"author": "user", "content": "Расскажи про новые фичи в Python 3.12."}, {"author": "model", "content": "В Python 3.12 появились f-строки с отступами, новый синтаксис для универсальных генериков и улучшенная обработка ошибок Unicode."}]}
        ```
*   **Menge:** Mindestens 100-200 hochwertige Beispiele, aber je mehr, desto besser (Tausende für ernsthafte Aufgaben).
*   **Qualität:** Genauigkeit, konsistenter Stil, Ton und Format im gesamten Datensatz.

### 5. Modelle und Plattformen


#### 5.1. OpenAI

OpenAI bietet eine ziemlich einfache und intuitive API für die Feinabstimmung.

**Prozess:**

1.  Bereiten Sie die Daten im JSONL-Format vor, wobei jede Zeile ein Objekt mit einem `messages`-Array ist (wie in der Chat Completions API).
2.  Laden Sie die Datendatei über die API hoch.
3.  Erstellen Sie einen Feinabstimmungsauftrag, indem Sie die hochgeladene Datei und das Basismodell angeben.
4.  Überwachen Sie den Fortschritt.
5.  Verwenden Sie das neue, abgestimmte Modell anhand seiner ID.

**Beispieldaten (Datei `training_data.jsonl`):**

```json
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I apologize for the inconvenience! Let's try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the on-screen instructions."}]}
```

**Beispiel Python-Code:**

Vorher installieren: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Legen Sie Ihren OpenAI API-Schlüssel fest. Es wird empfohlen, eine Umgebungsvariable zu verwenden.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Hochladen der Datendatei
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Datei erfolgreich hochgeladen. Datei-ID: {file_id}")
except openai.APIStatusError as e:
    print(f"Fehler beim Hochladen der Datei: {e.status_code} - {e.response}")
    exit()

# 2. Erstellen des Feinabstimmungsauftrags
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Sie können eine bestimmte Version angeben, z.B. "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Feinabstimmungsauftrag erstellt. Auftrags-ID: {job_id}")
    print("Überwachen Sie den Auftragsstatus über die API oder im OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Fehler beim Erstellen des Auftrags: {e.status_code} - {e.response}")
    exit()

# Beispiel für die Überwachung des Status und das Abrufen des Modellnamens (nach Auftragserstellung ausführen):
# # job_id = "ftjob-..." # Ersetzen Sie durch Ihre Auftrags-ID
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Aktueller Auftragsstatus: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Name des abgestimmten Modells: {fine_tuned_model_name}")

# 3. Verwenden des abgestimmten Modells (nachdem es bereit ist)
# # Ersetzen Sie durch den tatsächlichen Namen Ihres Modells, der nach erfolgreicher Feinabstimmung erhalten wurde
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "Ich habe ein Anmeldeproblem."}
# #             ]
# #         )
# #         print("\nAntwort des abgestimmten Modells:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Fehler bei der Verwendung des Modells: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **bietet keine öffentliche API zur Feinabstimmung seiner Claude 3-Modelle (Opus, Sonnet, Haiku) in der gleichen Weise wie OpenAI oder Google an.**

Anthropic konzentriert sich auf die Erstellung sehr leistungsfähiger Basismodelle, die nach eigenen Angaben hervorragend mit fortgeschrittenem Prompt Engineering und RAG-Mustern zusammenarbeiten und den Bedarf an Feinabstimmung in den meisten Fällen minimieren.
Für große Unternehmenskunden oder Partner kann es Programme zur Erstellung von "benutzerdefinierten" Modellen oder spezialisierten Integrationen geben, aber dies ist keine öffentlich zugängliche Feinabstimmungsfunktion über die API.

Wenn Sie mit Claude 3 arbeiten, sollte Ihr Hauptaugenmerk liegen auf:

*   **Hochwertiges Prompt Engineering:** Experimentieren Sie mit Systemanweisungen, Few-Shot-Beispielen, klarer Formatierung von Anfragen. Claude ist bekannt für seine Fähigkeit, Anweisungen, insbesondere in XML-Tags, streng zu befolgen.
*   **RAG-Systeme:** Verwenden Sie externe Wissensdatenbanken, um dem Modell relevanten Kontext bereitzustellen.

#### 5.3. Google (Gemini)

Google entwickelt aktiv Feinabstimmungsfunktionen über seine Plattform **Google Cloud Vertex AI**.
Dies ist eine vollwertige ML-Plattform, die Tools zur Datenvorbereitung, zum Ausführen von Trainingsaufträgen und zum Bereitstellen von Modellen bereitstellt.
Die Feinabstimmung ist für Modelle der Gemini-Familie verfügbar.

**Prozess:**

1.  Bereiten Sie die Daten (JSONL oder CSV) im Format `input_text`/`output_text` (für die Anweisungsabstimmung) oder `messages` (für die Chat-Abstimmung) vor.
2.  Laden Sie Daten in Google Cloud Storage (GCS) hoch.
3.  Erstellen und führen Sie einen Feinabstimmungsauftrag über die Vertex AI Console oder das SDK aus.
4.  Stellen Sie das abgestimmte Modell an einem Endpunkt (Endpoint) bereit.
5.  Verwenden Sie das abgestimmte Modell über diesen Endpunkt.

**Beispieldaten (Datei `gemini_tuning_data.jsonl`):**

```json
{"input_text": "Суммируй основные идеи этой книги: 'Книга рассказывает о путешествии героя, который преодолевает препятствия и находит себя.'", "output_text": "Главный герой книги отправляется в трансформирующее путешествие, сталкиваясь с трудностями и обретая самопознание."}
{"input_text": "Объясни принцип работы термоядерного реактора простыми словами.", "output_text": "Термоядерный реактор пытается воспроизвести процесс, который происходит на Солнце: слияние легких атомных ядер при очень высоких температурах, высвобождая огромное количество энергии."}
```

**Beispiel Python-Code (erfordert `google-cloud-aiplatform`):**

Vorher installieren: `pip install google-cloud-aiplatform` und `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Einstellungen ---
# ERSETZEN Sie durch Ihre Werte:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Wählen Sie eine Region, die Gemini und Vertex AI unterstützt
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Name Ihres GCS-Buckets (muss vorher erstellt werden)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Ende der Einstellungen ---

# Initialisierung von Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Erstellen der Datendatei (falls nicht vorhanden)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Sumiere die Hauptideen dieses Buches: \'Das Buch erzählt die Geschichte einer Heldenreise, der Hindernisse überwindet und sich selbst findet.\'", "output_text": "Der Hauptcharakter des Buches begibt sich auf eine transformative Reise, stellt sich Herausforderungen und findet Selbsterkenntnis."}\n')
    f.write('{"input_text": "Erklären Sie das Funktionsprinzip eines thermonuklearen Reaktors in einfachen Worten.", "output_text": "Ein thermonuklearer Reaktor versucht, den Prozess zu replizieren, der auf der Sonne stattfindet: die Fusion leichter Atomkerne bei sehr hohen Temperaturen, wodurch eine enorme Menge an Energie freigesetzt wird."}\n')
print(f"Datendatei '{DATA_FILE_LOCAL_PATH}' erstellt.")


# 2. Hochladen der Daten in Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Lädt eine Datei in den GCS-Bucket hoch."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Datei '{source_file_name}' hochgeladen nach 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Fehler beim Hochladen der Datei in GCS. Stellen Sie sicher, dass der Bucket existiert und Sie Berechtigungen haben: {e}")
    exit()

# 3. Erstellen und Ausführen des Feinabstimmungsauftrags
print(f"\nStarte Feinabstimmung des Modells '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` startet den Auftrag und gibt das abgestimmte Modell nach Abschluss zurück
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Basismodell Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Anzahl der Trainingsschritte. Optimaler Wert hängt von der Datengröße ab.
        # batch_size=16, # Kann angegeben werden
        # learning_rate_multiplier=1.0 # Kann angegeben werden
    )
    print(f"Modell '{TUNED_MODEL_DISPLAY_NAME}' erfolgreich abgestimmt. Modell-ID: {tuned_model.name}")
    print("Der Feinabstimmungsprozess kann einige Zeit in Anspruch nehmen.")
except Exception as e:
    print(f"Feinabstimmungsfehler. Überprüfen Sie die Protokolle in der Vertex AI Console: {e}")
    exit()

# 4. Bereitstellen des abgestimmten Modells (zur Verwendung)
print(f"\nBereitstellen des abgestimmten Modells '{TUNED_MODEL_DISPLAY_NAME}' am Endpunkt...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Maschinentyp für den Endpunkt. Wählen Sie den geeigneten.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Modell am Endpunkt bereitgestellt: {endpoint.name}")
    print("Die Bereitstellung kann ebenfalls mehrere Minuten dauern.")
except Exception as e:
    print(f"Fehler beim Bereitstellen des Modells: {e}")
    exit()

# 5. Verwenden des abgestimmten Modells
print("\nTesten des abgestimmten Modells...")
prompt = "Erzählen Sie mir von Ihren Fähigkeiten nach dem Training."
instances = [{"prompt": prompt}] # Für Anweisungsabstimmung. Bei Chat-Abstimmung: {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nAntwort des abgestimmten Modells:")
    print(response.predictions[0])
except Exception as e:
    print(f"Fehler bei der Verwendung des abgestimmten Modells: {e}")

# Nach Abschluss nicht vergessen, den Endpunkt und das Modell zu löschen, um unnötige Kosten zu vermeiden:
# endpoint.delete()
# tuned_model.delete()
```

### 6. Allgemeine Empfehlungen

*   **Beginnen Sie klein:** Versuchen Sie nicht, das Modell sofort mit Tausenden von Beispielen zu trainieren. Beginnen Sie mit einem kleinen, aber hochwertigen Datensatz.
*   **Iterieren:** Feinabstimmung ist ein iterativer Prozess. Trainieren, bewerten, Daten oder Hyperparameter anpassen, wiederholen.
*   **Überwachung:** Überwachen Sie sorgfältig die Trainingsmetriken (Verluste) und verwenden Sie einen Validierungsdatensatz, um Überanpassung zu vermeiden.
*   **Bewertung:** Testen Sie das abgestimmte Modell immer mit Daten, die es während des Trainings *nie gesehen* hat, um seine Generalisierungsfähigkeit zu beurteilen.
*   **Kosten:** Denken Sie daran, dass Feinabstimmung und Bereitstellung von Endpunkten kostenpflichtig sind. Berücksichtigen Sie dies in Ihrem Budget.
*   **Dokumentation:** Beziehen Sie sich immer auf die offizielle Dokumentation des LLM-Anbieters. APIs und Funktionen entwickeln sich ständig weiter.
