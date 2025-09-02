### `question_817.md`
**Вопрос 817**

При создании Python-приложения, которое должно корректно завершать свою работу при получении сигнала `SIGINT` (например, при нажатии CTRL+C), какой из следующих фрагментов кода *наиболее* правильно использует модуль `signal` для регистрации обработчика сигнала?

**Варианты ответа:**

*   **A:**
    ```python
    import signal

    def handler(signum, frame):
        print("Сигнал получен!")

    signal.signal(signal.SIGINT, handler())
    ```

*   **B:**
    ```python
    import signal

    def handler(signum, frame):
        print("Сигнал получен!")

    signal.signal(signal.SIGINT, handler)
    ```

*   **C:**
    ```python
    import signal

    def handler():
        print("Сигнал получен!")

    signal.signal(signal.SIGINT, handler)
    ```

*   **D:**
    ```python
    import signal

    def handler(signum):
        print("Сигнал получен!")

    signal.signal(signal.SIGINT, handler)
    ```

**Верный ответ:**

*   **B**

**Объяснение:**

Функция `signal.signal()` принимает два аргумента: номер сигнала (например, `signal.SIGINT`) и *функцию-обработчик*. Важно передать *саму функцию* (ее имя) в качестве аргумента, а не результат ее вызова. Вариант B передает `handler`, что является правильным.  Вариант A передает `handler()`, что вызовет функцию немедленно и передаст результат ее выполнения (в данном случае, `None`) в `signal.signal()`, что приведет к ошибке или некорректной работе. Функция обработчик должна принимать 2 аргумента.

**Пример:**

```python
import signal
import time

def handler(signum, frame):
    print("Сигнал SIGINT получен! Завершаю программу...")
    exit(0)

signal.signal(signal.SIGINT, handler)

print("Программа запущена. Нажмите CTRL+C для завершения.")

while True:
    print("Работаю...")
    time.sleep(1)
```

В этом примере, когда пользователь нажимает CTRL+C, функция `handler` будет вызвана, напечатает сообщение и завершит программу.

