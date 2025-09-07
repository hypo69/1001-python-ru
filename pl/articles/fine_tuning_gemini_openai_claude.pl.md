## Ściągawka. Personalizacja LLM: prompty, dostrajanie modeli, przykłady kodu.

W tym artykule:

1.  Jak tworzy się "efekt pamięci" w LLM (krótki przegląd).
2.  Po co i kiedy potrzebne jest dostrajanie (Fine-tuning) modelu.
3.  Kiedy dostrajanie nie jest najlepszym rozwiązaniem.
4.  Przygotowanie danych.
5.  Przykłady dostrajania dla **OpenAI (GPT)**, **Google (Gemini)** i **Anthropic (Claude)** (różni się).

### 1. Jak LLM "pamięta" i "dostosowuje się": Iluzja kontekstu

Zanim przejdziemy do dostrajania, ważne jest, aby zrozumieć, jak LLM w ogóle udaje się stworzyć poczucie personalizacji.
Jest to ważne, aby nie rzucać się w kosztowne dostrajanie, jeśli zadanie można rozwiązać prostszymi metodami:

*   Poprzez **Okno Kontekstu (Pamięć Krótkotrwała):** W ramach jednego dialogu wysyłasz modelowi nie tylko nowe pytanie, ale także **całą lub część poprzedniej korespondencji**. Model przetwarza cały ten tekst jako jeden "kontekst". Dzięki temu "pamięta" poprzednie wypowiedzi i kontynuuje myśl. Ograniczeniem jest tutaj długość okna kontekstu (liczba tokenów).
*   Tworzenie **Instrukcji Systemowych (System Prompt):** Możesz ustawić rolę, ton, zasady zachowania modelu na początku każdego dialogu. Na przykład: "Jesteś ekspertem Pythona, odpowiadaj zwięźle."
*   Włączenie do zapytania kilku przykładów pożądanego zachowania **Few-Shot Learning:** (pary wejście/wyjście) pozwala modelowi "nauczyć się" tego wzorca bezpośrednio w ramach bieżącego zapytania.
*   **Zarządzanie stanem po stronie aplikacji:** Najpotężniejszy sposób. Aplikacja (która odwołuje się do API) może przechowywać informacje o użytkowniku (preferencje, historię, dane profilowe) i dynamicznie dodawać je do promptu przed wysłaniem do modelu.


### 2.

Dostrajanie to proces dalszego szkolenia już gotowego bazowego LLM na własnym, specyficznym zestawie danych. Pozwala to modelowi:

*   **Dostosować styl i ton:** Model będzie mówił "Twoim językiem" – czy to ściśle naukowym, przyjaznym marketingowym, czy slangiem określonej społeczności.
*   **Postępować zgodnie ze specyficznymi instrukcjami i formatami:** Jeśli potrzebujesz odpowiedzi w ściśle określonej strukturze JSON, lub zawsze z określonym zestawem pól.
*   **Zrozumieć język specyficzny dla domeny:** Szkolenie na wewnętrznej dokumentacji lub tekstach branżowych pomoże modelowi lepiej radzić sobie z terminologią Twojej niszy.
*   **Poprawić wydajność w wąskich zadaniach:** Dla niektórych typów zapytań (np. klasyfikacja opinii, generowanie kodu w określonym frameworku) dostrajanie może zapewnić dokładniejsze i bardziej trafne odpowiedzi niż model bazowy.
*   **Skrócić długość promptów:** Jeśli model "zna" już pożądane zachowanie dzięki dostrojeniu, nie musisz mu o tym przypominać za każdym razem w prompcie, co oszczędza tokeny i zmniejsza opóźnienia.

### 3.

Dostrajanie to potężne, ale nie uniwersalne narzędzie. Nie należy go używać, jeśli:

*   **Model powinien mieć dostęp do nowej wiedzy:** Dostrajanie zmienia wagi modelu, ale nie "ładuje" do niego nowych faktów w czasie rzeczywistym. Jeśli Twoim zadaniem jest odpowiadanie na pytania na podstawie stale zmieniającej się bazy wiedzy (dokumenty firmowe, najnowsze wiadomości), lepiej użyć **Retrieval Augmented Generation (RAG)**. Tutaj model bazowy otrzymuje kontekst z Twojej bazy danych *w momencie zapytania*.
*   **Proste zadanie można rozwiązać inżynierią promptów:** Zawsze zaczynaj od najbardziej efektywnej inżynierii promptów. Jeśli zadanie można rozwiązać prostymi instrukcjami i przykładami few-shot, dostrajanie jest zbędne i bardziej kosztowne.
*   **Nie masz wystarczającej ilości wysokiej jakości danych:** Złe dane = źle dostrojony model.

### 4. Przygotowanie danych.

Jakość i ilość Twoich danych są kluczowe. Model uczy się na Twoich przykładach, dlatego muszą być one dokładne, różnorodne i spójne.

*   **Format:** Najczęściej JSON Lines (`.jsonl`) lub CSV (`.csv`).
*   **Struktura danych:** Zależy od zadania.
    *   **Instruction Tuning (Instrukcja-Odpowiedź):** Nadaje się do uogólnionych zadań typu "pytanie-odpowiedź", parafrazy, podsumowania.
        ```json
        {"input_text": "Перефразируй предложение: 'Технология ИИ стремительно развивается.'", "output_text": "Искусственный интеллект демонстрирует стремительный прогресс."}
        {"input_text": "Назови столицу Франции.", "output_text": "Столица Франции — Париж."}
        ```
    *   **Chat Tuning (Czat):** Idealny do szkolenia modelu w prowadzeniu dialogu w określonej roli lub stylu.
        ```json
        {"messages": [{"author": "user", "content": "Привет! Что порекомендуешь на ужин?"}, {"author": "model", "content": "Добрый вечер! Сегодня отличный день для пасты Карбонара, или, если вы предпочитаете что-то легкое, салат Цезарь."}]}
        {"messages": [{"author": "user", "content": "Расскажи про новые фичи w Python 3.12."}, {"author": "model", "content": "W Python 3.12 pojawiły się f-stroki z odstupami, nowy składnia dla uniwersalnych generyków i ulepszona obsługa błędów Unicode."}]}
        ```
*   **Ilość:** Minimum 100-200 wysokiej jakości przykładów, ale im więcej, tym lepiej (tysiące dla poważnych zadań).
*   **Jakość:** Dokładność, spójny styl, ton, format w całym zestawie danych.

### 5. Modele i Platformy


#### 5.1. OpenAI

OpenAI zapewnia dość prosty i intuicyjny interfejs API do dostrajania.

**Proces:**

1.  Przygotuj dane w formacie JSONL, gdzie każda linia to obiekt z tablicą `messages` (jak w API Chat Completions).
2.  Prześlij plik danych za pośrednictwem API.
3.  Utwórz zadanie dostrajania, określając przesłany plik i model bazowy.
4.  Monitoruj postęp.
5.  Użyj nowego, dostrojonego modelu po jego ID.

**Przykładowe dane (plik `training_data.jsonl`):**

```json
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I apologize for the inconvenience! Let's try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the on-screen instructions."}]}
```

**Przykładowy kod Python:**

Zainstaluj wcześniej: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Ustaw swój klucz API OpenAI. Zaleca się użycie zmiennej środowiskowej.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Przesyłanie pliku danych
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Plik pomyślnie przesłany. ID pliku: {file_id}")
except openai.APIStatusError as e:
    print(f"Błąd przesyłania pliku: {e.status_code} - {e.response}")
    exit()

# 2. Tworzenie zadania dostrajania
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Możesz określić konkretną wersję, np. "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Zadanie dostrajania utworzone. ID zadania: {job_id}")
    print("Monitoruj status zadania za pośrednictwem API lub w OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Błąd tworzenia zadania: {e.status_code} - {e.response}")
    exit()

# Przykład monitorowania statusu i pobierania nazwy modelu (wykonaj po utworzeniu zadania):
# # job_id = "ftjob-..." # Zastąp swoim ID zadania
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Bieżący status zadania: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Nazwa dostrojonego modelu: {fine_tuned_model_name}")

# 3. Używanie dostrojonego modelu (po jego gotowości)
# # Zastąp rzeczywistą nazwą swojego modelu, uzyskaną po pomyślnym dostrojeniu
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "Mam problem z logowaniem."}
# #             ]
# #         )
# #         print("\nOdpowiedź dostrojonego modelu:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Błąd podczas używania modelu: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **nie udostępnia publicznego API do dostrajania swoich modeli Claude 3 (Opus, Sonnet, Haiku) w taki sam sposób, jak OpenAI czy Google.**

Anthropic koncentruje się na tworzeniu bardzo potężnych modeli bazowych, które, jak twierdzą, doskonale współpracują z zaawansowaną inżynierią promptów i wzorcami RAG, minimalizując potrzebę dostrajania w większości przypadków.
Dla dużych klientów korporacyjnych lub partnerów mogą istnieć programy tworzenia modeli "niestandardowych" lub specjalistycznych integracji, ale nie jest to publicznie dostępna funkcja dostrajania za pośrednictwem API.

Jeśli pracujesz z Claude 3, Twoim głównym celem powinno być:

*   **Wysokiej jakości inżynieria promptów:** Eksperymentuj z instrukcjami systemowymi, przykładami few-shot, wyraźnym formatowaniem zapytań. Claude jest znany z umiejętności ścisłego przestrzegania instrukcji, zwłaszcza w tagach XML.
*   **Systemy RAG:** Używaj zewnętrznych baz wiedzy, aby dostarczyć modelowi odpowiedni kontekst.

#### 5.3. Google (Gemini)

Google aktywnie rozwija możliwości dostrajania za pośrednictwem swojej platformy **Google Cloud Vertex AI**.
Jest to pełnoprawna platforma ML, która zapewnia narzędzia do przygotowywania danych, uruchamiania zadań szkoleniowych i wdrażania modeli.
Dostrajanie jest dostępne dla modeli z rodziny Gemini.

**Proces:**

1.  Przygotuj dane (JSONL lub CSV) w formacie `input_text`/`output_text` (do dostrajania instrukcji) lub `messages` (do dostrajania czatu).
2.  Prześlij dane do Google Cloud Storage (GCS).
3.  Utwórz i uruchom zadanie dostrajania za pośrednictwem konsoli Vertex AI lub SDK.
4.  Wdróż dostrojony model do punktu końcowego (Endpoint).
5.  Użyj dostrojonego modelu za pośrednictwem tego punktu końcowego.

**Przykładowe dane (plik `gemini_tuning_data.jsonl`):**

```json
{"input_text": "Summarize the main ideas of this book: 'The book tells the story of a hero's journey, who overcomes obstacles and finds himself.'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and achieving self-discovery."}
{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to replicate the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}
```

**Przykładowy kod Python (wymaga `google-cloud-aiplatform`):**

Zainstaluj wcześniej: `pip install google-cloud-aiplatform` i `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Ustawienia ---
# ZASTĄP swoimi wartościami:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Wybierz region obsługujący Gemini i Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Nazwa Twojego bucketa GCS (musi być utworzony wcześniej)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Koniec ustawień ---

# Inicjalizacja Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Tworzenie pliku danych (jeśli nie istnieje)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Summarize the main ideas of this book: \'The book tells the story of a hero\'s journey, who overcomes obstacles and finds himself.\'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and achieving self-discovery."}\n')
    f.write('{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to replicate the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}\n')
print(f"Plik danych '{DATA_FILE_LOCAL_PATH}' utworzony.")


# 2. Przesyłanie danych do Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Przesyła plik do bucketa GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Plik '{source_file_name}' przesłany do 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Błąd przesyłania pliku do GCS. Upewnij się, że bucket istnieje i masz uprawnienia: {e}")
    exit()

# 3. Tworzenie i uruchamianie zadania dostrajania
print(f"\nUruchamianie dostrajania modelu '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` uruchamia zadanie i zwraca dostrojony model po zakończeniu
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Bazowy model Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Liczba kroków szkoleniowych. Optymalna wartość zależy od rozmiaru danych.
        # batch_size=16, # Można określić
        # learning_rate_multiplier=1.0 # Można określić
    )
    print(f"Model '{TUNED_MODEL_DISPLAY_NAME}' pomyślnie dostrojony. ID modelu: {tuned_model.name}")
    print("Proces dostrajania może zająć sporo czasu.")
except Exception as e:
    print(f"Błąd dostrajania. Sprawdź logi w konsoli Vertex AI: {e}")
    exit()

# 4. Wdrażanie dostrojonego modelu (do użytku)
print(f"\nWdrażanie dostrojonego modelu '{TUNED_MODEL_DISPLAY_NAME}' do punktu końcowego...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Typ maszyny dla punktu końcowego. Wybierz odpowiedni.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Model wdrożony do punktu końcowego: {endpoint.name}")
    print("Wdrażanie również może zająć kilka minut.")
except Exception as e:
    print(f"Błąd wdrażania modelu: {e}")
    exit()

# 5. Używanie dostrojonego modelu
print("\nTestowanie dostrojonego modelu...")
prompt = "Opowiedz mi o swoich możliwościach po szkoleniu."
instances = [{"prompt": prompt}] # Do dostrajania instrukcji. Jeśli dostrajanie czatu, to {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nOdpowiedź dostrojonego modelu:")
    print(response.predictions[0])
except Exception as e:
    print(f"Błąd podczas używania dostrojonego modelu: {e}")

# Po zakończeniu, nie zapomnij usunąć punktu końcowego i modelu, aby uniknąć niepotrzebnych kosztów:
# endpoint.delete()
# tuned_model.delete()
```

### 6. Ogólne zalecenia

*   **Zacznij od małych kroków:** Nie próbuj od razu szkolić modelu na tysiącach przykładów. Zacznij od małego, ale wysokiej jakości zestawu danych.
*   **Iteruj:** Dostrajanie to proces iteracyjny. Szkol, oceniaj, dostosowuj dane lub hiperparametry, powtarzaj.
*   **Monitorowanie:** Dokładnie monitoruj metryki szkoleniowe (straty) i używaj zestawu danych walidacyjnych, aby uniknąć przetrenowania.
*   **Ocena:** Zawsze testuj dostrojony model na danych, których *nigdy nie widział* podczas szkolenia, aby ocenić jego zdolność do generalizacji.
*   **Koszt:** Pamiętaj, że dostrajanie i wdrażanie punktów końcowych są płatne. Uwzględnij to w swoim budżecie.
*   **Dokumentacja:** Zawsze odwołuj się do oficjalnej dokumentacji dostawcy LLM. API i możliwości stale ewoluują.
