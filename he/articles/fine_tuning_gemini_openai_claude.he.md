## דף עזר. התאמה אישית של LLM: פרומפטים, כוונון עדין של מודלים, דוגמאות קוד.

במאמר זה:

1.  כיצד נוצר "אפקט הזיכרון" ב-LLM (סקירה קצרה).
2.  למה ומתי נדרש כוונון עדין (Fine-tuning) של מודל.
3.  מתי כוונון עדין אינו הפתרון הטוב ביותר.
4.  הכנת נתונים.
5.  דוגמאות לכוונון עדין עבור **OpenAI (GPT)**, **Google (Gemini)** ו-**Anthropic (Claude)** (שונה).

### 1. כיצד LLM "זוכר" ו"מתאים את עצמו": אשליית ההקשר

לפני שנדבר על כוונון עדין, חשוב להבין כיצד LLM מצליח בכלל ליצור תחושה של התאמה אישית.
זה חשוב כדי לא למהר לכוונון עדין יקר אם המשימה ניתנת לפתרון בדרכים פשוטות יותר:

*   באמצעות **חלון הקשר (זיכרון לטווח קצר):** בתוך דיאלוג אחד, אתה שולח למודל לא רק שאלה חדשה, אלא גם **את כל או חלק מההתכתבות הקודמת**. המודל מעבד את כל הטקסט הזה כ"הקשר" יחיד. בזכות זה הוא "זוכר" הערות קודמות וממשיך את המחשבה. המגבלה כאן היא אורך חלון ההקשר (מספר האסימונים).
*   חיבור **הוראות מערכת (System Prompt):** אתה יכול להגדיר למודל תפקיד, טון, כללי התנהגות בתחילת כל דיאלוג. לדוגמה: "אתה מומחה Python, ענה בקצרה."
*   הכללת מספר דוגמאות של התנהגות רצויה בבקשה **Few-Shot Learning:** (זוגות קלט/פלט) מאפשרת למודל "ללמוד" דפוס זה ישירות בתוך הבקשה הנוכחית.
*   **ניהול מצב בצד היישום:** הדרך החזקה ביותר. היישום (שניגש ל-API) יכול לאחסן מידע על המשתמש (העדפות, היסטוריה, נתוני פרופיל) ולהוסיף אותו באופן דינמי לפרומפט לפני שליחתו למודל.


### 2.

כוונון עדין הוא תהליך אימון נוסף של LLM בסיסי קיים על סט נתונים ספציפי משלך. זה מאפשר למודל:

*   **להתאים סגנון וטון:** המודל ידבר "בשפה שלך" – בין אם זה סגנון מדעי קפדני, שיווקי ידידותי או סלנג של קהילה מסוימת.
*   **לפעול לפי הוראות ופורמטים ספציפיים:** אם אתה זקוק לתשובות במבנה JSON מוגדר בקפדנות, או תמיד עם סט שדות ספציפי.
*   **להבין שפה ספציפית לתחום:** אימון על התיעוד הפנימי שלך או טקסטים תעשייתיים יעזור למודל להתמודד טוב יותר עם הטרמינולוגיה של הנישה שלך.
*   **לשפר ביצועים במשימות צרות:** עבור סוגים מסוימים של שאילתות (לדוגמה, סיווג סנטימנטים, יצירת קוד בפריימוורק ספציפי), כוונון עדין יכול לספק תשובות מדויקות ורלוונטיות יותר מאשר המודל הבסיסי.
*   **להפחית את אורך הפרומפטים:** אם המודל כבר "יודע" את ההתנהגות הרצויה בזכות הכוונון, אינך צריך להזכיר לו זאת בכל פעם בפרומפט, מה שחוסך אסימונים ומפחית השהיה.

### 3.

כוונון עדין הוא כלי חזק אך לא אוניברסלי. אל תשתמש בו אם:

*   **המודל צריך לגשת לידע חדש:** כוונון עדין משנה את משקלי המודל, אך אינו "טוען" לתוכו עובדות חדשות בזמן אמת. אם משימתך היא לענות על שאלות המבוססות על בסיס ידע המשתנה ללא הרף (מסמכי חברה, חדשות אחרונות), עדיף להשתמש ב-**Retrieval Augmented Generation (RAG)**. כאן המודל הבסיסי מקבל הקשר ממאגר הנתונים שלך *בזמן השאילתה*.
*   **משימה פשוטה ניתנת לפתרון באמצעות הנדסת פרומפטים:** תמיד התחל עם הנדסת פרומפטים היעילה ביותר. אם המשימה ניתנת לפתרון באמצעות הוראות פשוטות ודוגמאות few-shot, כוונון עדין מיותר ויקר יותר.
*   **אין לך מספיק נתונים באיכות גבוהה:** נתונים גרועים = מודל מכוונן גרוע.

### 4. הכנת נתונים.

האיכות והכמות של הנתונים שלך קריטיות. המודל לומד מהדוגמאות שלך, ולכן הן חייבות להיות מדויקות, מגוונות ועקביות.

*   **פורמט:** לרוב JSON Lines (`.jsonl`) או CSV (`.csv`).
*   **מבנה נתונים:** תלוי במשימה.
    *   **Instruction Tuning (הוראה-תגובה):** מתאים למשימות כלליות כמו "שאלות-תשובות", ניסוח מחדש, סיכום.
        ```json
        {"input_text": "Перефразируй предложение: 'Технология ИИ стремительно развивается.'", "output_text": "Искусственный интеллект демонстрирует стремительный прогресс."}
        {"input_text": "Назови столицу Франции.", "output_text": "Столица Франции — Париж."}
        ```
    *   **Chat Tuning (צ'אט):** אידיאלי לאימון המודל לנהל דיאלוג בתפקיד או בסגנון ספציפי.
        ```json
        {"messages": [{"author": "user", "content": "Привет! Что порекомендуешь на ужин?"}, {"author": "model", "content": "Добрый вечер! Сегодня отличный день для пасты Карбонара, или, если вы предпочитаете что-то легкое, салат Цезарь."}]}
        {"messages": [{"author": "user", "content": "Расскажи про новые фичи в Python 3.12."}, {"author": "model", "content": "В Python 3.12 появились f-строки с отступами, новый синтаксис для универсальных генериков и улучшенная обработка ошибок Unicode."}]}
        ```
*   **כמות:** מינימום 100-200 דוגמאות איכותיות, אך ככל שיותר, כך טוב יותר (אלפים למשימות רציניות).
*   **איכות:** דיוק, עקביות בסגנון, בטון ובפורמט בכל סט הנתונים.

### 5. מודלים ופלטפורמות


#### 5.1. OpenAI

OpenAI מספקת API די פשוט ואינטואיטיבי לכוונון עדין.

**תהליך:**

1.  הכנת נתונים בפורמט JSONL, כאשר כל שורה היא אובייקט עם מערך `messages` (כמו ב-Chat Completions API).
2.  העלאת קובץ הנתונים באמצעות API.
3.  יצירת משימת כוונון עדין, תוך ציון הקובץ שהועלה והמודל הבסיסי.
4.  מעקב אחר ההתקדמות.
5.  שימוש במודל החדש, המכוונן, לפי ה-ID שלו.

**דוגמת נתונים (קובץ `training_data.jsonl`):**

```json
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I apologize for the inconvenience! Let's try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the on-screen instructions."}]}
```

**דוגמת קוד Python:**

התקן מראש: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# הגדר את מפתח ה-API של OpenAI. מומלץ להשתמש במשתנה סביבה.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. העלאת קובץ נתונים
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"קובץ הועלה בהצלחה. ID קובץ: {file_id}")
except openai.APIStatusError as e:
    print(f"שגיאת העלאת קובץ: {e.status_code} - {e.response}")
    exit()

# 2. יצירת משימת כוונון עדין
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # ניתן לציין גרסה ספציפית, לדוגמה, "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"משימת כוונון עדין נוצרה. ID משימה: {job_id}")
    print("עקוב אחר סטטוס המשימה באמצעות API או ב-OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"שגיאת יצירת משימה: {e.status_code} - {e.response}")
    exit()

# דוגמה למעקב אחר סטטוס וקבלת שם המודל (יש לבצע לאחר יצירת המשימה):
# # job_id = "ftjob-..." # החלף ב-ID המשימה שלך
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"סטטוס משימה נוכחי: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"שם המודל המכוונן: {fine_tuned_model_name}")

# 3. שימוש במודל המכוונן (לאחר שהוא מוכן)
# # החלף בשם האמיתי של המודל שלך, שהתקבל לאחר כוונון עדין מוצלח
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "יש לי בעיה בהתחברות."}
# #             ]
# #         )
# #         print("\nתגובת המודל המכוונן:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"שגיאה בשימוש במודל: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **אינה מספקת API ציבורי לכוונון עדין של מודלי Claude 3 שלה (Opus, Sonnet, Haiku) באותו אופן כמו OpenAI או Google.**

Anthropic מתמקדת ביצירת מודלי בסיס חזקים מאוד, שלטענתם, עובדים מצוין עם הנדסת פרומפטים מתקדמת ודפוסי RAG, וממזערים את הצורך בכוונון עדין ברוב המקרים.
עבור לקוחות תאגידיים גדולים או שותפים, ייתכנו תוכניות ליצירת מודלים "מותאמים אישית" או אינטגרציות מיוחדות, אך זו אינה תכונת כוונון עדין זמינה לציבור דרך ה-API.

אם אתה עובד עם Claude 3, ההתמקדות העיקרית שלך צריכה להיות ב:

*   **הנדסת פרומפטים באיכות גבוהה:** התנסה עם הוראות מערכת, דוגמאות few-shot, עיצוב ברור של בקשות. Claude ידוע ביכולתו לציית בקפדנות להוראות, במיוחד בתגי XML.
*   **מערכות RAG:** השתמש במאגרי ידע חיצוניים כדי לספק למודל הקשר רלוונטי.

#### 5.3. Google (Gemini)

Google מפתחת באופן פעיל יכולות כוונון עדין באמצעות פלטפורמת **Google Cloud Vertex AI** שלה.
זוהי פלטפורמת ML מלאה המספקת כלים להכנת נתונים, הפעלת משימות אימון ופריסת מודלים.
כוונון עדין זמין עבור מודלים ממשפחת Gemini.

**תהליך:**

1.  הכנת נתונים (JSONL או CSV) בפורמט `input_text`/`output_text` (עבור כוונון הוראות) או `messages` (עבור כוונון צ'אט).
2.  העלאת נתונים ל-Google Cloud Storage (GCS).
3.  יצירה והפעלה של משימת כוונון עדין באמצעות Vertex AI Console או SDK.
4.  פריסת המודל המכוונן לנקודת קצה (Endpoint).
5.  שימוש במודל המכוונן באמצעות נקודת קצה זו.

**דוגמת נתונים (קובץ `gemini_tuning_data.jsonl`):**

```json
{"input_text": "Суммируй основные идеи этой книги: 'Книга рассказывает о путешествии героя, который преодолевает препятствия и находит себя.'", "output_text": "Главный герой книги отправляется в трансформирующее путешествие, сталкиваясь с трудностями и обретая самопознание."}
{"input_text": "Объясни принцип работы термоядерного реактора простыми словами.", "output_text": "Термоядерный реактор пытается воспроизвести процесс, который происходит на Солнце: слияние легких атомных ядер при очень высоких температурах, высвобождая огромное количество энергии."}
```

**דוגמת קוד Python (דורש `google-cloud-aiplatform`):**

התקן מראש: `pip install google-cloud-aiplatform` ו-`pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- הגדרות ---
# החלף בערכים שלך:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # בחר אזור התומך ב-Gemini וב-Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # שם הבאקט שלך ב-GCS (חייב להיווצר מראש)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- סוף הגדרות ---

# אתחול Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. יצירת קובץ נתונים (אם הוא לא קיים)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Summarize the main ideas of this book: \'The book tells the story of a hero\'s journey, who overcomes obstacles and finds himself.\'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and achieving self-discovery."}\n')
    f.write('{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to replicate the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}\n')
print(f"קובץ נתונים '{DATA_FILE_LOCAL_PATH}' נוצר.")


# 2. העלאת נתונים ל-Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """מעלה קובץ לבאקט GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"קובץ '{source_file_name}' הועלה ל-'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"שגיאת העלאת קובץ ל-GCS. ודא שהבאקט קיים ויש לך הרשאות: {e}")
    exit()

# 3. יצירה והפעלה של משימת כוונון עדין
print(f"\nהפעלת כוונון עדין של מודל '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` מפעיל את המשימה ומחזיר את המודל המכוונן לאחר השלמה
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # מודל בסיס Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # מספר שלבי אימון. ערך אופטימלי תלוי בגודל הנתונים.
        # batch_size=16, # ניתן לציין
        # learning_rate_multiplier=1.0 # ניתן לציין
    )
    print(f"מודל '{TUNED_MODEL_DISPLAY_NAME}' כוונן בהצלחה. ID מודל: {tuned_model.name}")
    print("תהליך הכוונון העדין עשוי לקחת זמן משמעותי.")
except Exception as e:
    print(f"שגיאת כוונון עדין. בדוק יומנים ב-Vertex AI Console: {e}")
    exit()

# 4. פריסת המודל המכוונן (לשימוש)
print(f"\nפורס מודל מכוונן '{TUNED_MODEL_DISPLAY_NAME}' לנקודת קצה...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # סוג מכונה לנקודת קצה. בחר מתאים.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"מודל נפרס לנקודת קצה: {endpoint.name}")
    print("הפריסה עשויה גם לקחת מספר דקות.")
except Exception as e:
    print(f"שגיאת פריסת מודל: {e}")
    exit()

# 5. שימוש במודל המכוונן
print("\nבודק מודל מכוונן...")
prompt = "ספר לי על היכולות שלך לאחר האימון."
instances = [{"prompt": prompt}] # עבור Instruction Tuning. אם Chat Tuning, אז {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nתגובת המודל המכוונן:")
    print(response.predictions[0])
except Exception as e:
    print(f"שגיאה בשימוש במודל המכוונן: {e}")

# לאחר סיום, אל תשכח למחוק את נקודת הקצה והמודל כדי למנוע עלויות מיותרות:
# endpoint.delete()
# tuned_model.delete()
```

### 6. המלצות כלליות

*   **התחל בקטן:** אל תנסה לאמן את המודל על אלפי דוגמאות מיד. התחל עם סט נתונים קטן אך איכותי.
*   **חזור על התהליך:** כוונון עדין הוא תהליך איטרטיבי. אמן, הערך, התאם נתונים או היפרפרמטרים, חזור על התהליך.
*   **ניטור:** עקוב בקפידה אחר מדדי האימון (הפסדים) והשתמש בסט נתוני אימות כדי למנוע התאמת יתר.
*   **הערכה:** תמיד בדוק את המודל המכוונן על נתונים שהוא *מעולם לא ראה* במהלך האימון כדי להעריך את יכולת ההכללה שלו.
*   **עלות:** זכור שכוונון עדין ופריסת נקודות קצה כרוכים בתשלום. קח זאת בחשבון בתקציב שלך.
*   **תיעוד:** תמיד עיין בתיעוד הרשמי של ספק ה-LLM. API ויכולות מתפתחים כל הזמן.
