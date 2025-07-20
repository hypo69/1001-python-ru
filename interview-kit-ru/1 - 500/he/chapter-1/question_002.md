### `question_002.md`

**שאלה 2.** בפייתון, לולאת `for` גמישה מאוד ומאפשרת לעבור על אובייקטים איטרביליים שונים. נניח שיש לכם מילון עם מפתחות מסוג מחרוזת וערכים מסוג מספר שלם. איזו מהאפשרויות הבאות מבצעת איטרציה נכונה הן על המפתחות והן על הערכים של המילון?

- A. `for key, value in dictionary.items(): print(key, value)`

- B. `for key in dictionary: print(key, dictionary[key])`

- C. `for value in dictionary.values(): print(value)`

- D. `for key in dictionary.keys(): print(key)`

**תשובה נכונה: A**

**הסבר:**

*   **מתודת `items()`:** מתודת המילון `items()` מחזירה *view object* המציג רשימה של זוגות מפתח-ערך כטאפלים (tuples). זה מאפשר לעבור בו-זמנית על המפתחות והערכים בלולאת `for`.

*   **מתודת `keys()`:** מתודת `keys()` מחזירה *view object* המכיל רק את המפתחות של המילון.

*   **מתודת `values()`:** מתודת `values()` מחזירה *view object* המכיל רק את הערכים של המילון.

**דוגמה:**

```python
my_dictionary: dict[str, int] = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# איטרציה נכונה על מפתחות וערכים:
print("איטרציה באמצעות items():")
for key, value in my_dictionary.items():
    print(f"מפתח: {key}, ערך: {value}")
# פלט:
# איטרציה באמצעות items():
# מפתח: apple, ערך: 1
# מפתח: banana, ערך: 2
# מפתח: cherry, ערך: 3

# איטרציה על מפתחות באמצעות dictionary[key]:
print("\nאיטרציה על מפתחות באמצעות dictionary[key]:")
for key in my_dictionary:
    print(f"מפתח: {key}, ערך: {my_dictionary[key]}")
# פלט:
# איטרציה על מפתחות באמצעות dictionary[key]:
# מפתח: apple, ערך: 1
# מפתח: banana, ערך: 2
# מפתח: cherry, ערך: 3

# איטרציה רק על ערכים:
print("\nאיטרציה רק על ערכים:")
for value in my_dictionary.values():
    print(f"ערך: {value}")
# פלט:
# איטרציה רק על ערכים:
# ערך: 1
# ערך: 2
# ערך: 3

# איטרציה רק על מפתחות:
print("\nאיטרציה רק על מפתחות:")
for key in my_dictionary.keys():
    print(f"מפתח: {key}")
# פלט:
# איטרציה רק על מפתחות:
# מפתח: apple
# מפתח: banana
# מפתח: cherry
```

**לסיכום:**

*   אפשרות **A** `for key, value in dictionary.items(): print(key, value)` מבצעת איטרציה נכונה על זוגות "מפתח-ערך" של המילון באמצעות מתודת `items()`.

*   אפשרות **B** `for key in dictionary: print(key, dictionary[key])` עובדת, אך היא משתמשת בגישה ישירה לערך דרך המפתח במילון, ולא מבצעת איטרציה על טאפלים של (key, value).

*   אפשרויות **C** ו-**D** מבצעות איטרציה או רק על הערכים, או רק על המפתחות.

לכן, תשובה **A** היא הנכונה, מכיוון שהיא מאפשרת גישה בו-זמנית גם למפתחות וגם לערכים בלולאת `for`.