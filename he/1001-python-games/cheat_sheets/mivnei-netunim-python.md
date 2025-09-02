**1. רשימות (Lists)**

*   **הגדרה:** רשימות בפייתון הן אוספים מסודרים וניתנים לשינוי של פריטים. זה אומר שאתה יכול להוסיף, למחוק ולשנות פריטים ברשימה, וסדר הפריטים חשוב.
*   **ייצוג:** רשימות נוצרות באמצעות סוגריים מרובעים `[]`, ופריטים מופרדים בפסיקים.

*   **דוגמאות:**

    ```python
    # יצירת רשימה
    boris_list = ["בוריס", "מוסקבה", 30, "מהנדס"]
    print(f"יצירת רשימה: {boris_list}")

    # גישה לפי אינדקס
    print(f"פריט באינדקס 0: {boris_list[0]}")

    # שינוי פריט
    boris_list[2] = 31
    print(f"שינוי פריט: {boris_list}")

    # הוספת פריט לסוף
    boris_list.append("נשוי")
    print(f"הוספה לסוף: {boris_list}")

    # הוספת פריט לפי אינדקס
    boris_list.insert(1, "רוסיה")
    print(f"הוספת פריט: {boris_list}")

    # מחיקת פריט לפי ערך
    boris_list.remove("מהנדס")
    print(f"מחיקת פריט לפי ערך: {boris_list}")

    # מחיקת פריט לפי אינדקס
    del boris_list[2]
    print(f"מחיקת פריט לפי אינדקס: {boris_list}")

    # הרחבת רשימה עם רשימה אחרת
    boris_list.extend(["תחביב", "דיג"])
    print(f"הרחבת רשימה: {boris_list}")

    # מחיקת פריט מהסוף
    boris_list.pop()
    print(f"מחיקת פריט מהסוף: {boris_list}")

    ```

**2. מילונים (Dictionaries)**

*   **הגדרה:** מילונים בפייתון הם אוספים לא מסודרים של פריטים, כאשר כל פריט מורכב מזוג "מפתח-ערך".
*   **ייצוג:** מילונים נוצרים באמצעות סוגריים מסולסלים `{}`, וזוגות "מפתח-ערך" מופרדים בנקודתיים `:`.

*   **דוגמאות:**
    ```python
    # יצירת מילון
    alice_dict = {"name": "אליס", "age": 25, "city": "לונדון", "occupation": "אמנית"}
    print(f"יצירת מילון: {alice_dict}")

    # גישה לפי מפתח
    print(f"ערך עבור מפתח 'name': {alice_dict['name']}")

    # שינוי ערך
    alice_dict["age"] = 26
    print(f"שינוי ערך: {alice_dict}")

    # הוספת זוג מפתח-ערך
    alice_dict["hobby"] = "ציור"
    print(f"הוספת זוג: {alice_dict}")

    # מחיקת זוג לפי מפתח
    del alice_dict["city"]
    print(f"מחיקת זוג: {alice_dict}")

    # מחיקת זוג באמצעות שיטת pop (עם ערך מוחזר)
    hobby = alice_dict.pop("hobby")
    print(f"מחיקה עם ערך מוחזר: {alice_dict}, ערך: {hobby}")

    # בדיקת קיום מפתח
    print(f"מפתח 'name' קיים: {'name' in alice_dict}")
    ```

**3. טאפלים (Tuples)**

*   **הגדרה:** טאפלים בפייתון הם אוספים מסודרים ו**בלתי ניתנים לשינוי** של פריטים.
*   **ייצוג:** טאפלים נוצרים באמצעות סוגריים עגולים `()`, ופריטים מופרדים בפסיקים.

*   **דוגמאות:**

    ```python
    # יצירת טאפל
    boris_tuple = ("בוריס", "מוסקבה", 30, "מהנדס")
    print(f"יצירת טאפל: {boris_tuple}")

    # גישה לפי אינדקס
    print(f"פריט באינדקס 2: {boris_tuple[2]}")

    # לא ניתן לשנות פריט
    # boris_tuple[0] = "בוריס" # זה יגרום לשגיאה: TypeError: 'tuple' object does not support item assignment

    # לא ניתן להוסיף פריט
    # boris_tuple.append(4) # זה יגרום לשגיאה: AttributeError: 'tuple' object has no attribute 'append'

    # לא ניתן למחוק פריט
    # del boris_tuple[0]  # זה יגרום לשגיאה: TypeError: 'tuple' object doesn't support item deletion
    ```

**4. SimpleNamespace**

*   **הגדרה:** `SimpleNamespace` מהמודול `types` - היא מחלקה פשוטה המאפשרת ליצור אובייקטים שתכונותיהם (מאפיינים) ניתנות להגדרה הן בעת היצירה והן מאוחר יותר.
*   **ייצוג:** כדי ליצור אובייקט `SimpleNamespace`, עליך לייבא אותו מ-`types` ולהעביר לו ארגומנטים בעלי שם (או לא להעביר כלל):
     ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="אליס", age=25, city="לונדון")
    ```
*  **תכונות:**
    *  מאפשרת יצירת אובייקטים עם תכונות דינמיות (בדומה למילון).
    *  נוחה ליצירת אובייקטים פשוטים לאחסון נתונים.
    *  תכונות נגישות באמצעות סימון נקודה, כמו אובייקטים רגילים: `alice_namespace.name`
    *  בניגוד למילונים, סדר התכונות נשמר.
    *  ניתן לשנות שדות, אך לא ניתן להוסיף שדות חדשים.

*  **דוגמאות:**
    ```python
    from types import SimpleNamespace

    # יצירת SimpleNamespace
    alice_namespace = SimpleNamespace(name="אליס", age=25, city="לונדון")
    print(f"יצירת SimpleNamespace: {alice_namespace}")

    # גישה לתכונה
    print(f"תכונה 'name': {alice_namespace.name}")

    # שינוי תכונה
    alice_namespace.age = 26
    print(f"שינוי תכונה: {alice_namespace}")

    # לא ניתן להוסיף תכונה חדשה
    # alice_namespace.occupation = "אמנית" # זה יגרום לשגיאה: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

   # הוספה באמצעות setattr
    setattr(alice_namespace, "occupation", "אמנית")
    print(f"הוספת תכונה: {alice_namespace}")

    # מחיקה באמצעות delattr
    delattr(alice_namespace, "city")
    print(f"מחיקת תכונה: {alice_namespace}")
    ```