## Dataclasses: כשפייתון פוגש נתונים מובנים (עם דוגמאות חדשות עם שמות)

בפייתון, כשצריך מחלקה לאחסון נתונים, בדרך כלל צריך לכתוב קוד תבניתי עבור `__init__`, `__repr__`, `__eq__` ומתודות קסם אחרות. המודול `dataclasses`, שהוצג בפייתון 3.7, נועד לפתור בעיה זו על ידי מתן הדקורטור `@dataclass`, שמייצר באופן אוטומטי את המתודות הללו עבורך.

### מה זה Dataclass?

`dataclass` היא מחלקה, שכפי שהשם מרמז, מיועדת בעיקר לאחסון נתונים. היא מספקת את היתרונות המרכזיים הבאים:

1.  **פחות קוד תבניתי:** מייצר באופן אוטומטי `__init__`, `__repr__`, `__eq__`, `__hash__` (בתנאים מסוימים), ומתודות אחרות המבוססות על הערות הטיפוסים של השדות שלך.
2.  **קריאות:** הקוד הופך לתמציתי יותר וממוקד בהגדרת מבנה הנתונים.
3.  **אינטרוספקציה:** קל לבדוק את שדות ה-dataclass באמצעות פונקציות מאותו מודול `dataclasses`.
4.  **ביצועים (עם `slots=True`):** יכול לצרוך פחות זיכרון ולהיות מהיר יותר בגישה לתכונות.

### שימוש בסיסי

נתחיל עם דוגמה פשוטה. נניח שאנחנו צריכים מחלקה לייצוג נקודה במרחב דו-ממדי.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# יצירת מופע
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - __repr__ שנוצר אוטומטית

# השוואת מופעים - __eq__ שנוצר אוטומטית
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

כפי שאתה יכול לראות, לא היינו צריכים לכתוב `__init__` או `__repr__`. הכל עבד "מהקופסה".

### פרמטרים של הדקורטור `@dataclass`

הדקורטור `@dataclass` מקבל מספר פרמטרים המאפשרים לך להתאים אישית את ההתנהגות שנוצרת.

```python
@dataclass(
    init=True,         # האם ליצור __init__ (ברירת מחדל True)
    repr=True,         # האם ליצור __repr__ (ברירת מחדל True)
    eq=True,           # האם ליצור __eq__ (ברירת מחדל True)
    order=False,       # האם ליצור __lt__, __le__, __gt__, __ge__ (ברירת מחדל False)
    unsafe_hash=False, # האם ליצור __hash__ (ברירת מחדל False)
    frozen=False,      # האם להפוך מופעים לבלתי ניתנים לשינוי (ברירת מחדל False)
    match_args=True,   # האם לכלול את המחלקה במנגנון התאמת תבניות מבנית (פייתון 3.10+, ברירת מחדל True)
    kw_only=False,     # האם להפוך את כל השדות לארגומנטים של מילת מפתח בלבד ב-__init__ (פייתון 3.10+, ברירת מחדל False)
    slots=False        # האם להשתמש ב-__slots__ כדי לחסוך בזיכרון (פייתון 3.10+, ברירת מחדל False)
)
class MyDataClass:
    # ...
```

בואו נבחן את החשובים שבהם, כולל אלה מהבקשה שלך:

#### `init=True` (ברירת מחדל)

אם `True`, `dataclass` ייצור מתודת `__init__`. אם יש לך `__init__` משלך ואתה משאיר את `init=True`, ה-`__init__` שלך יופעל, אך השדות שהוגדרו ב-dataclass לא יאותחלו דרכו באופן אוטומטי. בדרך כלל, אם אתה כותב `__init__` משלך, אתה מגדיר `init=False` כדי למנוע התנגשויות ולשלוט באופן מלא באתחול.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "שלום!"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("אליס", 30) # מדפיס "שלום!"
print(alice) # CustomPersonInit(name='אליס', age=30) - repr עדיין עובד
```

#### `repr=True` (ברירת מחדל)

אם `True`, ייצור מתודת `__repr__` המספקת ייצוג מחרוזת נוח של האובייקט, שימושי לניפוי באגים.

#### `eq=True` (ברירת מחדל)

אם `True`, ייצור מתודת `__eq__` המאפשרת לך להשוות שני מופעים של מחלקה לשוויון על ידי בדיקת שוויון כל השדות שלהם.

#### `order=False`

אם `True`, `dataclass` ייצור מתודות `__lt__`, `__le__`, `__gt__`, `__ge__`. זה מאפשר לך להשוות מופעים עבור "קטן מ", "גדול מ" וכו'. ההשוואה מתבצעת לפי סדר הצהרת השדות. כדי ש-`order=True` יעבוד, `eq=True` חייב להיות מוגדר גם כן.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("אליס", 30)
boris = Person("בוריס", 25)
victor = Person("ויקטור", 35) # בואו נוסיף את ויקטור
galina = Person("גלינה", 30)
alice_older = Person("אליס", 35)


print(f"אליס ({alice.age}) > בוריס ({boris.age})? {alice > boris}") # False (כי 'אליס' < 'בוריס' לפי שם). ההשוואה היא לקסיקוגרפית על הטאפל (שם, גיל). ('אליס', 30) < ('בוריס', 25) זה False. אז `>` יהיה False.
# הסבר: ('אליס', 30) > ('בוריס', 25) -> False, כי 'אליס' < 'בוריס'.
print(f"אליס ({alice.age}) < alice_older ({alice_older.age})? {alice < alice_older}") # True (כי השם זהה, והגיל 30 < 35)
print(f"גלינה ({galina.age}) == אליס ({alice.age})? {galina == alice}") # False (שמות שונים)
```

**הערה חשובה:** סדר השדות חשוב עבור `order=True`.

#### `unsafe_hash=False`

אם `True`, ייצור מתודת `__hash__`. Dataclasses אינם ניתנים לגיבוב כברירת מחדל אם הם ניתנים לשינוי (`frozen=False`) מכיוון שאובייקטים ניתנים לגיבוב חייבים להיות בלתי ניתנים לשינוי. אם אתה בטוח שה-dataclass הניתן לשינוי שלך ישמש רק בהקשרים שבהם הגיבוב שלו לא ישתנה (וזה מסוכן!), תוכל להגדיר `unsafe_hash=True`.
הרבה יותר נפוץ, `__hash__` נוצר באופן אוטומטי אם:
1.  `frozen=True`.
2.  `frozen=False`, אבל `eq=True` וכל השדות ניתנים לגיבוב גם כן.

```python
@dataclass(frozen=True) # dataclasses קפואים ניתנים לגיבוב
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # עובד

@dataclass(unsafe_hash=True) # מסוכן אם האובייקט ניתן לשינוי
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # הגיבוב השתנה, מה שעלול להוביל לבעיות בעת שימוש ב-set/dict
```

#### `frozen=False`

אם `True`, מופעים של המחלקה הופכים לבלתי ניתנים לשינוי. לאחר יצירת אובייקט, לא תוכל לשנות את ערכי השדות שלו. זה שימושי ליצירת אובייקטים בלתי ניתנים לשינוי שקל יותר להשתמש בהם ביישומים מרובי הליכים או כמפתחות מילון (אם הם ניתנים לגיבוב).

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (פייתון 3.10+)

אם `True`, **כל** השדות ב-`__init__` הופכים לארגומנטים של **מילת מפתח בלבד**. זה אומר שאתה חייב להעביר את ערכי השדות לפי שם, לא לפי מיקום. זה משפר את הקריאות ומונע שגיאות, במיוחד כאשר למחלקה יש שדות רבים או שהם עשויים להיות מאותו סוג.

```python
@dataclass(kw_only=True)
class UserConfig:
    username: str
    email: str
    is_active: bool = True
    theme: str = "dark"

# user1 = UserConfig("alice_ivanova", "alice@example.com") # TypeError: __init__() takes 0 positional arguments but 3 were given
user1 = UserConfig(username="alice_ivanova", email="alice@example.com")
print(user1)

# אתה יכול לעקוף התנהגות זו עבור שדה ספציפי עם field(kw_only=False)
@dataclass(kw_only=True)
class MixedConfig:
    # חובה מיקומי (לא בסגנון dataclass)
    # השדה `id` לא יהיה kw_only, למרות שהמחלקה צוינה כ-kw_only=True
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # שאר השדות הם kw_only
    email: str
    age: int = 0

# שים לב ש-id ושם מועברים לפי מיקום, ואימייל מועבר לפי שם
mixed_config = MixedConfig(123, "בוריס", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="ויקטור", email="viktor@example.com") # שגיאה, id ושם יהיו מיקומיים
# תרחיש זה פחות טיפוסי, kw_only מוחל בדרך כלל על כל המחלקה
```

**הערה:** `field(kw_only=False)` על שדה עוקף את `kw_only=True` ברמת המחלקה, מה שהופך את השדה הספציפי הזה למיקומי. עם זאת, לרוב, `kw_only=True` משמש לכל המחלקה. השימוש העיקרי ב-`field(kw_only=True)` הוא כאשר יש לך dataclass רגיל (`kw_only=False` כברירת מחדל), אבל אתה רוצה להפוך *כמה* שדות למילות מפתח בלבד.

#### `slots=False` (פייתון 3.10+)

אם `True`, `dataclass` ייצור `__slots__` עבור המחלקה שלך. `__slots__` הוא תכונה מיוחדת המאפשרת לפייתון להקצות כמות קבועה של זיכרון למופעי מחלקה, במקום להשתמש במילון דינמי `__dict__` לאחסון תכונות.

**יתרונות של `slots=True`:**
*   **חיסכון בזיכרון:** מפחית באופן משמעותי את כמות הזיכרון הנצרכת על ידי כל מופע. זה חשוב במיוחד עבור יישומים שיוצרים מיליוני אובייקטים.
*   **גישה מהירה יותר לתכונות:** גישה לתכונות באמצעות `__slots__` יכולה להיות מעט מהירה יותר, מכיוון שפייתון לא צריך לחפש אותן במילון.

**חסרונות של `slots=True`:**
*   **לא ניתן להוסיף תכונות חדשות "על הדרך":** לא תוכל להקצות תכונה שלא הוצהרה ב-dataclass (או ב-`__slots__` של מחלקת אב).
*   **קשיים עם ירושה מרובה:** זה יכול להיות קשה להשתמש ב-`__slots__` עם ירושה מרובה, במיוחד אם כמה מחלקות אב אינן משתמשות ב-`__slots__` או משתמשות בהן באופן שונה.
*   **אין לו `__dict__`:** למופעים לא תהיה תכונת `__dict__` אלא אם כן היא נוספה במפורש ל-`__slots__` או למחלקת אב.

```python
import sys

@dataclass
class RegularPoint:
    x: int
    y: int

@dataclass(slots=True)
class SlottedPoint:
    x: int
    y: int

rp = RegularPoint(1, 2)
sp = SlottedPoint(1, 2)

print(f"גודל של RegularPoint: {sys.getsizeof(rp)} בתים")
# בערך 56 בתים בפייתון 3.10+ (עשוי להשתנות)
# print(rp.__dict__) # {'x': 1, 'y': 2} - יש לו __dict__

print(f"גודל של SlottedPoint: {sys.getsizeof(sp)} בתים")
# בערך 32 בתים בפייתון 3.10+ (עשוי להשתנות) - קטן משמעותית
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# ניסיון להוסיף תכונה חדשה ל-dataclass עם slots
try:
    sp.z = 30
except AttributeError as e:
    print(f"שגיאה בהוספת תכונה חדשה: {e}")
```

**מתי להשתמש ב-`slots=True`?**
כשאתה יוצר מספר גדול מאוד של מופעים של אותה מחלקה, וחיסכון בזיכרון הוא בראש סדר העדיפויות. זוהי אופטימיזציה נהדרת, אבל יש לה את הפשרות שלה.

### פונקציית `field()`: תצורת שדה מפורטת

בנוסף לפרמטרים ברמת המחלקה, ניתן להגדיר כל שדה בנפרד באמצעות הפונקציה `field()` מהמודול `dataclasses`. זה שימושי במיוחד כאשר אתה זקוק ללוגיקה מורכבת יותר עבור שדות מאשר רק הערת טיפוס.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # ליצירת מזהים

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # לא מאותחל דרך __init__, נוצר אוטומטית
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # לא נכלל בהשוואה, יש לו מטא-נתונים
    tags: List[str] = field(default_factory=list, repr=False) # משתמש בפונקציית מפעל לרשימה, לא מוצג ב-repr
    description: str = field(default="אין תיאור") # ערך ברירת מחדל רגיל
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # לא נכלל בגיבוב

p = Product(name="מחשב נייד", price=1200.0, tags=["אלקטרוניקה", "טכנולוגיה"])
print(p)
# Product(id='prod-...', name='מחשב נייד', price=1200.0, description='אין תיאור', details={})
# שים לב ש-'tags' אינו ב-repr, ו-'id' נוצר באופן אוטומטי.

p2 = Product(name="מחשב נייד", price=1500.0, tags=["אלקטרוניקה", "טכנולוגיה"])
print(f"p == p2? {p == p2}") # True, כי המחיר אינו נכלל בהשוואה (compare=False)

# p3 = Product(name="מחשב שולחני", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (בגלל details: hash=False)
# אם frozen=True, ו-details לא היו hash=False, אז ה-dict היה צריך להיות בלתי ניתן לשינוי.
```

בואו נבחן את הפרמטרים של `field()`:

*   **`default`**: ערך ברירת מחדל רגיל עבור השדה.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`**: פונקציה ללא ארגומנטים שתופעל כדי לקבל את ערך ברירת המחדל עבור השדה. **הקפד להשתמש ב-`default_factory` עבור ערכי ברירת מחדל ניתנים לשינוי (רשימות, מילונים, אובייקטים) כדי למנוע בעיות של מצב משותף בין מופעים!**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`**: אם `True` (ברירת מחדל), השדה ייכלל במתודת `__init__` שנוצרה. אם `False`, השדה לא יהיה ארגומנט בקונסטרוקטור, ואתה חייב לספק לו `default` / `default_factory`, או לאתחל אותו ב-`__post_init__`.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`**: אם `True` (ברירת מחדל), השדה ייכלל במתודת `__repr__` שנוצרה. שימושי להסתרת נתונים גדולים או רגישים.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`**: אם `True` (ברירת מחדל), השדה ייכלל במתודות `__eq__` ו-`__order__` שנוצרו. אם `False`, הוא לא ישפיע על השוואת אובייקטים.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`**: אם `True` (ברירת מחדל), השדה ייכלל במתודת `__hash__` שנוצרה. אם `False`, הוא לא ישפיע על הגיבוב של האובייקט. אם המחלקה היא `frozen=True`, אבל לשדה כלשהו יש `hash=False`, אז המחלקה לא תוכל ליצור את ה-`__hash__` שלה ותהפוך לבלתי ניתנת לגיבוב.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`**: מילון לאחסון נתונים שרירותיים המשויכים לשדה. `dataclasses` מתעלמים מנתונים אלה, אך ניתן להשתמש בהם על ידי כלים חיצוניים (למשל, לאימות, סריאליזציה, יצירת תיעוד).
    ```python
    user_id: int = field(metadata={'help': 'מזהה משתמש ייחודי', 'validator': 'positive_int'})
    ```

*   **`kw_only`**: (פייתון 3.10+) אם `True`, שדה ספציפי זה הופך לארגומנט של מילת מפתח בלבד ב-`__init__`. אם `False`, הוא הופך למיקומי. זה מאפשר לך לערבב ארגומנטים מיקומיים ושל מילות מפתח בלבד כאשר ה-`kw_only` של המחלקה הוא `False` כברירת מחדל.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # מיקומי
        optional_kw: int = field(default=0, kw_only=True) # מילת מפתח בלבד

    fp1 = FlexibleParams("נדרש", optional_kw=100)
    # fp2 = FlexibleParams("נדרש", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### פונקציית `fields()`: אינטרוספקציה של Dataclass

הפונקציה `fields()` מהמודול `dataclasses` מאפשרת לך לקבל מידע על השדות של dataclass או מופע שלו. היא מחזירה טאפל של אובייקטים `Field`.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'מחבר', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# קבלת מידע על השדות של מחלקת Book
book_fields = fields(Book)

for f in book_fields:
    print(f"שם השדה: {f.name}")
    print(f"טיפוס השדה: {f.type}")
    print(f"ערך ברירת מחדל: {f.default}")
    print(f"משתמש ב-default_factory: {f.default_factory is not None}")
    print(f"נכלל ב-init: {f.init}")
    print(f"נכלל ב-repr: {f.repr}")
    print(f"נכלל ב-compare: {f.compare}")
    print(f"נכלל ב-hash: {f.hash}")
    print(f"מטא-נתונים: {f.metadata}")
    print(f"מילת מפתח בלבד: {f.kw_only}") # עבור פייתון 3.10+
    print("-" * 20)

# גישה למטא-נתונים של שדה ספציפי:
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"שם תצוגה למחבר: {author_field_info.metadata.get('display_name')}")
```

לאובייקט `Field` יש את התכונות הבאות: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### מתודת `__post_init__`

לפעמים אתה זקוק ללוגיקה נוספת לאחר שה-`__init__` האוטומטי של ה-dataclass סיים לאתחל את השדות. לשם כך, תוכל להגדיר מתודת `__post_init__`. היא תופעל מיד לאחר `__init__`.

זה שימושי עבור:
*   אימות נתונים.
*   חישוב שדות נגזרים המבוססים על שדות שכבר אותחלו.
*   ביצוע כל לוגיקה אחרת התלויה בשדות מאותחלים במלואם.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # שדה זה לא ייכלל בפרמטרים של __init__
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ הופעל עבור {self.first_name} {self.last_name} ---")
        # אימות
        if not self.first_name or not self.last_name:
            raise ValueError("שם פרטי ושם משפחה אינם יכולים להיות ריקים.")
        # חישוב שדה נגזר
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"משתמש {self.first_name} {self.last_name} נוצר עם אימייל: {self.email}")
        print(f"זמן יצירה: {self.created_at}")
        print(f"--- __post_init__ הסתיים ---")

alice_ivanova = User("אליס", "איבנובה")
print("\nאובייקט נוצר:")
print(alice_ivanova)

print("\n")

try:
    victor_no_last_name = User("ויקטור", "")
except ValueError as e:
    print(f"שגיאה ביצירת משתמש: {e}")
```

### ירושה של Dataclass

Dataclasses תומכים בירושה. שדות ממחלקות בסיס נכללים במחלקות ילד.

```python
@dataclass
class Vehicle:
    make: str
    model: str

@dataclass
class Car(Vehicle):
    num_doors: int
    is_electric: bool = False

@dataclass
class ElectricCar(Car):
    battery_kwh: float

alices_car = Car("Toyota", "Camry", 4)
print(alices_car) # Car(make='Toyota', model='Camry', num_doors=4, is_electric=False)

boris_car = ElectricCar("Tesla", "Model 3", 4, True, 75.0)
print(boris_car) # ElectricCar(make='Tesla', model='Model 3', num_doors=4, is_electric=True, battery_kwh=75.0)
```

**תכונות של ירושה עם `slots=True`:**
*   אם מחלקת האב משתמשת ב-`__slots__`, מחלקת הילד חייבת להשתמש גם ב-`__slots__` כדי לקבל את חיסכון הזיכרון.
*   מחלקת הילד חייבת להגדיר `__slots__` משלה עבור השדות החדשים שלה.
*   אם מחלקת הילד אינה מגדירה `__slots__`, יהיה לה `__dict__` בנוסף ל-slots של האב.

### מתי להשתמש ב-Dataclasses?

*   **מחלקות מיכל נתונים:** כאשר המטרה העיקרית של המחלקה היא לאחסן נתונים, ואתה זקוק ל-`__init__`, `__repr__`, `__eq__` אוטומטיים.
*   **אובייקטים בלתי ניתנים לשינוי:** כאשר אתה זקוק לאובייקטים שמצבם לא אמור להשתנות לאחר היצירה (`frozen=True`).
*   **תצורות:** להגדרת מבנה של פרמטרי תצורה.
*   **אובייקטי העברת נתונים (DTOs):** להעברת נתונים מובנים בין חלקי יישום.
*   **לוגיקה עסקית פשוטה:** כאשר מתודות המחלקה פועלות בעיקר על נתוני המחלקה עצמה, אין להן מצב פנימי מורכב או תופעות לוואי.

### מתי לא להשתמש ב-Dataclasses?

*   **מחלקות עם התנהגות עשירה:** כאשר למחלקה יש לוגיקה עסקית מורכבת, מתודות רבות המקיימות אינטראקציה עם מערכות חיצוניות, או מצב פנימי מורכב, עדיף להשתמש במחלקה רגילה.
*   **מודלים של מיפוי OR (ORM):** למרות ש-dataclasses יכולים להיות חלק מ-ORM, הם אינם מחליפים מודלים מלאים של ORM, שלעתים קרובות דורשים מתודות ספציפיות לעבודה עם מסד נתונים, טעינה עצלה וכו'.
*   **פולימורפיזם והיררכיית ירושה עמוקה:** אם יש לך היררכיית מחלקות מורכבת עם פולימורפיזם עמוק ועקיפת התנהגות, מחלקות רגילות עשויות להיות גמישות יותר.

### מסקנה

`dataclasses` הם תוספת חזקה ונוחה לפייתון שמפשטת באופן משמעותי את יצירת המחלקות מוכוונות הנתונים. הם עוזרים לכתוב קוד נקי, קריא וניתן לתחזוקה יותר, ואפשרויות כמו `slots=True` ו-`kw_only=True` מספקות הזדמנויות נוספות לאופטימיזציה של ביצועים ושיפור הארגונומיה של ה-API של הקוד שלך. אל תשכח את `field()` לתצורה מפורטת של כל שדה ואת `fields()` לאינטרוספקציה!
