## Spickzettel. Personalisierung von LLM: Prompts, Feinabstimmung von Modellen, Codebeispiele.

In diesem Artikel:

1.  Wie der "Memory-Effekt" in LLM erzeugt wird (kurzer Überblick).
2.  Warum und wann eine Feinabstimmung (Fine-tuning) eines Modells erforderlich ist.
3.  Wann Feinabstimmung nicht die beste Lösung ist.
4.  Datenvorbereitung.
5.  Beispiele für die Feinabstimmung für **OpenAI (GPT)**, **Google (Gemini)** und **Anthropic (Claude)** (unterscheidet sich).

### 1. Wie LLM "sich erinnert" und "sich anpasst": Die Illusion des Kontexts

Bevor wir über Feinabstimmung sprechen, ist es wichtig zu verstehen, wie LLM es überhaupt schafft, ein Gefühl der Personalisierung zu erzeugen.
Dies ist wichtig, um sich nicht in eine kostspielige Feinabstimmung zu stürzen, wenn die Aufgabe mit einfacheren Methoden gelöst werden kann:

*   Über das **Kontextfenster (Kurzzeitgedächtnis):** Innerhalb eines einzelnen Dialogs senden Sie dem Modell nicht nur eine neue Frage, sondern auch **die gesamte oder einen Teil der vorherigen Korrespondenz**. Das Modell verarbeitet diesen gesamten Text als einen einzigen "Kontext". Dank dessen "erinnert" es sich an frühere Bemerkungen und setzt den Gedanken fort. Die Einschränkung hier ist die Länge des Kontextfensters (Anzahl der Token).
*   Erstellung von **Systemanweisungen (System Prompt):** Sie können dem Modell eine Rolle, einen Ton und Verhaltensregeln zuweisen. Zum Beispiel: "Sie sind ein Python-Experte, antworten Sie kurz."
*   Aufnahme mehrerer Beispiele für das gewünschte Verhalten in die Anfrage **Few-Shot Learning:** (Eingabe-/Ausgabe-Paare) ermöglicht es dem Modell, dieses Muster direkt innerhalb der aktuellen Anfrage zu "lernen".
*   **Anwendungsseitiges Zustandsmanagement:** Die leistungsstärkste Methode. Die Anwendung (die auf die API zugreift) kann Benutzerinformationen (Präferenzen, Verlauf, Profildaten) speichern und diese dynamisch dem Prompt hinzufügen, bevor sie an das Modell gesendet werden.

### 2. 

Feinabstimmung ist der Prozess des weiteren Trainings eines bereits vorbereiteten Basis-LLM auf Ihrem eigenen, spezifischen Datensatz. Dies ermöglicht dem Modell:

*   **Stil und Ton anzupassen:** Das Modell spricht "Ihre Sprache" – sei es streng wissenschaftlich, freundlich marketingorientiert oder der Slang einer bestimmten Gemeinschaft.
*   **Spezifische Anweisungen und Formate zu befolgen:** Wenn Sie Antworten in einer streng definierten JSON-Struktur oder immer mit einem bestimmten Satz von Feldern benötigen.
*   **Domänenspezifische Sprache zu verstehen:** Das Training mit Ihrer internen Dokumentation oder branchenspezifischen Texten hilft dem Modell, die Terminologie Ihrer Nische besser zu verarbeiten.
*   **Die Leistung bei engen Aufgaben zu verbessern:** Für bestimmte Arten von Anfragen (z. B. Sentiment-Klassifizierung, Codegenerierung in einem bestimmten Framework) kann die Feinabstimmung genauere und relevantere Antworten liefern als das Basismodell.
*   **Die Prompt-Länge zu reduzieren:** Wenn das Modell das gewünschte Verhalten durch Feinabstimmung bereits "kennt", müssen Sie es nicht jedes Mal im Prompt daran erinnern, was Token spart und die Latenz reduziert.

### 3. 

Feinabstimmung ist ein leistungsstarkes, aber kein universelles Werkzeug. Sie sollten es nicht verwenden, wenn:

*   **Das Modell auf neues Wissen zugreifen muss:** Feinabstimmung ändert die Gewichte des Modells, aber es "lädt" keine neuen Fakten in Echtzeit in es. Wenn Ihre Aufgabe darin besteht, Fragen auf der Grundlage einer sich ständig ändernden Wissensbasis (Unternehmensdokumente, neueste Nachrichten) zu beantworten, ist es besser, **Retrieval Augmented Generation (RAG)** zu verwenden. Hier erhält das Basismodell den Kontext aus Ihrer Datenbank *während der Abfrageausführung*.
*   **Eine einfache Aufgabe durch Prompt-Engineering gelöst werden kann:** Beginnen Sie immer mit dem effektivsten Prompt-Engineering. Wenn die Aufgabe mit einfachen Anweisungen und Few-Shot-Beispielen gelöst werden kann, ist die Feinabstimmung überflüssig und kostspieliger.
*   **Sie nicht über genügend hochwertige Daten verfügen:** Schlechte Daten = schlecht abgestimmtes Modell.

### 4. Datenvorbereitung. 

Die Qualität und Quantität Ihrer Daten sind von entscheidender Bedeutung. Das Modell lernt aus Ihren Beispielen, daher müssen diese genau, vielfältig und konsistent sein.

*   **Format:** Meistens JSON Lines (<code>.jsonl</code>) oder CSV (<code>.csv</code>).
*   **Datenstruktur:** Abhängig von der Aufgabe.
    *   **Instruction Tuning (Anweisung-Antwort):** Geeignet für verallgemeinerte Aufgaben wie Frage-Antwort, Umformulierung, Zusammenfassung.
        ```json
        {"input_text": "Formulieren Sie den Satz um: 'KI-Technologie entwickelt sich rasant.'", "output_text": "Künstliche Intelligenz zeigt rasante Fortschritte."}
        {"input_text": "Nennen Sie die Hauptstadt Frankreichs.", "output_text": "Die Hauptstadt Frankreichs ist Paris."}
        ```
    *   **Chat Tuning (Chat):** Ideal, um das Modell darin zu schulen, einen Dialog in einer bestimmten Rolle oder einem bestimmten Stil zu führen.
        ```json
        {"messages": [{"author": "user", "content": "Hallo! Was empfehlen Sie zum Abendessen?"}, {"author": "model", "content": "Guten Abend! Heute ist ein großartiger Tag für Pasta Carbonara, oder, wenn Sie etwas Leichtes bevorzugen, einen Caesar-Salat."}]}
        {"messages": [{"author": "user", "content": "Erzählen Sie mir von neuen Funktionen in Python 3.12."}, {"author": "model", "content": "In Python 3.12 wurden f-Strings mit Einrückungen, eine neue Syntax für universelle Generika und eine verbesserte Unicode-Fehlerbehandlung eingeführt."}]}
        ```
*   **Menge:** Mindestens 100-200 hochwertige Beispiele, aber je mehr, desto besser (Tausende für ernsthafte Aufgaben).
*   **Qualität:** Genauigkeit, Konsistenz von Stil, Ton und Format im gesamten Datensatz.

### 5. Modelle und Plattformen

#### 5.1. OpenAI

OpenAI bietet eine recht einfache und intuitive API zur Feinabstimmung.

**Prozess:**

1.  Bereiten Sie die Daten im JSONL-Format vor, wobei jede Zeile ein Objekt mit einem Array von <code>messages</code> ist (wie in der Chat Completions API).
2.  Laden Sie die Datendatei über die API hoch.
3.  Erstellen Sie einen Feinabstimmungsauftrag, indem Sie die hochgeladene Datei und das Basismodell angeben.
4.  Überwachen Sie den Fortschritt.
5.  Verwenden Sie das neue, feinabgestimmte Modell anhand seiner ID.

**Beispieldaten (Datei <code>training_data.jsonl</code>):**

```json
{"messages": [{"role": "system", "content": "Sie sind ein freundlicher Assistent für den Kundensupport eines IT-Unternehmens."}, {"role": "user", "content": "Mein Internet funktioniert nicht."}, {"role": "assistant", "content": "Oh, entschuldigen Sie die Unannehmlichkeiten! Lassen Sie uns versuchen, das Problem zu lösen. Wie sind Sie mit dem Internet verbunden – über Wi-Fi oder über Kabel?"}]}
{"messages": [{"role": "system", "content": "Sie sind ein freundlicher Assistent für den Kundensupport eines IT-Unternehmens."}, {"role": "user", "content": "Wie kann ich mein Passwort zurücksetzen?"}, {"role": "assistant", "content": "Gerne! Um Ihr Passwort zurückzusetzen, gehen Sie bitte zur Anmeldeseite und klicken Sie unter dem Eingabefeld auf 'Passwort vergessen?'. Befolgen Sie dann die Anweisungen auf dem Bildschirm."}]}
```

**Beispiel Python-Code:**

Vorher installieren: <code>pip install openai</code>

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

# 2. Erstellen eines Feinabstimmungsauftrags
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Sie können eine bestimmte Version angeben, z. B. "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Feinabstimmungsauftrag erstellt. Auftrags-ID: {job_id}")
    print("Überwachen Sie den Auftragsstatus über die API oder im OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Fehler beim Erstellen des Auftrags: {e.status_code} - {e.response}")
    exit()

# Beispiel für die Statusüberwachung und das Abrufen des Modellnamens (nach Auftragserstellung ausführen):
# # job_id = "ftjob-..." # Ersetzen Sie dies durch Ihre Auftrags-ID
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Aktueller Auftragsstatus: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Name des feinabgestimmten Modells: {fine_tuned_model_name}")

# 3. Verwenden des feinabgestimmten Modells (nachdem es bereit ist)
# # Ersetzen Sie dies durch den tatsächlichen Namen Ihres Modells, der nach erfolgreicher Feinabstimmung erhalten wurde
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "Ich habe ein Anmeldeproblem."}
# #             ]
# #         )
# #         print("\nAntwort des feinabgestimmten Modells:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Fehler bei der Verwendung des Modells: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **bietet keine öffentliche API zur Feinabstimmung seiner Claude 3-Modelle (Opus, Sonnet, Haiku) in dem Sinne an, wie es OpenAI oder Google tun.**

Anthropic konzentriert sich auf die Erstellung sehr leistungsstarker Basismodelle, die nach eigenen Angaben hervorragend mit fortschrittlichem Prompt-Engineering und RAG-Mustern funktionieren und die Notwendigkeit einer Feinabstimmung in den meisten Fällen minimieren.
Für große Unternehmenskunden oder Partner kann es Programme zur Erstellung von "benutzerdefinierten" Modellen oder spezialisierten Integrationen geben, aber dies ist keine öffentlich zugängliche Feinabstimmungsfunktion über die API.

Wenn Sie mit Claude 3 arbeiten, sollten Sie sich hauptsächlich auf Folgendes konzentrieren:

*   **Hochwertiges Prompt-Engineering:** Experimentieren Sie mit Systemanweisungen, Few-Shot-Beispielen und klarer Formatierung von Anfragen. Claude ist bekannt für seine Fähigkeit, Anweisungen, insbesondere in XML-Tags, streng zu befolgen.
*   **RAG-Systeme:** Verwenden Sie externe Wissensdatenbanken, um dem Modell relevanten Kontext bereitzustellen.

#### 5.3. Google (Gemini)

Google entwickelt aktiv Feinabstimmungsfunktionen über seine Plattform **Google Cloud Vertex AI**.
Dies ist eine vollwertige ML-Plattform, die Tools zur Datenvorbereitung, zum Ausführen von Trainingsaufträgen und zum Bereitstellen von Modellen bereitstellt.
Die Feinabstimmung ist für Modelle der Gemini-Familie verfügbar.

**Prozess:**

1.  Bereiten Sie Daten (JSONL oder CSV) im Format `input_text`/`output_text` (für Instruction Tuning) oder `messages` (für Chat Tuning) vor.
2.  Laden Sie Daten in Google Cloud Storage (GCS) hoch.
3.  Erstellen und führen Sie einen Feinabstimmungsauftrag über die Vertex AI Console oder das SDK aus.
4.  Stellen Sie das feinabgestimmte Modell an einem Endpunkt bereit.
5.  Verwenden Sie das feinabgestimmte Modell über diesen Endpunkt.

**Beispieldaten (Datei <code>gemini_tuning_data.jsonl</code>):**

```json
{"input_text": "Fassen Sie die Hauptideen dieses Buches zusammen: 'Das Buch erzählt von der Reise eines Helden, der Hindernisse überwindet und sich selbst findet.'", "output_text": "Die Hauptfigur des Buches begibt sich auf eine transformative Reise, stellt sich Herausforderungen und erlangt Selbsterkenntnis."}
{"input_text": "Erklären Sie das Funktionsprinzip eines thermonuklearen Reaktors in einfachen Worten.", "output_text": "Ein thermonuklearer Reaktor versucht, den Prozess zu reproduzieren, der auf der Sonne stattfindet: die Fusion leichter Atomkerne bei sehr hohen Temperaturen, wodurch enorme Energiemengen freigesetzt werden."}
```

**Beispiel Python-Code (erfordert <code>google-cloud-aiplatform</code>):**

Vorher installieren: <code>pip install google-cloud-aiplatform</code> und <code>pip install google-cloud-storage</code>

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
    f.write('{"input_text": "Fassen Sie die Hauptideen dieses Buches zusammen: \'Das Buch erzählt von der Reise eines Helden, der Hindernisse überwindet und sich selbst findet.\'", "output_text": "Die Hauptfigur des Buches begibt sich auf eine transformative Reise, stellt sich Herausforderungen und erlangt Selbsterkenntnis."}\n')
    f.write('{"input_text": "Erklären Sie das Funktionsprinzip eines thermonuklearen Reaktors in einfachen Worten.", "output_text": "Ein thermonuklearer Reaktor versucht, den Prozess zu reproduzieren, der auf der Sonne stattfindet: die Fusion leichter Atomkerne bei sehr hohen Temperaturen, wodurch enorme Energiemengen freigesetzt werden."}\n')
print(f"Datendatei '{DATA_FILE_LOCAL_PATH}' erstellt.")


# 2. Hochladen der Daten in Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Lädt eine Datei in einen GCS-Bucket hoch."""
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
print(f"\nStart der Feinabstimmung des Modells '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` startet den Auftrag und gibt das feinabgestimmte Modell nach Abschluss zurück
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Basismodell Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Anzahl der Trainingsschritte. Optimaler Wert hängt von der Datengröße ab.
        # batch_size=16, # Kann angegeben werden
        # learning_rate_multiplier=1.0 # Kann angegeben werden
    )
    print(f"Modell '{TUNED_MODEL_DISPLAY_NAME}' erfolgreich feinabgestimmt. Modell-ID: {tuned_model.name}")
    print("Der Feinabstimmungsprozess kann erhebliche Zeit in Anspruch nehmen.")
except Exception as e:
    print(f"Fehler bei der Feinabstimmung. Überprüfen Sie die Protokolle in der Vertex AI Console: {e}")
    exit()

# 4. Bereitstellen des feinabgestimmten Modells (zur Verwendung)
print(f"\nBereitstellen des feinabgestimmten Modells '{TUNED_MODEL_DISPLAY_NAME}' am Endpunkt...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Maschinentyp für den Endpunkt. Wählen Sie den geeigneten.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Modell am Endpunkt bereitgestellt: {endpoint.name}")
    print("Die Bereitstellung kann ebenfalls einige Minuten dauern.")
except Exception as e:
    print(f"Fehler beim Bereitstellen des Modells: {e}")
    exit()

# 5. Verwenden des feinabgestimmten Modells
print("\nTesten des feinabgestimmten Modells...")
prompt = "Erzählen Sie mir von Ihren Fähigkeiten nach dem Training."
instances = [{"prompt": prompt}] # Für Instruction Tuning. Bei Chat Tuning: {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nAntwort des feinabgestimmten Modells:")
    print(response.predictions[0])
except Exception as e:
    print(f"Fehler bei der Verwendung des feinabgestimmten Modells: {e}")

# Nach Abschluss der Arbeit nicht vergessen, den Endpunkt und das Modell zu löschen, um unnötige Kosten zu vermeiden:
# endpoint.delete()
# tuned_model.delete()

```