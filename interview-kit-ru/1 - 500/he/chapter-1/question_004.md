### `question_004.md`

**שאלה 4.** פייתון תומכת במספר סוגי נתונים, ומחרוזות הן אחד מסוגי הנתונים הנפוצים ביותר. איזו מהדרכים הבאות היא הדרך הנכונה לשרשר שלוש מחרוזות בפייתון, כך שהתוצאה תהיה מחרוזת אחת ללא רווחים נוספים ביניהן?

- A.  `"Python" + "is" + "awesome"`

- B.  `"Python", "is", "awesome"`

- C.  `"Python" + " " + "is" + " " + "awesome"`

- D.  `"Python".join(["is", "awesome"])`

**תשובה נכונה: A**

**הסבר:**

*   **אופרטור `+`:** בפייתון, האופרטור `+` משמש לשרשור מחרוזות. כאשר משתמשים ב-`+` בין מחרוזות, הן פשוט מחוברות למחרוזת אחת מבלי להוסיף תווים נוספים, אלא אם כן הם נוספו במפורש.
*   **פסיק `,`:** אם מחרוזות מופרדות בפסיקים, כמו באפשרות B, זה ייצור tuple של מחרוזות, ולא מחרוזת משורשרת.
*   **הוספת רווחים:** באפשרות C, רווחים מתווספים במפורש במהלך השרשור, מה שמוביל להכללת רווחים בין המילים.
*   **מתודת `join()`:** המתודה `join()` משמשת לחיבור איברים של אובייקט איטרבילי (כמו רשימה) למחרוזת אחת, תוך שימוש במחרוזת שעליה מופעלת המתודה כמפריד.

**דוגמה:**

```python
string1: str = "Python"
string2: str = "is"
string3: str = "awesome"

# שרשור נכון
concatenated_string_a: str = string1 + string2 + string3
print(f"A: {concatenated_string_a}")  # פלט: A: Pythonisawesome

# שרשור לא נכון עם tuple
concatenated_string_b: tuple[str, str, str] = (string1, string2, string3)
print(f"B: {concatenated_string_b}")  # פלט: B: ('Python', 'is', 'awesome')

# שרשור עם רווחים
concatenated_string_c: str = string1 + " " + string2 + " " + string3
print(f"C: {concatenated_string_c}")  # פלט: C: Python is awesome

# שימוש ב-join
concatenated_string_d: str = " ".join([string2, string3])
print(f"D: {string1}{concatenated_string_d}")  # פלט: D: Pythonis awesome
```

**לסיכום:**

*   אפשרות **A** `"Python" + "is" + "awesome"` מובילה לשרשור נכון של המחרוזות מבלי להוסיף רווחים ביניהן.

*   אפשרות **B** `"Python", "is", "awesome"` יוצרת tuple, לא מחרוזת.

*   אפשרות **C** `"Python" + " " + "is" + " " + "awesome"` מוסיפה רווחים בין המחרוזות, מה שלא עונה על דרישת השאלה.

*   אפשרות **D** `"Python".join(["is", "awesome"])` משתמשת ב-`join`, אך בדוגמה זו היא תוסיף רווח בין "is" ל-"awesome", ובנוסף יהיה צורך להוסיף את המחרוזת "Python" בהתחלה.

לכן, תשובה **A** היא הנכונה, מכיוון שהיא משרשרת במדויק את המחרוזות לאחת ללא רווחים נוספים.