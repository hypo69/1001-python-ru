# 🧲 Как «поймать» print() в Python: перехватываем stdout без сторонних библиотек

В Python можно перехватить то, что выводится на экран через `print()`. Особенно когда:
Я покажу, как элегантно решить эту задачу — без сторонних зависимостей, с помощью стандартной библиотеки и пары строк кода.

---

## 📦 Мини-контекст: перехват stdout

Самый простой способ — временно переназначить `sys.stdout` на `io.StringIO()` внутри контекстного менеджера:

```python
from contextlib import contextmanager
import sys
import io

@contextmanager
def capture_stdout():
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout
```

Пример использования:

```python
with capture_stdout() as out:
    print("Это вывод, который перехвачен")

print("Результат:", out.getvalue())
```

---

## 🔧 Хочется больше контроля?

Вот ещё полезные варианты:

### 💬 Перехват `stderr`

```python
@contextmanager
def capture_stderr():
    old = sys.stderr
    sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stderr = old
```

### 🔁 Объединённый stdout + stderr

```python
@contextmanager
def capture_output():
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
```

---

## 💡 Примеры из жизни

### ✅ Тестируем вывод функции

```python
def say_hello(name):
    print(f"Hello, {name}!")

with capture_stdout() as out:
    say_hello("Pythonista")

assert "Hello, Pythonista!" in out.getvalue()
```

### 🔕 Подавляем шумный вывод

```python
with capture_stdout():
    import noisy_library
```

### 📝 Логируем результат внешней команды

```python
with capture_output() as out:
    run_some_cli_tool()

with open("cli_output.log", "w") as f:
    f.write(out.getvalue())
```

---

## 🔀 А если нужно и видеть, и перехватывать?

Иногда хочется, чтобы `print()` **и отображался в терминале, и сохранялся**. Это можно сделать через `Tee`-объект:

```python
class Tee(io.StringIO):
    def __init__(self, original):
        super().__init__()
        self.original = original

    def write(self, text):
        self.original.write(text)
        super().write(text)

@contextmanager
def capture_stdout_tee():
    old_stdout = sys.stdout
    sys.stdout = tee = Tee(old_stdout)
    try:
        yield tee
    finally:
        sys.stdout = old_stdout
```

Пример:

```python
with capture_stdout_tee() as out:
    print("Этот вывод виден и в терминале, и в логе")

print("Из буфера:", out.getvalue())
```

Соберём из всех вышеописанных идей **полезную, самодостаточную утилиту** для перехвата вывода в Python, которую можно:

* импортировать в любой проект,
* использовать для тестов, логирования и отладки,
* легко расширять.

---

## 📦 Файл: `stdout_capture.py`

```python
"""
stdout_capture.py

Утилита для перехвата stdout и stderr с помощью контекстных менеджеров.

Поддерживает:
- перехват stdout;
- перехват stderr;
- объединённый перехват stdout + stderr;
- режим "tee" — одновременный вывод в терминал и в буфер.

Не требует сторонних библиотек.
"""

import sys
import io
from contextlib import contextmanager


@contextmanager
def capture_stdout():
    """
    Перехватывает stdout (print).
    """
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout


@contextmanager
def capture_stderr():
    """
    Перехватывает stderr (ошибки и исключения).
    """
    old_stderr = sys.stderr
    sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stderr = old_stderr


@contextmanager
def capture_output():
    """
    Перехватывает stdout и stderr одновременно.
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = sys.stderr = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


class Tee(io.StringIO):
    """
    Tee-класс: сохраняет вывод и передаёт его в оригинальный stdout/stderr.
    """
    def __init__(self, original):
        super().__init__()
        self.original = original

    def write(self, text):
        self.original.write(text)
        super().write(text)

    def flush(self):
        self.original.flush()


@contextmanager
def capture_stdout_tee():
    """
    Tee-перехват stdout — сохраняет и отображает одновременно.
    """
    old_stdout = sys.stdout
    sys.stdout = tee = Tee(old_stdout)
    try:
        yield tee
    finally:
        sys.stdout = old_stdout


@contextmanager
def capture_output_tee():
    """
    Tee-перехват stdout и stderr — сохраняет и отображает одновременно.
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = sys.stderr = tee = Tee(old_stdout)
    try:
        yield tee
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
```

---

## ✅ Примеры использования

```python
from stdout_capture import capture_stdout, capture_output, capture_stdout_tee


def test_func():
    print("Hello from function")


# Простой перехват
with capture_stdout() as out:
    test_func()

print("Captured:", out.getvalue())


# Объединённый stdout + stderr
with capture_output() as out:
    print("Something")
    raise Exception("Oops")  # будет тоже перехвачено

# Сохранение вывода и одновременное отображение
with capture_stdout_tee() as out:
    print("Visible AND captured")

print("Tee captured:", out.getvalue())
```

