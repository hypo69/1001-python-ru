### **Scenario for Gemini CLI: Conway's Game of Life.**

#### **Step 1: Creating the `GEMINI.MD` system instruction**
In the working directory, create a `GEMINI.md` file and paste the system instruction into it. Example instruction:

```markdown
## 📘 Instruction for generating Python code

### 1. General rules

* Use **Python 3.10+**.
* Adhere to a **clear, readable, and unambiguous coding style**.
* **Every function, method, and class** must have:

  * Type hints
  * Complete and correct documentation in `docstring` format (see section 3)
  * Internal comments (`#`), where necessary

---

### 2. Comments

* Comments must be **accurate** and describe **what the code does**, not "what we are doing".
* **It is forbidden** to use pronouns: `we do`, `we return`, `we send`, `we go` and so on.
* **Only terms are allowed**: `extraction`, `execution`, `call`, `replacement`, `check`, 
`sending`, `The function performs`, `The function changes the value`, etc.

#### ❌ Example of an incorrect comment:

```python
# We get the parameter value
```

#### ✅ Example of a correct comment:

``````python
# The function extracts the parameter value
``````

---

### 3. Docstring (documentation format)

Each function/method/class must contain a `docstring` in the following format:

<pre>```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Description of the `param` parameter.
        param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

    Returns:
        dict | None: Description of the return value. Returns a dictionary or `None`.

    Raises:
        SomeError: Description of the situation in which the `SomeError` exception occurs.

    Example:
        >>> function('param', 'param1')
        {'param': 'param1'}
    """
```</pre>

* **All parameters and return values must be described.**
* The wording must be **concise, accurate, and unambiguous**.
* Do not omit the description of parameters/return values/exceptions.

---

### 4. Type hints

* **All variables, parameters, and return values** must be annotated.
* Use Python 3.10+ syntax: `list[int]`, `dict[str, Any]`, `str | None`, etc.
* Examples of correct annotations:

#### ✅ Simple types:

<pre>```python
name: str = "John"
count: int = 42
flag: bool = True
```

#### ✅ Collections and complex types:

<pre>```python
from typing import Any, Optional, Callable, TypeAlias

coordinates: tuple[float, float] = (55.75, 37.61)
metadata: dict[str, Any] = {"debug": True}
UserId: TypeAlias = int
```

#### ✅ Functions and methods:

<pre>```python
def get_user_name(user_id: int) -> str:
    """Returns the user's name by their ID."""
    ...
```

#### ✅ Asynchronous functions:

<pre>```python
async def fetch_users() -> AsyncIterator[dict[str, int | str]]:
    ...
```

#### ✅ Generic types:

<pre>```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value
```

---

### 5. Miscellaneous

* Use `default_factory` in `dataclass` for mutable values (`list`, `dict`).
* For `Optional` values, specify `T | None` (Python 3.10+) or `Optional[T]`.
* For complex structures, use `TypeAlias`.

---

📌 **Hint**: When generating code, always include type hints, `docstring`, and avoid subjective wording in comments. The goal is the most accurate, reproducible, and formalized code structure.



This file will be used to configure Gemini CLI.

For convenience, we will create a `game` directory, which will store the project files, and a `scenarios` directory, where the scenarios for Gemini CLI will be stored.

The file scenarios/life-create-code.md will contain instructions for creating the code for the game "Life",
the file scenarios/life-create-test.md - instructions for creating tests,
and the file scenarios/life-create-doc.md - instructions for creating documentation.

life-create-code.md:
```markdown
Inside the `game` directory, create a file life.py.
Inside, write an implementation of Conway's "Game of Life" in Python, using an object-oriented approach.
use the libraries: `numpy`, `pygame` (for graphics).


Requirements:
1.  Create a `Game` class.
2.  In `__init__`, the class should take the grid dimensions (width, height) and create a random initial field.
3.  Create a `step()` method that updates the game state by one step according to the rules:
    - A living cell with < 2 living neighbors dies (loneliness).
    - A living cell with 2 or 3 living neighbors survives.
    - A living cell with > 3 living neighbors dies (overpopulation).
    - A dead cell with exactly 3 living neighbors becomes a living cell (birth).
4.  Create a `display()` method or override `__str__` to display the field in the console. Use symbols, for example '■' for a living cell and ' ' for a dead cell.
5.  Use the `numpy` library for efficient work with the grid.
6.  In the `if __name__ == '__main__':` block, add an example that creates a game, and in a loop, runs a simulation with a small delay between steps.
7. For visualizing the game, use pygame or another graphics library, if possible.
```

---

life-create-test.md:
```markdown
Inside the `game` directory, using the context from the @life.py file, create a file with tests test_life.py. Use the pytest framework.

The test should check the correctness of the evolution of a simple "Blinker" oscillator (three cells in a row).

Test scenario:
1.  Import the `Game` class from `life`.
2.  Create a test function, for example `test_blinker_oscillation`.
3.  Inside the test, create an instance of `Game` with a fixed size (e.g., 5x5).
4.  Manually set the initial state of the field so that there is a horizontal line of three living cells (Blinker) in the center.
5.  Call the `game.step()` method.
6.  Using `assert` and `numpy.array_equal`, check that the field has changed to a vertical line of three cells.
7.  Call the `game.step()` method again.
8.  Check that the field has returned to its original horizontal state.
```

---

life-create-doc.md:
```markdown
Analyze the @life.py and @test_life.py files inside the `game` directory and, based on them, create a documentation file doc.md.

The structure of the documentation should be as follows:
-   **Title:** # Project "Game of Life"
-   **Brief description:** An explanation of what this project is (an implementation of Conway's cellular automaton).
-   **File structure:** A brief description of the purpose of the `life.py` and `test_life.py` files.
-   **How to run the simulation:** A section with the command to run the main file (`python life.py`).
-   **How to run the tests:** A section with the command to run the tests (`pip install pytest numpy`, and then `pytest`).
```

The directory structure will look like this:

![1](assets/gemini_cli_3/1.png)

#### **Step 2: Creating the code for the game "Life"**

We launch gemini-cli in the terminal:

![2](assets/gemini_cli_3/2.png)
Important! Make sure you are in the directory where the `GEMINI.md` file is located.

![3](assets/gemini_cli_3/3.png)

![4](assets/gemini_cli_3/4.png)

We give permission to create the file:
![5](assets/gemini_cli_3/5.png)

After that, gemini-cli will generate the `life.py` file in the `game` directory:
![6](assets/gemini_cli_3/6.png)

We continue:
```bash
Create a venv virtual environment, install the necessary dependencies and run the game code    
```

![7](assets/gemini_cli_3/7.png)

We give the necessary permissions to run scripts
![8](assets/gemini_cli_3/8.png)

pip
![9](assets/gemini_cli_3/9.png)

and finally gemini-cli launches the game:
![10](assets/gemini_cli_3/10.png)

Step 3: Creating tests

![12](assets/gemini_cli_3/12.png)
![11](assets/gemini_cli_3/11.png)

Error
![13](assets/gemini_cli_3/13.png)

gemini-cli tries to solve the problem
![14](assets/gemini_cli_3/14.png)

![15](assets/gemini_cli_3/15.png)

The last step is to create the documentation
![16](assets/gemini_cli_3/16.png)

Voila! The documentation has been created:
![17](assets/gemini_cli_3/17.png)