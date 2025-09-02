### שאל את מודל Gemini

לצורך העבודה נדרש מפתח API.

מפתח API למודל ניתן לקבל כאן: [https://aistudio.google.com/](https://aistudio.google.com/)




```python
import google.generativeai as genai

class GoogleGenerativeAI:
    """
    מחלקה לאינטראקציה עם מודלי Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        אתחול מודל GoogleGenerativeAI.

        ארגומנטים:
            api_key (str): מפתח API לגישה למודל הגנרטיבי.
            model_name (str, optional): שם המודל לשימוש. ברירת מחדל "gemini-2.0-flash-exp".
        """
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        שולח שאילתת טקסט למודל ומחזיר את התשובה.

        ארגומנטים:
            q (str): השאלה שתישלח למודל.

        מחזיר:
            str: תשובה מהמודל.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"שגיאה: {str(ex)}"
```

### איך הקוד הזה עובד

1. **ייבוא ספרייה**: אנו מייבאים את ספריית `google.generativeai`, המספקת ממשק לאינטראקציה עם מודלי Google AI.

2. **מחלקה `GoogleGenerativeAI`**: מחלקה זו עוטפת את כל הלוגיקה לאינטראקציה עם מודל Gemini. היא מקבלת מפתח API ושם מודל כפרמטרים. כברירת מחדל נעשה שימוש במודל `gemini-2.0-flash-exp`.

3. **שיטת `__init__`**: בשיטה זו מתבצעת הגדרת המודל. אנו מעבירים את מפתח ה-API ואת שם המודל, ולאחר מכן מאתחלים את אובייקט המודל.

4. **שיטת `ask`**: שיטה זו שולחת שאילתת טקסט למודל ומחזירה את התשובה. אם משהו משתבש, השיטה תחזיר הודעת שגיאה.

### איך להשתמש?

```python
################################################################################
#                                                                              #
#             הכנס את מפתח ה-API שלך ל-GEMINI                                       #
#                                                                              #
################################################################################

API_KEY: str = input("מפתח API מ-`gemini`: ")
model = GoogleGenerativeAI(api_key=API_KEY)

q = input("שאלה: ")
response = model.ask(q)
print(response)
```

1. **הכנסת מפתח API**: תחילה, התוכנית מבקשת מהמשתמש מפתח API לגישה למודל Gemini. מפתח זה ניתן לקבל מאתר [Google AI Studio](https://aistudio.google.com/).

2. **יצירת אובייקט מודל**: אנו יוצרים אובייקט של המחלקה `GoogleGenerativeAI`, ומעבירים לו את מפתח ה-API.

3. **הכנסת שאלה**: המשתמש מכניס את השאלה שהוא רוצה לשאול את המודל.

4. **קבלת תשובה**: התוכנית שולחת את השאלה למודל ומציגה את התשובה על המסך.

### דוגמה לשימוש

יש לך מפתח API, ואתה רוצה לשאול את המודל: "איך לשפר את הקוד שלי?". כך זה ייראה:

```
מפתח API מ-`gemini`: המפתח_API_שלך
שאלה: איך לשפר את הקוד שלי?
תשובה: כדי לשפר את הקוד שלך, מומלץ לעקוב אחר עקרונות קוד נקי, כגון מתן שמות ברורים והגיוניים למשתנים ולפונקציות, שימוש בהערות להסברת לוגיקה מורכבת, ויישום עקרונות SOLID לתכנון מחלקות ומודולים.
```


הפעל את הקוד [כאן](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)
