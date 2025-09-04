## דף עזר. התאמה אישית של LLM: פרומפטים, כוונון עדין של מודלים, דוגמאות קוד.

במאמר זה:

1.  כיצד נוצר "אפקט הזיכרון" ב-LLM (סקירה קצרה).
2.  למה ומתי נדרש כוונון עדין (Fine-tuning) של מודל.
3.  מתי כוונון עדין אינו הפתרון הטוב ביותר.
4.  הכנת נתונים.
5.  דוגמאות לכוונון עדין עבור **OpenAI (GPT)**, **Google (Gemini)** ו-**Anthropic (Claude)** (שונה).

### 1. כיצד LLM "זוכר" ו"מתאים את עצמו": אשליית ההקשר

לפני שנדבר על כוונון עדין, חשוב להבין כיצד LLM מצליח ליצור תחושה של התאמה אישית.
זה חשוב כדי לא למהר לכוונון עדין יקר אם ניתן לפתור את המשימה בדרכים פשוטות יותר:

*   באמצעות **חלון הקשר (זיכרון לטווח קצר):** במסגרת דיאלוג אחד, אתה שולח למודל לא רק שאלה חדשה, אלא גם **את כל או חלק מההתכתבות הקודמת**. המודל מעבד את כל הטקסט הזה כ"הקשר" יחיד. בזכות זה הוא "זוכר" את ההערות הקודמות וממשיך את המחשבה. המגבלה כאן היא אורך חלון ההקשר (מספר הטוקנים).
*   חיבור **הוראות מערכת (System Prompt):** אתה יכול להגדיר למודל תפקיד, טון וכללי התנהגות בתחילת כל דיאלוג. לדוגמה: "אתה מומחה לפייתון, ענה בקצרה."
*   הכללת מספר דוגמאות להתנהגות רצויה בבקשה **למידה של מספר דוגמאות (Few-Shot Learning):** (זוגות קלט/פלט) מאפשרת למודל "ללמוד" דפוס זה ישירות במסגרת הבקשה הנוכחית.
*   **ניהול מצב בצד היישום:** הדרך החזקה ביותר. היישום (שפונה ל-API) יכול לאחסן מידע על המשתמש (העדפות, היסטוריה, נתוני פרופיל) ולהוסיף אותו באופן דינמי לפרומפט לפני שליחתו למודל.

### 2.

כוונון עדין הוא תהליך של אימון נוסף של LLM בסיסי שכבר הוכן על בסיס נתוני הקלט הספציפיים שלך. זה מאפשר למודל:

*   **להתאים סגנון וטון:** המודל ידבר "בשפה שלך" – בין אם זה סגנון מדעי קפדני, שיווקי ידידותי או סלנג של קהילה מסוימת.
*   **לפעול לפי הוראות ופורמטים ספציפיים:** אם אתה זקוק לתשובות במבנה JSON מוגדר בקפדנות, או תמיד עם קבוצה ספציפית של שדות.
*   **להבין שפה ספציפית לתחום:** אימון על התיעוד הפנימי שלך או טקסטים תעשייתיים יעזור למודל להתמודד טוב יותר עם הטרמינולוגיה של הנישה שלך.
*   **לשפר ביצועים במשימות צרות:** עבור סוגים מסוימים של שאילתות (לדוגמה, סיווג סנטימנטים, יצירת קוד במסגרת ספציפית), כוונון עדין יכול לספק תשובות מדויקות ורלוונטיות יותר מאשר המודל הבסיסי.
*   **לקצר את אורך הפרומפטים:** אם המודל כבר "יודע" את ההתנהגות הרצויה בזכות הכוונון, אינך צריך להזכיר לו זאת בכל פעם בפרומפט, מה שחוסך טוקנים ומפחית את זמן ההשהיה.

### 3.

כוונון עדין הוא כלי חזק אך לא אוניברסלי. אין להשתמש בו אם:

*   **המודל צריך לגשת לידע חדש:** כוונון עדין משנה את משקלי המודל, אך הוא אינו "טוען" לתוכו עובדות חדשות בזמן אמת. אם המשימה שלך היא לענות על שאלות המבוססות על בסיס ידע המשתנה ללא הרף (מסמכי חברה, חדשות אחרונות), עדיף להשתמש ב-**Retrieval Augmented Generation (RAG)**. כאן, המודל הבסיסי מקבל הקשר ממאגר הנתונים שלך *במהלך ביצוע השאילתה*.
*   **משימה פשוטה ניתנת לפתרון באמצעות הנדסת פרומפטים:** התחל תמיד עם הנדסת פרומפטים היעילה ביותר. אם ניתן לפתור את המשימה באמצעות הוראות פשוטות ודוגמאות של מספר דוגמאות, כוונון עדין מיותר ויקר יותר.
*   **אין לך מספיק נתונים באיכות גבוהה:** נתונים גרועים = מודל מכוונן גרוע.

### 4. הכנת נתונים.

איכות וכמות הנתונים שלך קריטיות. המודל לומד מהדוגמאות שלך, ולכן הן חייבות להיות מדויקות, מגוונות ועקביות.

*   **פורמט:** לרוב JSON Lines (<code>.jsonl</code>) או CSV (<code>.csv</code>).
*   **מבנה נתונים:** תלוי במשימה.
    *   **כוונון הוראות (Instruction Tuning - הוראה-תגובה):** מתאים למשימות כלליות כגון שאלות-תשובות, ניסוח מחדש, סיכום.
        ```json
        {"input_text": "נסח מחדש את המשפט: 'טכנולוגיית AI מתפתחת במהירות.'", "output_text": "בינה מלאכותית מפגינה התקדמות מהירה."}
        {"input_text": "ציין את בירת צרפת.", "output_text": "בירת צרפת היא פריז."}
        ```
    *   **כוונון צ'אט (Chat Tuning - צ'אט):** אידיאלי לאימון המודל לנהל דיאלוג בתפקיד או סגנון ספציפי.
        ```json
        {"messages": [{"author": "user", "content": "היי! מה אתה ממליץ לארוחת ערב?"}, {"author": "model", "content": "ערב טוב! היום הוא יום נהדר לפסטה קרבונרה, או, אם אתה מעדיף משהו קל, סלט קיסר."}]}
        {"messages": [{"author": "user", "content": "ספר לי על תכונות חדשות בפייתון 3.12."}, {"author": "model", "content": "בפייתון 3.12 הוצגו f-strings עם הזחה, תחביר חדש לגנריות אוניברסליות וטיפול משופר בשגיאות Unicode."}]}
        ```
*   **כמות:** מינימום 100-200 דוגמאות איכותיות, אך ככל שיותר, כך טוב יותר (אלפים למשימות רציניות).
*   **איכות:** דיוק, עקביות בסגנון, בטון ובפורמט בכל מערך הנתונים.

### 5. מודלים ופלטפורמות

#### 5.1. OpenAI

OpenAI מספקת API פשוט ואינטואיטיבי למדי לכוונון עדין.

**תהליך:**

1.  הכנת נתונים בפורמט JSONL, כאשר כל שורה היא אובייקט עם מערך <code>messages</code> (כמו ב-Chat Completions API).
2.  העלאת קובץ הנתונים באמצעות API.
3.  יצירת משימת כוונון עדין, תוך ציון הקובץ שהועלה והמודל הבסיסי.
4.  מעקב אחר ההתקדמות.
5.  שימוש במודל החדש, המכוונן, לפי ה-ID שלו.

**דוגמת נתונים (קובץ <code>training_data.jsonl</code>):**

```json
{"messages": [{"role": "system", "content": "אתה עוזר ידידותי לתמיכת לקוחות של חברת IT."}, {"role": "user", "content": "האינטרנט שלי לא עובד."}, {"role": "assistant", "content": "אוי, אני מתנצל על אי הנוחות! בואו ננסה להבין. איך אתה מחובר לאינטרנט – באמצעות Wi-Fi או כבל?"}]}
{"messages": [{"role": "system", "content": "אתה עוזר ידידותי לתמיכת לקוחות של חברת IT."}, {"role": "user", "content": "איך אני יכול לאפס את הסיסמה שלי?"}, {"role": "assistant", "content": "בטח! כדי לאפס את הסיסמה שלך, אנא עבור לדף הכניסה ולחץ על 'שכחת סיסמה?' מתחת לשדה הקלט. לאחר מכן עקוב אחר ההוראות שעל המסך."}]
```

**דוגמת קוד Python:**

התקן מראש: <code>pip install openai</code>

```python
import openai
from openai import OpenAI
import os

# הגדר את מפתח ה-API של OpenAI שלך. מומלץ להשתמש במשתנה סביבה.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. העלאת קובץ נתונים
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"קובץ הועלה בהצלחה. מזהה קובץ: {file_id}")
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
    print(f"משימת כוונון עדין נוצרה. מזהה משימה: {job_id}")
    print("עקוב אחר סטטוס המשימה באמצעות API או ב-OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"שגיאת יצירת משימה: {e.status_code} - {e.response}")
    exit()

# דוגמה למעקב אחר סטטוס וקבלת שם המודל (להפעלה לאחר יצירת המשימה):
# # job_id = "ftjob-..." # החלף במזהה המשימה שלך
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"סטטוס המשימה הנוכחי: {job_status.status}")
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

Anthropic **אינה מספקת API ציבורי לכוונון עדין של מודלי Claude 3 שלה (Opus, Sonnet, Haiku) באותו מובן כמו OpenAI או Google.**

Anthropic מתמקדת ביצירת מודלי בסיס חזקים מאוד, שלטענתם, עובדים מצוין עם הנדסת פרומפטים מתקדמת ודפוסי RAG, וממזערים את הצורך בכוונון עדין ברוב המקרים.
עבור לקוחות ארגוניים גדולים או שותפים, ייתכנו תוכניות ליצירת מודלים "מותאמים אישית" או אינטגרציות מיוחדות, אך זו אינה פונקציית כוונון עדין זמינה לציבור באמצעות API.

אם אתה עובד עם Claude 3, ההתמקדות העיקרית שלך צריכה להיות ב:

*   **הנדסת פרומפטים באיכות גבוהה:** התנסה בהוראות מערכת, דוגמאות של מספר דוגמאות, עיצוב ברור של בקשות. Claude ידוע ביכולתו לציית בקפדנות להוראות, במיוחד בתגי XML.
*   **מערכות RAG:** השתמש במאגרי ידע חיצוניים כדי לספק למודל הקשר רלוונטי.

#### 5.3. Google (Gemini)

גוגל מפתחת באופן פעיל יכולות כוונון עדין באמצעות פלטפורמת **Google Cloud Vertex AI** שלה.
זוהי פלטפורמת ML מלאה המספקת כלים להכנת נתונים, הפעלת משימות אימון ופריסת מודלים.
כוונון עדין זמין עבור מודלים ממשפחת Gemini.

**תהליך:**

1.  הכנת נתונים (JSONL או CSV) בפורמט `input_text`/`output_text` (לכוונון הוראות) או `messages` (לכוונון צ'אט).
2.  העלאת נתונים ל-Google Cloud Storage (GCS).
3.  יצירה והפעלה של משימת כוונון עדין באמצעות Vertex AI Console או SDK.
4.  פריסת המודל המכוונן לנקודת קצה (Endpoint).
5.  שימוש במודל המכוונן באמצעות נקודת קצה זו.

**דוגמת נתונים (קובץ <code>gemini_tuning_data.jsonl</code>):**

```json
{"input_text": "סכם את הרעיונות העיקריים של ספר זה: 'הספר מספר על מסעו של גיבור המתגבר על מכשולים ומוצא את עצמו.'", "output_text": "הדמות הראשית של הספר יוצאת למסע טרנספורמטיבי, מתמודדת עם אתגרים ומשיגה גילוי עצמי."}
{"input_text": "הסבר את עקרון הפעולה של כור תרמו-גרעיני במילים פשוטות.", "output_text": "כור תרמו-גרעיני מנסה לשחזר את התהליך המתרחש בשמש: מיזוג גרעיני אטום קלים בטמפרטורות גבוהות מאוד, תוך שחרור כמויות עצומות של אנרגיה."}
```

**דוגמת קוד Python (דורש <code>google-cloud-aiplatform</code>):**

התקן מראש: <code>pip install google-cloud-aiplatform</code> ו-<code>pip install google-cloud-storage</code>

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- הגדרות ---
# החלף בערכים שלך:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # בחר אזור התומך ב-Gemini וב-Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # שם דלי ה-GCS שלך (חייב להיווצר מראש)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- סוף הגדרות ---

# אתחול Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. יצירת קובץ נתונים (אם אינו קיים)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "סכם את הרעיונות העיקריים של ספר זה: \'הספר מספר על מסעו של גיבור המתגבר על מכשולים ומוצא את עצמו.\'", "output_text": "הדמות הראשית של הספר יוצאת למסע טרנספורמטיבי, מתמודדת עם אתגרים ומשיגה גילוי עצמי."}\n')
    f.write('{"input_text": "הסבר את עקרון הפעולה של כור תרמו-גרעיני במילים פשוטות.", "output_text": "כור תרמו-גרעיני מנסה לשחזר את התהליך המתרחש בשמש: מיזוג גרעיני אטום קלים בטמפרטורות גבוהות מאוד, תוך שחרור כמויות עצומות של אנרגיה."}\n')
print(f"קובץ נתונים '{DATA_FILE_LOCAL_PATH}' נוצר.")


# 2. העלאת נתונים ל-Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """מעלה קובץ לדלי GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"קובץ '{source_file_name}' הועלה ל-'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"שגיאת העלאת קובץ ל-GCS. ודא שהדלי קיים ויש לך הרשאות: {e}")
    exit()

# 3. יצירה והפעלה של משימת כוונון עדין
print(f"\nהפעלת כוונון עדין של מודל '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` מפעיל את המשימה ומחזיר את המודל המכוונן לאחר השלמתו
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # מודל בסיס Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # מספר שלבי אימון. הערך האופטימלי תלוי בגודל הנתונים.
        # batch_size=16, # ניתן לציין
        # learning_rate_multiplier=1.0 # ניתן לציין
    )
    print(f"מודל '{TUNED_MODEL_DISPLAY_NAME}' כוונן בהצלחה. מזהה מודל: {tuned_model.name}")
    print("תהליך הכוונון העדין עשוי לקחת זמן משמעותי.")
except Exception as e:
    print(f"שגיאת כוונון עדין. בדוק את היומנים ב-Vertex AI Console: {e}")
    exit()

# 4. פריסת המודל המכוונן (לשימוש)
print(f"\nפריסת המודל המכוונן '{TUNED_MODEL_DISPLAY_NAME}' לנקודת הקצה...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # סוג מכונה עבור נקודת הקצה. בחר את המתאים.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"מודל נפרס לנקודת הקצה: {endpoint.name}")
    print("הפריסה עשויה גם היא לקחת מספר דקות.")
except Exception as e:
    print(f"שגיאת פריסת מודל: {e}")
    exit()

# 5. שימוש במודל המכוונן
print("\nבדיקת המודל המכוונן...")
prompt = "ספר לי על היכולות שלך לאחר האימון."
instances = [{"prompt": prompt}] # לכוונון הוראות. אם כוונון צ'אט, אז {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nתגובת המודל המכוונן:")
    print(response.predictions[0])
except Exception as e:
    print(f"שגיאה בשימוש במודל המכוונן: {e}")

# לאחר סיום העבודה, אל תשכח למחוק את נקודת הקצה ואת המודל כדי למנוע עלויות מיותרות:
# endpoint.delete()
# tuned_model.delete()

```