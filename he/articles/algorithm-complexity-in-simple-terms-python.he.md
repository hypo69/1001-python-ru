## מורכבות אלגוריתמים במילים פשוטות ודוגמאות בפייתון

בתכנות, ישנן דרכים רבות לפתור אותה בעיה. עם זאת, לא כל הפתרונות יעילים באותה מידה. אחד ההיבטים המרכזיים שיש לקחת בחשבון בעת פיתוח אלגוריתמים הוא מורכבותם. הבנת מורכבות של אלגוריתם מאפשרת להעריך כמה מהר הוא יעבוד וכמה משאבים (לדוגמה, זיכרון) הוא ידרוש לביצועו, במיוחד ככל שנפח נתוני הקלט גדל. הבנת מורכבות אלגוריתמים היא מיומנות בסיסית המאפשרת לכתוב קוד יעיל יותר.

### מהי מורכבות אלגוריתם?

תאר לעצמך שיש לך משימה: למצוא שם ספציפי בספר טלפונים.

*   **הדרך הפשוטה (חיפוש לינארי):** אתה לוקח את הספר ומתחיל לדפדף דף אחר דף עד שתמצא את השם שאתה צריך. אם השם נמצא בסוף הספר, תצטרך לדפדף בכל הספר!
*   **הדרך החכמה (חיפוש בינארי):** אתה פותח את הספר באמצע. אם השם שאתה מחפש מופיע לפני השם בדף זה, אתה סוגר את החצי השני של הספר ומחפש בחצי הראשון. אם השם מופיע מאוחר יותר, אתה מחפש בחצי השני. וכך אתה חוזר על הפעולה עד שתמצא את השם שאתה צריך. בכל שלב, אתה זורק חצי מהספר!

**מורכבות אלגוריתם** היא דרך לתאר כמה "זמן" (או משאבים, כגון זיכרון) אלגוריתם יצטרך כדי להשלים את משימתו, בהתאם למידת "גודלה" של המשימה.

*   **חיפוש לינארי:** אם יש 10 עמודים בספר, ייתכן שתצטרך לדפדף ב-10 עמודים. אם יש 100 עמודים בספר, ייתכן שתצטרך לדפדף ב-100 עמודים. כמות העבודה גדלה *באופן לינארי* עם גודל המשימה. זה נקרא **O(n)**, כאשר 'n' הוא גודל המשימה (מספר העמודים בספר).

*   **חיפוש בינארי:** אם יש 16 עמודים בספר, תצטרך לכל היותר 4 צעדים כדי למצוא את השם. אם יש 32 עמודים בספר, תצטרך לכל היותר 5 צעדים. כמות העבודה גדלה הרבה יותר לאט מגודל המשימה. זה נקרא **O(log n)** (נקרא "O של לוג n").



*   אלגוריתם **O(n)** הופך איטי יותר *ביחס ישר* לגידול בגודל המשימה.
*   אלגוריתם **O(log n)** הופך איטי יותר *הרבה יותר לאט* מגידול גודל המשימה.



תאר לעצמך שאתה מפתח מנוע חיפוש. אם תשתמש באלגוריתם O(n) לחיפוש באינטרנט (המכיל מיליארדי דפי אינטרנט), זה ייקח זמן רב להפליא! ואלגוריתם O(log n) יטפל במשימה זו הרבה יותר מהר.

### סוגים עיקריים של מורכבות אלגוריתמים

להלן כמה מסוגי המורכבות הנפוצים ביותר:

*   **O(1) – מורכבות קבועה:** זמן הריצה תמיד זהה, ללא קשר לגודל המשימה. לדוגמה, לקיחת האיבר הראשון מרשימה.

    ```python
    def get_first_element(my_list):
        """O(1) - קבלת האיבר הראשון ברשימה."""
        return my_list[0]
    ```

*   **O(log n) – מורכבות לוגריתמית:** זמן הריצה גדל לאט מאוד ככל שגודל המשימה גדל. דוגמה מצוינת היא חיפוש בינארי.

    ```python
    def binary_search(my_list, target):
        """O(log n) - חיפוש בינארי ברשימה ממוינת."""
        low = 0
        high = len(my_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if my_list[mid] == target:
                return mid
            elif my_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # איבר לא נמצא
    ```

*   **O(n) – מורכבות לינארית:** זמן הריצה גדל באופן יחסי ישר לגודל המשימה. לדוגמה, מעבר על כל איבר ברשימה.

    ```python
    def linear_search(my_list, target):
        """O(n) - חיפוש לינארי ברשימה."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # איבר לא נמצא
    ```

*   **O(n log n) – מורכבות לינארית-לוגריתמית:**  נמצא לעיתים קרובות באלגוריתמי מיון יעילים, כגון מיון מיזוג ומיון מהיר.

    ```python
    def merge_sort(my_list):
        """O(n log n) - מיון מיזוג."""
        if len(my_list) <= 1:
            return my_list

        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])

        return merge(left, right)

    def merge(left, right):
        """פונקציית עזר ל-merge_sort."""
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    ```

*   **O(n^2) – מורכבות ריבועית:** זמן הריצה גדל *ריבועית* עם גודל המשימה. לדוגמה, השוואת כל איבר ברשימה לכל איבר אחר באותה רשימה.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - מיון בועות."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – מורכבות אקספוננציאלית:** זמן הריצה גדל מהר מאוד ככל שגודל המשימה גדל.  נמצא בדרך כלל באלגוריתמים המשתמשים בכוח גס.

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - חישוב רקורסיבי של מספר פיבונאצ'י."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – מורכבות עצרתית:** סוג המורכבות האיטי ביותר. מתרחש בעת איטרציה על כל התמורות האפשריות של איברים.

### דוגמאות לבעיות ואלגוריתמים עם מורכבות שונה

בואו נסתכל על כמה דוגמאות לבעיות ואלגוריתמים שונים לפתרונן כדי לראות
כיצד המורכבות משפיעה על הביצועים.

**1. מיון רשימה:**

*   **משימה:** מיון רשימה של איברים בסדר מסוים (לדוגמה, עולה).
*   **אלגוריתמים:**
    *   **מיון בועות (Bubble Sort):**

        ```python
        def bubble_sort(my_list):
            n = len(my_list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if my_list[j] > my_list[j+1] :
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        # דוגמת שימוש
        my_list = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(my_list)
        print("מערך ממוין:", my_list) # פלט: [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **מיון מיזוג (Merge Sort):**

        ```python
        def merge_sort(my_list):
            if len(my_list) <= 1:
                return my_list

            mid = len(my_list) // 2
            left = merge_sort(my_list[:mid])
            right = merge_sort(my_list[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        # דוגמת שימוש
        my_list = [64, 34, 25, 12, 22, 11, 90]
        sorted_list = merge_sort(my_list)
        print("מערך ממוין:", sorted_list) # פלט: [11, 12, 22, 25, 34, 64, 90]
        ```
*   **מסקנה:** עבור רשימות גדולות של איברים, אלגוריתמים עם O(n log n) (מיון מיזוג) עדיפים על אלגוריתמים עם O(n^2) (מיון בועות).

**2. מציאת המסלול הקצר ביותר בגרף:**

*   **משימה:** מציאת המסלול הקצר ביותר בין שני קודקודים בגרף (לדוגמה, בין שתי ערים על מפה).
*   **אלגוריתמים:**
    *   **אלגוריתם דיקסטרה:**

        ```python
        import heapq

        def dijkstra(graph, start):
            """אלגוריתם דיקסטרה למציאת המסלולים הקצרים ביותר."""
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            priority_queue = [(0, start)]  # (מרחק, צומת)

            while priority_queue:
                distance, node = heapq.heappop(priority_queue)

                if distance > distances[node]:
                    continue

                for neighbor, weight in graph[node].items():
                    new_distance = distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbor))

            return distances

        # דוגמת שימוש
        graph = {
            'A': {'B': 5, 'C': 1},
            'B': {'A': 5, 'C': 2, 'D': 1},
            'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
            'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
            'E': {'C': 8, 'D': 3},
            'F': {'D': 6}
        }
        start_node = 'A'
        shortest_paths = dijkstra(graph, start_node)
        print(f"המסלולים הקצרים ביותר מ-{start_node}: {shortest_paths}")
        ```

*   **מסקנה:** בחירת האלגוריתם תלויה בסוג הגרף (משוקלל/לא משוקלל, נוכחות משקלים שליליים) ובגודל הגרף. אלגוריתם דיקסטרה יעיל עבור גרפים עם משקלים לא שליליים.

**3. מציאת תת-מחרוזת במחרוזת:**

*   **משימה:** מציאת כל המופעים של תת-מחרוזת ספציפית במחרוזת גדולה יותר.
*   **אלגוריתמים:**
    *   **חיפוש מחרוזת נאיבי (Naive String Search):**

        ```python
        def naive_string_search(text, pattern):
            """אלגוריתם חיפוש מחרוזת נאיבי."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # דוגמת שימוש
        text = "זוהי דוגמת טקסט פשוטה."
        pattern = "דוגמה"
        occurrences = naive_string_search(text, pattern)
        print(f"מופעים של '{pattern}' בטקסט: {occurrences}")  # פלט: [17]
        ```

*   **מסקנה:** עבור חיפושי תת-מחרוזות תכופים במחרוזות גדולות, קיימים אלגוריתמים יעילים יותר, כגון KMP.

**4. בעיית התרמיל (Knapsack Problem):**

*   **משימה:** יש לך תרמיל בקיבולת מסוימת וקבוצת פריטים עם משקלים וערכים שונים. עליך לבחור את הפריטים שימקסמו את הערך הכולל, מבלי לחרוג מקיבולת התרמיל.
*   **אלגוריתמים:**
    *   **תכנות דינמי (Dynamic Programming):**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """פתרון בעיית התרמיל באמצעות תכנות דינמי."""
            dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

            for i in range(n + 1):
                for w in range(capacity + 1):
                    if i == 0 or w == 0:
                        dp[i][w] = 0
                    elif weights[i-1] <= w:
                        dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],  dp[i-1][w])
                    else:
                        dp[i][w] = dp[i-1][w]

            return dp[n][capacity]

        # דוגמת שימוש
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(values)
        max_value = knapsack_dynamic_programming(capacity, weights, values, n)
        print(f"ערך מקסימלי: {max_value}")  # פלט: 220
        ```

*   **בחירת האלגוריתם תלויה בגודל הבעיה ובדרישות לדיוק הפתרון.**

###  סימון Big O: פישוט המורכבות

בדרך כלל, מורכבות מתוארת באמצעות "Big O" (סימון O). היא מראה כמה מהר זמן הריצה של אלגוריתם גדל עם גודל המשימה, *אסימפטוטית*, כלומר, עבור ערכים גדולים מאוד של `n`. קבועים קטנים ופרטי יישום בדרך כלל מתעלמים. לדוגמה, אלגוריתם המבצע `2n + 5` פעולות עדיין נחשב *O(n)*.

###  המקרה הגרוע ביותר, המקרה הממוצע, המקרה הטוב ביותר

מורכבות של אלגוריתם יכולה להיות תלויה בנתוני הקלט. בדרך כלל אנו מדברים על מורכבות ב*מקרה הגרוע ביותר*: זוהי הכמות המקסימלית של זמן או משאבים שאלגוריתם עשוי לדרוש. לעיתים, מנותחת גם מורכבות במקרה הממוצע ובמקרה הטוב ביותר.
