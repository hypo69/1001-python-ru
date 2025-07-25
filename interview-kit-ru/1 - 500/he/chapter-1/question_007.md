### `question_007.md`
**שאלה 7.** בעת יצירת פונקציה בפייתון המחזירה עצרת של מספר באמצעות רקורסיה, איזו מהגדרות הפונקציה הבאות ממומשת נכון ועומדת בעקרונות הרקורסיה?

- A
```python
def factorial(n): 
    return n * factorial(n-1) if n > 1 else 1
```

- B
```python
def factorial(n): return factorial(n-1) * n if n == 0 else 1
```

- C
```python
def factorial(n): 
    factorial(n-1) * n
```

- D
```python
def factorial(n): 
    return n * factorial(n) if n > 1 else 1
    
```

**תשובה נכונה: A**

**הסבר:**

*   **פונקציה רקורסיבית:** פונקציה רקורסיבית היא פונקציה שקוראת לעצמה. חלק חשוב בפונקציה רקורסיבית הוא קיומו של **תנאי עצירה** (base case), שעוצר את הרקורסיה, ו**מקרה רקורסיבי**, שקורא לפונקציה עם קלט שונה כדי להתקרב לתנאי העצירה.

*   **עצרת:** עצרת של מספר `n` (מסומנת כ-`n!`) היא מכפלת כל המספרים הטבעיים עד `n`. לדוגמה, `5! = 5 * 4 * 3 * 2 * 1 = 120`.

*   **מימוש נכון של רקורסיה:**
    *   **תנאי עצירה:** עבור עצרת, תנאי העצירה הוא `n = 1` (או `n <= 1`, כולל `0!`). במקרה זה, העצרת שווה ל-1.
    *   **מקרה רקורסיבי:** עבור `n > 1`, העצרת מחושבת כ-`n * factorial(n-1)`, כלומר, המספר הנוכחי מוכפל בעצרת של המספר הקטן ממנו באחד.
*   **בדיקת התנאי:** חשוב שהקריאה `factorial(n-1)` תתבצע רק כאשר `n>1`, אחרת תיווצר רקורסיה אינסופית.

**דוגמה:**

```python
def factorial(n: int) -> int:
    if n > 1:
      return n * factorial(n-1)
    else:
      return 1


print(f"factorial(5): {factorial(5)}") # פלט: factorial(5): 120

print(f"factorial(0): {factorial(0)}") # פלט: factorial(0): 1

print(f"factorial(1): {factorial(1)}") # פלט: factorial(1): 1
```

**לסיכום:**

*   אפשרות **A** `def factorial(n): return n * factorial(n-1) if n > 1 else 1` מממשת נכון את הפונקציה הרקורסיבית לחישוב עצרת, עם תנאי עצירה נכון וקריאה רקורסיבית נכונה.
*   אפשרות **B** `def factorial(n): return factorial(n-1) * n if n == 0 else 1` מכילה תנאי עצירה שגוי שלא יטפל בערכים חיוביים של n.
*   אפשרות **C** `def factorial(n): factorial(n-1) * n` חסרה תנאי עצירה ואינה מחזירה ערך, מה שיוביל לרקורסיה אינסופית ולשגיאה.
*   אפשרות **D** `def factorial(n): return n * factorial(n) if n > 1 else 1` גורמת לרקורסיה אינסופית, מכיוון שהיא קוראת לעצרת עם אותו המספר במקום `n-1`.

לכן, תשובה **A** היא הנכונה, מכיוון שהיא מכילה הגדרה נכונה של פונקציה רקורסיבית, עם תנאי עצירה וצעד רקורסיבי שמקטין את הקלט ומקרב אותו לתנאי העצירה.