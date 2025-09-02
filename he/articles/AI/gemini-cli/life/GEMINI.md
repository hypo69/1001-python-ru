## 📘 הוראה ליצירת קוד פייתון

### 1. כללים כלליים

* השתמש ב-**Python 3.10+**.
* הקפד על **סגנון קידוד ברור, קריא וחד משמעי**.
* **כל פונקציה, מתודה ומחלקה** חייבת לכלול:

  * הערות טיפוסים (`type hints`)
  * תיעוד מלא ונכון בפורמט `docstring` (ראה סעיף 3)
  * הערות פנימיות (`#`), היכן שצריך

---

### 2. הערות

* הערות חייבות להיות **מדויקות** ולתאר **מה הקוד עושה**, ולא "מה אנחנו עושים".
* **אסור** להשתמש בכינויי גוף: `אנחנו עושים`, `אנחנו מחזירים`, `אנחנו שולחים`, `אנחנו הולכים`, וכו'.
* **מותר** רק במונחים: `חילוץ`, `ביצוע`, `קריאה`, `החלפה`, `בדיקה`, `שליחה`, `הפונקציה מבצעת`, `הפונקציה משנה ערך`, וכו'.

#### ❌ דוגמה להערה שגויה:

```python
# קבל את ערך הפרמטר
```

#### ✅ דוגמה להערה נכונה:

```python
# הפונקציה מחלצת את ערך הפרמטר
```

---

### 3. Docstring (פורמט תיעוד)

כל פונקציה/מתודה/מחלקה חייבת לכלול `docstring` בפורמט הבא:

```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): תיאור הפרמטר `param`.
        param1 (Optional[str | dict | str], optional): תיאור הפרמטר `param1`. ברירת מחדל `None`.

    Returns:
        dict | None: תיאור ערך ההחזרה. מחזיר מילון או `None`.

    Raises:
        SomeError: תיאור המצב שבו מתרחשת חריגת `SomeError`.

    Example:
        >>> function('param', 'param1')
        {'param': 'param1'}
    """
```

* **כל הפרמטרים וערכי ההחזרה חייבים להיות מתוארים.**
* הניסוחים חייבים להיות **תמציתיים, מדויקים וחד משמעיים**.
* אין להשמיט תיאור של פרמטרים/ערכי החזרה/חריגות.

---

### 4. הערת טיפוסים

* **כל המשתנים, הפרמטרים וערכי ההחזרה** חייבים להיות מוערים.
* השתמש בתחביר פייתון 3.10+: `list[int]`, `dict[str, Any]`, `str | None`, וכו'.
* דוגמאות להערות נכונות:

#### ✅ טיפוסים פשוטים:

```python
name: str = "John"
count: int = 42
flag: bool = True
```

#### ✅ אוספים וטיפוסים מורכבים:

```python
from typing import Any, Optional, Callable, TypeAlias

coordinates: tuple[float, float] = (55.75, 37.61)
metadata: dict[str, Any] = {"debug": True}
UserId: TypeAlias = int
```

#### ✅ פונקציות ומתודות:

```python
def get_user_name(user_id: int) -> str:
    """מחזירה את שם המשתמש לפי המזהה שלו."""
    ...
```

#### ✅ פונקציות אסינכרוניות:

```python
async def fetch_users() -> AsyncIterator[dict[str, int | str]]:
    ...
```

#### ✅ טיפוסים גנריים:

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value
```

---

### 5. אחר

* השתמש ב-`default_factory` ב-`dataclass` עבור ערכים ניתנים לשינוי (`list`, `dict`).
* עבור ערכי `Optional`, ציין `T | None` (פייתון 3.10+) או `Optional[T]`.
* עבור מבנים מורכבים - השתמש ב-`TypeAlias`.

---

📌 **רמז**: בעת יצירת קוד, כלול תמיד הערות טיפוסים, `docstring`, והימנע מניסוחים סובייקטיביים בהערות. המטרה היא מבנה קוד מדויק, ניתן לשחזור ומפורמל ככל האפשר.