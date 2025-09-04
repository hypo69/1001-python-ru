## Ściągawka. Personalizacja LLM: prompty, dostrajanie modeli, przykłady kodu.

W tym artykule:

1.  Jak powstaje "efekt pamięci" w LLM (krótki przegląd).
2.  Dlaczego i kiedy potrzebne jest dostrajanie (Fine-tuning) modelu.
3.  Kiedy dostrajanie nie jest najlepszym rozwiązaniem.
4.  Przygotowanie danych.
5.  Przykłady dostrajania dla **OpenAI (GPT)**, **Google (Gemini)** i **Anthropic (Claude)** (różni się).

### 1. Jak LLM "pamięta" i "dostosowuje się": Iluzja kontekstu

Zanim przejdziemy do dostrajania, ważne jest, aby zrozumieć, jak LLM w ogóle udaje się stworzyć poczucie personalizacji.
Jest to ważne, aby nie rzucać się w kosztowne dostrajanie, jeśli zadanie można rozwiązać prostszymi metodami:

*   Poprzez **Okno kontekstowe (Pamięć krótkotrwała):** W ramach jednego dialogu wysyłasz modelowi nie tylko nowe pytanie, ale także **całą lub część poprzedniej korespondencji**. Model przetwarza cały ten tekst jako jeden "kontekst". Dzięki temu "pamięta" poprzednie wypowiedzi i kontynuuje myśl. Ograniczeniem jest tutaj długość okna kontekstowego (liczba tokenów).
*   Tworzenie **Instrukcji systemowych (System Prompt):** Możesz ustawić rolę, ton i zasady zachowania modelu na początku każdego dialogu. Na przykład: "Jesteś ekspertem Pythona, odpowiadaj zwięźle".
*   Włączenie do zapytania kilku przykładów pożądanego zachowania **Uczenie z kilku przykładów (Few-Shot Learning):** (pary wejście/wyjście) pozwala modelowi "nauczyć się" tego wzorca bezpośrednio w ramach bieżącego zapytania.
*   **Zarządzanie stanem po stronie aplikacji:** Najpotężniejszy sposób. Aplikacja (która odwołuje się do API) może przechowywać informacje o użytkowniku (preferencje, historię, dane profilu) i dynamicznie dodawać je do promptu przed wysłaniem do modelu.

### 2.

Dostrajanie to proces dalszego szkolenia już przygotowanego bazowego LLM na własnym, specyficznym zestawie danych. Pozwala to modelowi na:

*   **Dostosowanie stylu i tonu:** Model będzie mówił "Twoim językiem" – czy to surowym naukowym, przyjaznym marketingowym, czy slangiem określonej społeczności.
*   **Przestrzeganie specyficznych instrukcji i formatów:** Jeśli potrzebujesz odpowiedzi w ściśle określonej strukturze JSON lub zawsze z określonym zestawem pól.
*   **Zrozumienie języka specyficznego dla domeny:** Szkolenie na Twojej wewnętrznej dokumentacji lub tekstach branżowych pomoże modelowi lepiej radzić sobie z terminologią Twojej niszy.
*   **Poprawę wydajności w wąskich zadaniach:** W przypadku niektórych typów zapytań (np. klasyfikacja sentymentu, generowanie kodu w określonym frameworku) dostrajanie może zapewnić dokładniejsze i bardziej trafne odpowiedzi niż model bazowy.
*   **Skrócenie długości promptów:** Jeśli model "zna" już pożądane zachowanie dzięki dostrojeniu, nie musisz mu o tym przypominać za każdym razem w prompcie, co oszczędza tokeny i zmniejsza opóźnienia.

### 3.

Dostrajanie to potężne, ale nie uniwersalne narzędzie. Nie należy go używać, jeśli:

*   **Model musi mieć dostęp do nowej wiedzy:** Dostrajanie zmienia wagi modelu, ale nie "ładuje" do niego nowych faktów w czasie rzeczywistym. Jeśli Twoim zadaniem jest odpowiadanie na pytania na podstawie stale zmieniającej się bazy wiedzy (dokumenty firmowe, najnowsze wiadomości), lepiej użyć **Generacji Rozszerzonej o Pobieranie (RAG)**. Tutaj model bazowy uzyskuje kontekst z Twojej bazy danych *podczas wykonywania zapytania*.
*   **Proste zadanie można rozwiązać za pomocą inżynierii promptów:** Zawsze zaczynaj od najbardziej efektywnej inżynierii promptów. Jeśli zadanie można rozwiązać za pomocą prostych instrukcji i kilku przykładów, dostrajanie jest zbędne i bardziej kosztowne.
*   **Nie masz wystarczającej ilości wysokiej jakości danych:** Złe dane = źle dostrojony model.

### 4. Przygotowanie danych.

Jakość i ilość Twoich danych są kluczowe. Model uczy się na Twoich przykładach, dlatego muszą być one dokładne, różnorodne i spójne.

*   **Format:** Najczęściej JSON Lines (<code>.jsonl</code>) lub CSV (<code>.csv</code>).
*   **Struktura danych:** Zależy od zadania.
    *   **Dostrajanie instrukcji (Instruction Tuning - Instrukcja-Odpowiedź):** Nadaje się do uogólnionych zadań, takich jak pytania-odpowiedzi, przeformułowywanie, podsumowywanie.
        ```json
        {"input_text": "Przeformułuj zdanie: 'Technologia AI szybko się rozwija.'", "output_text": "Sztuczna inteligencja wykazuje szybki postęp."}
        {"input_text": "Podaj stolicę Francji.", "output_text": "Stolicą Francji jest Paryż."}
        ```
    *   **Dostrajanie czatu (Chat Tuning - Czat):** Idealne do szkolenia modelu w prowadzeniu dialogu w określonej roli lub stylu.
        ```json
        {"messages": [{"author": "user", "content": "Cześć! Co polecasz na obiad?"}, {"author": "model", "content": "Dobry wieczór! Dziś jest świetny dzień na makaron Carbonara, lub, jeśli wolisz coś lekkiego, sałatkę Cezar."}]}
        {"messages": [{"author": "user", "content": "Opowiedz mi o nowych funkcjach w Pythonie 3.12."}, {"author": "model", "content": "W Pythonie 3.12 pojawiły się f-stringi z wcięciami, nowa składnia dla uniwersalnych generyków i ulepszona obsługa błędów Unicode."}]}
        ```
*   **Ilość:** Minimum 100-200 wysokiej jakości przykładów, ale im więcej, tym lepiej (tysiące dla poważnych zadań).
*   **Jakość:** Dokładność, spójność stylu, tonu i formatu w całym zestawie danych.

### 5. Modele i platformy

#### 5.1. OpenAI

OpenAI zapewnia dość prosty i intuicyjny interfejs API do dostrajania.

**Proces:**

1.  Przygotuj dane w formacie JSONL, gdzie każdy wiersz to obiekt z tablicą <code>messages</code> (jak w Chat Completions API).
2.  Prześlij plik danych za pośrednictwem API.
3.  Utwórz zadanie dostrajania, określając przesłany plik i model bazowy.
4.  Monitoruj postęp.
5.  Użyj nowego, dostrojonego modelu po jego ID.

**Przykładowe dane (plik <code>training_data.jsonl</code>):**

```json
{"messages": [{"role": "system", "content": "Jesteś przyjaznym asystentem wsparcia klienta firmy IT."}, {"role": "user", "content": "Mój internet nie działa."}, {"role": "assistant", "content": "Och, przepraszam za niedogodności! Spróbujmy to rozgryźć. Jak jesteś podłączony do internetu – przez Wi-Fi czy przez kabel?"}]}
{"messages": [{"role": "system", "content": "Jesteś przyjaznym asystentem wsparcia klienta firmy IT."}, {"role": "user", "content": "Jak mogę zresetować hasło?"}, {"role": "assistant", "content": "Oczywiście! Aby zresetować hasło, przejdź na stronę logowania i kliknij 'Zapomniałeś hasła?' pod polem wprowadzania. Następnie postępuj zgodnie z instrukcjami na ekranie."}]}
```

**Przykładowy kod Python:**

Zainstaluj wcześniej: <code>pip install openai</code>

```python
import openai
from openai import OpenAI
import os

# Ustaw swój klucz API OpenAI. Zaleca się używanie zmiennej środowiskowej.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Przesyłanie pliku danych
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Plik przesłany pomyślnie. ID pliku: {file_id}")
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

# Przykład monitorowania statusu i pobierania nazwy modelu (uruchom po utworzeniu zadania):
# # job_id = "ftjob-..." # Zastąp swoim ID zadania
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Aktualny status zadania: {job_status.status}")
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
```</pre>
<h4>5.2. Anthropic</h4>
<p>Anthropic <strong>nie udostępnia publicznego API do dostrajania swoich modeli Claude 3 (Opus, Sonnet, Haiku) w tym samym sensie, co OpenAI czy Google.</strong></p>
<p>Anthropic koncentruje się na tworzeniu bardzo potężnych modeli bazowych, które, jak twierdzą, doskonale współpracują z zaawansowaną inżynierią promptów i wzorcami RAG, minimalizując potrzebę dostrajania w większości przypadków.
For large enterprise clients or partners, there may be programs for creating "custom" models or specialized integrations, but this is not a publicly available fine-tuning function via API.</p>
<p>If you are working with Claude 3, your primary focus should be on:</p>
<ul>
<li><strong>Wysokiej jakości inżynieria promptów:</strong> Eksperymentuj z instrukcjami systemowymi, przykładami few-shot, wyraźnym formatowaniem zapytań. Claude jest znany z umiejętności ścisłego przestrzegania instrukcji, zwłaszcza w tagach XML.</li>
<li><strong>Systemy RAG:</strong> Używaj zewnętrznych baz wiedzy, aby dostarczyć modelowi odpowiedni kontekst.</li>
</ul>
<h4>5.3. Google (Gemini)</h4>
<p>Google aktywnie rozwija możliwości dostrajania za pośrednictwem swojej platformy <strong>Google Cloud Vertex AI</strong>.
Jest to pełnoprawna platforma ML, która zapewnia narzędzia do przygotowywania danych, uruchamiania zadań szkoleniowych i wdrażania modeli.
Dostrajanie jest dostępne dla modeli z rodziny Gemini.</p>
<p><strong>Proces:</strong></p>
<ol>
<li>Przygotuj dane (JSONL lub CSV) w formacie <code>input_text</code>/<code>output_text</code> (do dostrajania instrukcji) lub <code>messages</code> (do dostrajania czatu).</li>
<li>Prześlij dane do Google Cloud Storage (GCS).</li>
<li>Utwórz i uruchom zadanie dostrajania za pośrednictwem konsoli Vertex AI lub SDK.</li>
<li>Wdróż dostrojony model na punkcie końcowym (Endpoint).</li>
<li>Użyj dostrojonego modelu za pośrednictwem tego punktu końcowego.</li>
</ol>
<p><strong>Przykładowe dane (plik <code>gemini_tuning_data.jsonl</code>):</strong></p>
<pre class="line-numbers"><code class="language-json">{"input_text": "Podsumuj główne idee tej książki: 'Książka opowiada o podróży bohatera, który pokonuje przeszkody i odnajduje siebie.'", "output_text": "Główny bohater książki wyrusza w transformacyjną podróż, stawiając czoła wyzwaniom i osiągając samopoznanie."}
{"input_text": "Wyjaśnij zasadę działania reaktora termojądrowego w prostych słowach.", "output_text": "Reaktor termojądrowy próbuje odtworzyć proces zachodzący na Słońcu: fuzję lekkich jąder atomowych w bardzo wysokich temperaturach, uwalniając ogromne ilości energii."}
</code></pre>
<p><strong>Przykładowy kod Python (wymaga <code>google-cloud-aiplatform</code>):</strong></p>
<p>Zainstaluj wcześniej: <code>pip install google-cloud-aiplatform</code> i <code>pip install google-cloud-storage</code></p>
<pre class="line-numbers"><code class="language-python">import os
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
    f.write('{"input_text": "Podsumuj główne idee tej książki: \'Książka opowiada o podróży bohatera, który pokonuje przeszkody i odnajduje siebie.\'", "output_text": "Główny bohater książki wyrusza w transformacyjną podróż, stawiając czoła wyzwaniom i osiągając samopoznanie."}\n')
    f.write('{"input_text": "Wyjaśnij zasadę działania reaktora termojądrowego w prostych słowach.", "output_text": "Reaktor termojądrowy próbuje odtworzyć proces zachodzący na Słońcu: fuzję lekkich jąder atomowych w bardzo wysokich temperaturach, uwalniając ogromne ilości energii."}\n')
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
print(f"\nRozpoczynanie dostrajania modelu '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` uruchamia zadanie i zwraca dostrojony model po zakończeniu
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Bazowy model Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Liczba kroków treningowych. Optymalna wartość zależy od rozmiaru danych.
        # batch_size=16, # Można określić
        # learning_rate_multiplier=1.0 # Można określić
    )
    print(f"Model '{TUNED_MODEL_DISPLAY_NAME}' dostrojony pomyślnie. ID modelu: {tuned_model.name}")
    print("Proces dostrajania może zająć sporo czasu.")
except Exception as e:
    print(f"Błąd dostrajania. Sprawdź logi w konsoli Vertex AI: {e}")
    exit()

# 4. Wdrażanie dostrojonego modelu (do użytku)
print(f"\nWdrażanie dostrojonego modelu '{TUNED_MODEL_DISPLAY_NAME}' na punkt końcowy...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Typ maszyny dla punktu końcowego. Wybierz odpowiedni.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Model wdrożony na punkt końcowy: {endpoint.name}")
    print("Wdrażanie również może zająć kilka minut.")
except Exception as e:
    print(f"Błąd wdrażania modelu: {e}")
    exit()

# 5. Używanie dostrojonego modelu
print("\nTestowanie dostrojonego modelu...")
prompt = "Opowiedz mi o swoich możliwościach po treningu."
instances = [{"prompt": prompt}] # Do dostrajania instrukcji. Jeśli dostrajanie czatu, to {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nOdpowiedź dostrojonego modelu:")
    print(response.predictions[0])
except Exception as e:
    print(f"Błąd podczas używania dostrojonego modelu: {e}")

# Po zakończeniu pracy, nie zapomnij usunąć punktu końcowego i modelu, aby uniknąć niepotrzebnych kosztów:
# # endpoint.delete()
# # tuned_model.delete()
</code></pre>
<h3>6. Ogólne rekomendacje</h3>
<ul>
<li><strong>Zacznij od małego:</strong> Nie próbuj od razu szkolić modelu na tysiącach przykładów. Zacznij od małego, ale wysokiej jakości zestawu danych.</li>
<li><strong>Iteruj:</strong> Dostrajanie to proces iteracyjny. Szkol, oceniaj, dostosowuj dane lub hiperparametry, powtarzaj.</li>
<li><strong>Monitorowanie:</strong> Dokładnie monitoruj metryki szkoleniowe (stratę) i używaj zestawu danych walidacyjnych, aby uniknąć przetrenowania.</li>
<li><strong>Ocena:</strong> Zawsze testuj dostrojony model na danych, których *nigdy nie widział* podczas szkolenia, aby ocenić jego zdolność do generalizacji.</li>
<li><strong>Koszt:</strong> Pamiętaj, że dostrajanie i wdrażanie punktów końcowych są płatne. Uwzględnij to w swoim budżecie.</li>
<li><strong>Dokumentacja:</strong> Zawsze odwołuj się do oficjalnej dokumentacji dostawcy LLM. Interfejsy API i możliwości stale ewoluują.</li>
</ul>
