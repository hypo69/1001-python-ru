# BANNER AI
מודל Gemini מחזיר את התשובה כבאנר ASCII בהתאם להוראה שניתנה לו.

 התוכנית מקיימת אינטראקציה עם מודל Google Generative AI ליצירת באנרים טקסטואליים.
 המשתמש יכול לבחור את סגנון עיצוב הבאנר ולשלוח טקסט למודל לעיבוד.

## התקנת תלויות
כדי להריץ את הקוד במחשב מקומי, תידרש התקנת ספריות גוגל.

```python
pip install google
pip install google-generativeai
```

אני ממליץ בחום לבצע את כל הניסויים בסביבה וירטואלית.


## תכונות קוד בתוכנית זו
1. הוראות נשמרות בקבצים שונים ונטענות לפי הצורך.
2. החל מדוגמה זו, אני שומר את מפתח המודל במשתנה סביבה, מה שחוסך לי את הצורך להזין את המפתח שוב ושוב.
3. אני משתמש בנתיבים מוחלטים לקבצים.
    כדי לקבוע את ספריית השורש של הפרויקט, אני מחפש באופן רקורסיבי כלפי מעלה קבצי סמן ('pyproject.toml', 'requirements.txt', '.git').
    את הספרייה שנמצאה אני שומר במשתנה __root__. ממנה, אני בונה את הנתיב להוראות המערכת:
    ``python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
    base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__
    ``


### 1. **ייבוא ספריות נחוצות**
```python
import google.generativeai as genai  # ייבוא ספרייה לעבודה עם Gemini
import re  # ייבוא ספרייה לעבודה עם ביטויים רגולריים
from pathlib import Path  # ייבוא לעבודה עם נתיבי מערכת קבצים
from header import __root__  # ייבוא אובייקט __root__, המכיל את הנתיב המוחלט לשורש הפרויקט
from dotenv import load_dotenv, set_key  # ייבוא פונקציות לעבודה עם משתני סביבה
import os  # ייבוא לעבודה עם משתני סביבה
```

- **`google.generativeai`**: משמש לאינטראקציה עם ה-API של Google Generative AI.
- **`re`**: ספרייה לעבודה עם ביטויים רגולריים (לא בשימוש בקוד זה, אך עשויה להיות שימושית בעתיד).
- **`Path`**: מאפשר עבודה עם נתיבי מערכת קבצים.
- **`__root__`**: אובייקט המכיל את הנתיב המוחלט לשורש הפרויקט.
- **`dotenv`**: מאפשר טעינת משתני סביבה מקובץ `.env` ושמירתם.
- **`os`**: משמש לעבודה עם משתני סביבה.

---

### 2. **טעינת משתני סביבה**
```python
load_dotenv()
```
- הפונקציה `load_dotenv()` טוענת משתני סביבה מקובץ `.env`, אם הוא קיים.

---

### 3. **מחלקה `GoogleGenerativeAI`**
המחלקה מיועדת לאינטראקציה עם מודל Google Generative AI.

#### 3.1. **תכונות מחלקה**
```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```
- רשימת מודלי Google Generative AI זמינים.

#### 3.2. **שיטת `__init__`**
```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    אתחול מודל GoogleGenerativeAI.

    :param api_key: מפתח API לגישה ל-Gemini.
    :type api_key: str
    :param system_instruction: הוראה למודל (הנחיית מערכת).
    :type system_instruction: str
    :param model_name: שם מודל Gemini לשימוש. ברירת מחדל 'gemini-2.0-flash-exp'.
    :type model_name: str
    """
    self.api_key = api_key
    self.model_name = model_name
    genai.configure(api_key=self.api_key)  # הגדרת הספרייה עם מפתח ה-API
    self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # אתחול המודל עם ההוראה
```
- **`api_key`**: מפתח API לגישה ל-Google Generative AI.
- **`system_instruction`**: הוראה למודל (לדוגמה, סגנון עיצוב טקסט).
- **`model_name`**: שם המודל, ברירת המחדל היא `'gemini-2.0-flash-exp'`.
- **`genai.configure(api_key=self.api_key)`**: הגדרת הספרייה באמצעות מפתח ה-API.
- **`genai.GenerativeModel(...)`**: אתחול המודל עם הפרמטרים שצוינו.

#### 3.3. **שיטת `ask`**
```python
def ask(self, q: str) -> str:
    """
    שולח בקשה למודל ומקבל תשובה.

    :param q: טקסט הבקשה.
    :type q: str
    :return: תשובת המודל או הודעת שגיאה.
    :rtype: str
    """
    try:
        response = self.model.generate_content(q)  # שליחת בקשה למודל
        return response.text  # קבלת תשובת טקסט
    except Exception as ex:
        return f'שגיאה: {str(ex)}'  # טיפול וקבלת שגיאה
```
- **`q`**: טקסט הבקשה הנשלח למודל.
- **`self.model.generate_content(q)`**: שליחת הבקשה למודל.
- **`response.text`**: קבלת תשובת הטקסט מהמודל.
- **`except Exception as ex`**: טיפול בשגיאות והחזרת הודעת שגיאה.

---

### 4. **החלק העיקרי של התוכנית**
```python
if __name__ == '__main__':
```
- בדיקה שהתוכנית מופעלת כסקריפט עצמאי.

#### 4.1. **הגדרת נתיבים**
```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__
```
- **`relative_path`**: נתיב יחסי לספרייה בתוך הפרויקט.
- **`base_path`**: נתיב מוחלט, המתקבל על ידי שילוב `__root__` ו-`relative_path`.

#### 4.2. **קריאת מפתח API**
```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('מפתח API לא נמצא. הכנס מפתח API מ-`gemini`: ')  # בקשת מפתח API מהמשתמש
    set_key('.env', 'API_KEY', API_KEY)  # שמירת מפתח לקובץ .env
```
- **`os.getenv('API_KEY')`**: מנסה לקבל את מפתח ה-API ממשתני הסביבה.
- אם המפתח לא נמצא, הוא מבקש אותו מהמשתמש באמצעות `input`.
- **`set_key('.env', 'API_KEY', API_KEY)`**: שומר את המפתח שהוזן לקובץ `.env` לשימוש עתידי.

#### 4.3. **הוראות למודל**
```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- מילון המכיל את שמות הקבצים עם הוראות למודל.

#### 4.4. **ברכת המשתמש**
```python
print('ברוך הבא למשחק באנר!')
print('הכנס טקסט, ואני אצור עבורך באנר טקסטואלי.')
```
- מברך את המשתמש ומסביר את פונקציונליות התוכנית.

#### 4.5. **לולאה לבחירת סגנון באנר**
```python
while True:
    print('בחר סגנון עיצוב באנר:')
    print('1. סימן \'*\'')
    print('2. סימן \'~\'')
    print('3. סימן \'#\'')
    choice = input('הכנס מספר סגנון (1, 2 או 3): ')
```
- המשתמש בוחר את סגנון עיצוב הבאנר.

#### 4.6. **קריאת הוראות למודל**
```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # קריאת הוראה מקובץ
else:
    print('בחירה לא חוקית. נעשה שימוש בסגנון ברירת מחדל \'*\'')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # קריאת הוראת ברירת מחדל
```
- אם הבחירה תקינה, קוראים את ההוראה המתאימה מהקובץ.
- אם הבחירה לא תקינה, משתמשים בהוראת ברירת המחדל.

#### 4.7. **יצירת מופע מחלקה**
```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- יוצרים מופע של המחלקה `GoogleGenerativeAI` עם הפרמטרים שצוינו.

#### 4.8. **בקשת טקסט מהמשתמש**
```python
user_text: str = input('הכנס טקסט לבאנר: ')
```
- המשתמש מכניס טקסט לבאנר.

#### 4.9. **אימות טקסט**
```python
if user_text.strip() == '':
    print('לא הכנסת טקסט. נסה שוב.')
else:
    response = model.ask(user_text)
    print('\nהבאנר שלך מוכן:')
    print(response)
```
- אם הטקסט ריק, מציגים הודעת שגיאה.
- אם הוזן טקסט, שולחים אותו למודל ומציגים את התוצאה.

```