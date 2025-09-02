## 📘 Instruction for Python Code Generation

### 1. General Rules

* Use **Python 3.10+**.
* Adhere to a **clear, readable, and unambiguous coding style**.
* **Every function, method, and class** must have:

  * Type annotations (`type hints`)
  * Full and correct documentation in `docstring` format (see section 3)
  * Internal comments (`#`), where necessary

---

### 2. Comments

* Comments must be **accurate** and describe **what the code does**, not "what we do".
* **Forbidden** to use pronouns: `we do`, `we return`, `we send`, `we go`, etc.
* **Allowed** only terms: `extraction`, `execution`, `call`, `replacement`, `check`, `sending`, `Function performs`, `Function changes value`, etc.

#### ❌ Example of incorrect comment:

```python
# Get parameter value
```

#### ✅ Example of correct comment:

```python
# Function extracts parameter value
```

---

### 3. Docstring (documentation format)

Every function/method/class must contain a `docstring` in the following format:

```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Description of parameter `param`.
        param1 (Optional[str | dict | str], optional): Description of parameter `param1`. Defaults to `None`.

    Returns:
        dict | None: Description of the return value. Returns a dictionary or `None`.

    Raises:
        SomeError: Description of the situation in which the `SomeError` exception occurs.

    Example:
        >>> function('param', 'param1')
        {'param': 'param1'}
    """
```

* **All parameters and return values must be described.**
* Formulations must be **concise, accurate, and unambiguous**.
* Skipping the description of parameters/return values/exceptions is not allowed.

---

### 4. Type annotation

* **All variables, parameters, and return values** must be annotated.
* Use Python 3.10+ syntax: `list[int]`, `dict[str, Any]`, `str | None`, etc.
* Examples of correct annotations:

#### ✅ Simple types:

```python
name: str = "John"
count: int = 42
flag: bool = True
```

#### ✅ Collections and complex types:

```python
from typing import Any, Optional, Callable, TypeAlias

coordinates: tuple[float, float] = (55.75, 37.61)
metadata: dict[str, Any] = {"debug": True}
UserId: TypeAlias = int
```

#### ✅ Functions and methods:

```python
def get_user_name(user_id: int) -> str:
    """Returns the user's name by their ID."""
    ...
```

#### ✅ Asynchronous functions:

```python
async def fetch_users() -> AsyncIterator[dict[str, int | str]]:
    ...
```

#### ✅ Generic types:

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

### 5. Other

* Use `default_factory` in `dataclass` for mutable values (`list`, `dict`).
* For `Optional` values, specify `T | None` (Python 3.10+) or `Optional[T]`.
* For complex structures, use `TypeAlias`.

---

📌 **Hint**: When generating code, always include type annotations, `docstring`, and avoid subjective phrasing in comments. The goal is the most accurate, reproducible, and formalized code structure.