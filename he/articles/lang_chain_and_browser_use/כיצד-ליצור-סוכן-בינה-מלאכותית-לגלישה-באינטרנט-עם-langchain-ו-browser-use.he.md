## כיצד ליצור סוכן בינה מלאכותית לגלישה באינטרנט באמצעות LangChain ו-Browser-Use: מדריך צעד אחר צעד

מדריך זה צעד אחר צעד יראה לך כיצד ליצור סוכן בינה מלאכותית המסוגל לחפש מידע בגוגל ולנתח דפי אינטרנט באמצעות LangChain ו-Browser-Use.

**שלב 1: התקנת ספריות נחוצות**

ראשית, עליך להתקין את ספריות הפייתון הנחוצות. פתח טרמינל או שורת פקודה והפעל את הפקודה הבאה:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**שלב 2: הגדרת מפתחות API**

נדרשים מפתחות API לעבודה עם OpenAI ו-SerpAPI.

* **מפתח API של OpenAI:** קבל את מפתח ה-API שלך מאתר OpenAI (openai.com).
* **מפתח API של SerpAPI:** SerpAPI מספקת API לעבודה עם תוצאות חיפוש. הירשם לאתר serpapi.com (קיימת גרסת ניסיון חינם), היכנס לחשבונך ומצא את מפתח ה-API שלך בדף לוח המחוונים.

צור קובץ `.env` באותה תיקייה שבה ימוקם סקריפט הפייתון שלך, והוסף לשם את המפתחות בפורמט הבא:

```
OPENAI_API_KEY=המפתח_שלך_openai
SERPAPI_API_KEY=המפתח_שלך_serpapi
```

**שלב 3: יצירת סקריפט פייתון (browser_agent.py)**

צור את הקובץ `browser_agent.py` והכנס לתוכו את הקוד הבא:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# הגדרת רישום
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# טעינת מפתחות API מקובץ .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # אתחול מודל השפה
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # ניתן לנסות מודלים אחרים

    # הגדרת כלי החיפוש (דוגמה פשוטה, ללא חיפוש גוגל בפועל)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"מחפש בגוגל: {query}",  # החלף בחיפוש אמיתי באמצעות SerpAPI במידת הצורך
        description="מחפש מידע בגוגל."
    )


    # הגדרת המשימה עבור הסוכן
    task = """
    מצא את החדשות האחרונות על חברת OpenAI בגוגל.
    לאחר מכן בקר באחד האתרים שנמצאו ומצא את שמות המייסדים.
    """

    # יצירת הסוכן
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # הפעלת הסוכן
    try:
        result = await agent.arun(task)
        print(f"תוצאה: {result}")
    except Exception as e:
        logging.error(f"אירעה שגיאה: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**שלב 4: הפעלת הסוכן**

פתח טרמינל או שורת פקודה, נווט לתיקייה עם הקובץ `browser_agent.py` והפעל אותו:

```bash
python browser_agent.py
```

**שלב 5: שיפור הסוכן (תכונות מתקדמות)**

* **חיפוש גוגל אמיתי:** החלף את פונקציית `lambda` ב-`search_tool` בקוד המשתמש ב-SerpAPI לחיפושי גוגל אמיתיים. זה ידרוש לימוד תיעוד SerpAPI.

* **אינטראקציה עם דפי אינטרנט (Browser-Use):** כדי להוסיף פונקציונליות של אינטראקציה עם דפי אינטרנט (פתיחת קישורים, חילוץ טקסט וכו'), תצטרך להשתמש בספריית `browser-use`. התיעוד של ספרייה זו יעזור לך להוסיף את הכלים המתאימים לסוכן שלך.

* **שימוש בזיכרון:** ניתן להשתמש במנגנוני הזיכרון של LangChain כדי לשמר הקשר בין בקשות.

* **שרשרות פעולה מורכבות יותר:** LangChain מאפשרת ליצור שרשרות פעולה מורכבות יותר לפתרון משימות מורכבות יותר.


דוגמה זו מדגימה את המבנה הבסיסי. כדי ליישם סוכן מלא המקיים אינטראקציה עם דפדפן וחיפוש גוגל, תידרש עבודה נוספת עם SerpAPI ו-`browser-use`. אל תשכח לעיין בתיעוד של ספריות אלו למידע מפורט יותר.
