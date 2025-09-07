# אימון מודל OpenAI לסיווג דפי אינטרנט

## מבוא

אימון מודל OpenAI לקבוע אם דף הוא חנות מקוונת.

- הכנת נתונים,
- טוקניזציה של טקסט,
- שליחת נתונים לאימון
- בדיקת מודל.

## שלב 1: הרשמה והגדרת OpenAI API

כדי להתחיל לעבוד עם OpenAI API, עליך להירשם לפלטפורמת OpenAI ולקבל מפתח API. מפתח זה ישמש לאימות בעת קריאה למתודות API.

```python
import openai

# הגדרת מפתח API
openai.api_key = 'המפתח-שלך'
```

## שלב 2: הכנת נתונים

כדי לאמן את המודל, עליך להכין סט נתונים שיכיל דוגמאות של דפי אינטרנט,
גם חנויות וגם לא חנויות.
כל רשומה צריכה לכלול את טקסט הדף ותווית מתאימה (`positive` לחנויות ו-`negative` ללא חנויות).

דוגמת קובץ JSON:

```json
[
    {
        "text": "<html><body><h1>ברוכים הבאים לחנות המקוונת שלנו</h1><p>אנו מציעים מגוון רחב של מוצרים במחירים תחרותיים. בקרו בחנות שלנו עוד היום!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>אודותינו</h1><p>אנו ספק מוביל של שירותים איכותיים. צרו קשר למידע נוסף.</p></body></html>",
        "label": "negative"
    }
]
```

## שלב 3: טוקניזציה של טקסט

לפני שליחת נתונים למודל OpenAI, יש לטוקן את הטקסט.
טוקניזציה היא תהליך פירוק טקסט למילים או אסימונים בודדים.
ב-Python ניתן להשתמש בספריות כמו NLTK, spaCy או tokenizers מספריית transformers.

דוגמת טוקניזציה באמצעות NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# דוגמת טקסט
text = "זוהי דוגמת טקסט לטוקניזציה."

# טוקניזציה של טקסט
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## שלב 4: שליחת נתונים לאימון

לאחר טוקניזציה של הטקסט, ניתן לשלוח את הנתונים לאימון מודל OpenAI.
הנה דוגמת קוד לשליחת נתונים:

```python
import openai

def train_model(data, positive=True):
    try:
        response = openai.Train.create(
            model="text-davinci-003",
            documents=[entry["text"] for entry in data],
            labels=["positive" if positive else "negative"] * len(data),
            show_progress=True
        )
        return response.id
    except Exception as ex:
        print("אירעה שגיאה במהלך האימון:", ex)
        return None

# דוגמת שימוש
data = [
    {"text": "טקסט של דף אינטרנט ראשון...", "label": "positive"},
    {"text": "טקסט של דף אינטרנט שני...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("ID משימה:", job_id)
```

## שלב 5: בדיקת מודל

לאחר אימון המודל, יש לבדוק אותו על סט נתונים לבדיקה.
הנה דוגמת קוד לבדיקה:

```python
import openai

def test_model(test_data):
    try:
        predictions = []
        for entry in test_data:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=entry["text"],
                max_tokens=1
            )
            prediction = response.choices[0].text.strip()
            predictions.append(prediction)
        return predictions
    except Exception as ex:
        print("אירעה שגיאה במהלך הבדיקה:", ex)
        return None

# דוגמת שימוש
test_data = [
    {"text": "טקסט של דף אינטרנט לבדיקה...", "label": "positive"},
    {"text": "טקסט של דף בדיקה אחר...", "label": "negative"}
]

predictions = test_model(test_data)
print("חיזויים:", predictions)
```

## שלב 6: טיפול בשגיאות ושיפור מודל

אם המודל נותן חיזויים שגויים, ניתן לשפר אותו על ידי
הוספת נתונים נוספים או שינוי פרמטרי אימון. ניתן גם להשתמש במשוב כדי לנתח שגיאות.

דוגמת טיפול בשגיאות:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"חיזוי שגוי לדף '{entry['name']}': חיזוי {pred}, בפועל {entry['label']}")

# דוגמת שימוש
handle_errors(predictions, test_data)
```