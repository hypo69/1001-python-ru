
## Работа с библиотекой `subprocess` в Python


1.  **Введение:**
    *   Что такое `subprocess` и зачем он нужен?
    *   Исторический контекст: замена старых модулей (`os.system`, `os.spawn*`, `commands`).
    *   Основные задачи, решаемые с помощью `subprocess`.
2.  **Основные функции и классы:**
    *   `subprocess.run()`: Современный и рекомендуемый подход.
    *   `subprocess.Popen()`: Низкоуровневый интерфейс для максимальной гибкости.
    *   Устаревшие, но встречающиеся функции: `call()`, `check_call()`, `check_output()`.
3.  **Ключевые аргументы функций `run()` и `Popen()`:**
    *   `args`: Команда и ее аргументы.
    *   `stdin`, `stdout`, `stderr`: Управление потоками ввода/вывода.
    *   `capture_output` (для `run()`): Удобный захват вывода.
    *   `text` (или `universal_newlines`): Работа с текстом vs байтами.
    *   `shell`: Особенности и риски использования оболочки.
    *   `cwd`: Указание рабочего каталога.
    *   `env`: Настройка переменных окружения.
    *   `timeout`: Установка таймаута выполнения.
    *   `check` (для `run()`): Автоматическая проверка кода возврата.
4.  **Работа с результатами и ошибками:**
    *   Объект `CompletedProcess` (результат `run()`).
    *   Атрибуты `returncode`, `stdout`, `stderr`.
    *   Исключения: `CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`.
    *   Взаимодействие с объектом `Popen`: `communicate()`, `wait()`, `poll()`, `terminate()`, `kill()`.
5.  **Продвинутые сценарии использования:**
    *   Перенаправление вывода одной команды на ввод другой (пайплайны/конвейеры).
    *   Асинхронный запуск процессов.
    *   Интерактивное взаимодействие с процессом.
    *   Работа с кодировками.
6.  **Безопасность и лучшие практики:**
    *   Риски `shell=True` и инъекции команд.
    *   Валидация и экранирование пользовательского ввода.
    *   Передача аргументов списком.
    *   Обработка ошибок и кодов возврата.
    *   Управление ресурсами (закрытие дескрипторов, завершение процессов).
7.  **Практические примеры:**
    *   Выполнение простой команды.
    *   Захват вывода команды.
    *   Отправка данных на ввод процессу.
    *   Создание конвейера.
    *   Обработка ошибок.
8.  **Заключение и полезные ресурсы.**

---

### 1. Введение

**Что такое `subprocess` и зачем он нужен?**

Модуль `subprocess` в Python предоставляет мощный и гибкий интерфейс для создания новых процессов, подключения к их потокам ввода/вывода/ошибок и получения их кодов возврата. Он позволяет Python-скриптам запускать и управлять другими программами, написанными на любом языке, будь то системные утилиты, скрипты оболочки или другие исполняемые файлы.

**Исторический контекст:**

До появления `subprocess`, для запуска внешних процессов использовались функции из модуля `os`, такие как `os.system()`, `os.spawn*()`, а также модуль `commands` (в Python 2). Эти подходы имели ряд недостатков:
*   `os.system()`: Запускает команду через системную оболочку, что небезопасно при работе с пользовательским вводом и менее гибко в управлении потоками.
*   `os.spawn*()`: Более гибкие, но сложны в использовании и платформозависимы.
*   Модуль `popen2` (и его вариации): Предоставлял доступ к потокам, но был сложен и имел проблемы с блокировками.

Модуль `subprocess` был представлен в Python 2.4 (PEP 324) как унифицированный и более безопасный способ взаимодействия с дочерними процессами. Он инкапсулирует лучшую функциональность предыдущих модулей и предоставляет более чистый API.

**Основные задачи, решаемые с помощью `subprocess`:**

*   Выполнение команд операционной системы (например, `ls`, `dir`, `ping`).
*   Запуск внешних утилит для обработки данных (например, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Интеграция с системами контроля версий (`git`, `svn`).
*   Запуск компиляторов или интерпретаторов других языков.
*   Автоматизация системного администрирования.
*   Организация взаимодействия между различными программами.

---

### 2. Основные функции и классы

Модуль `subprocess` предлагает несколько способов запуска процессов:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   Это **рекомендуемый** высокоуровневый API, появившийся в Python 3.5.
    *   Запускает команду, ожидает ее завершения и возвращает объект `CompletedProcess`.
    *   Подходит для большинства случаев, когда нужно просто выполнить команду и получить результат.

    ```python
    import subprocess

    # Простой запуск
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Если check=True и команда вернула не 0, будет выброшено CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Это основной класс для создания и управления дочерними процессами.
    *   Предоставляет максимальную гибкость: неблокирующий запуск, детальное управление потоками ввода/вывода, возможность отправлять сигналы процессу.
    *   Функция `run()` внутри себя использует `Popen`.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Процесс запущен с PID: {process.pid}")
    # ... можно делать другую работу ...
    process.wait() # Ожидать завершения
    print(f"Процесс завершился с кодом: {process.returncode}")
    ```

*   **Устаревшие, но встречающиеся функции (до Python 3.5 были основным API):**
    *   `subprocess.call(args, ...)`: Выполняет команду и ждет ее завершения. Возвращает код возврата. Похоже на `os.system()`, но безопаснее, если `shell=False`.
    *   `subprocess.check_call(args, ...)`: Как `call()`, но выбрасывает `CalledProcessError`, если код возврата не 0.
    *   `subprocess.check_output(args, ...)`: Выполняет команду, ждет завершения и возвращает ее стандартный вывод (stdout) в виде байтовой строки. Выбрасывает `CalledProcessError`, если код возврата не 0.

    Хотя эти функции все еще работают, `subprocess.run()` предоставляет более удобный и унифицированный интерфейс для тех же задач.

---

### 3. Ключевые аргументы функций `run()` и `Popen()`

Эти аргументы позволяют тонко настроить запуск и взаимодействие с дочерним процессом:

*   **`args`**:
    *   Первый и обязательный аргумент.
    *   Может быть списком строк (рекомендуется) или одной строкой (если `shell=True`).
    *   Первый элемент списка – это имя исполняемого файла, остальные – его аргументы.
    *   Пример: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**:
    *   Определяют, как будут обрабатываться стандартный ввод, вывод и поток ошибок дочернего процесса.
    *   Возможные значения:
        *   `None` (по умолчанию): Наследуются от родительского процесса.
        *   `subprocess.PIPE`: Создается канал (pipe), через который можно обмениваться данными. `process.stdin`, `process.stdout`, `process.stderr` становятся файлоподобными объектами.
        *   `subprocess.DEVNULL`: Перенаправляет поток в "никуда" (аналог `/dev/null`).
        *   Открытый файловый дескриптор (целое число).
        *   Существующий файловый объект (например, открытый файл `open('output.txt', 'w')`).

*   **`capture_output=True` (для `run()`):**
    *   Удобная опция, эквивалентная установке `stdout=subprocess.PIPE` и `stderr=subprocess.PIPE`.
    *   Результат будет доступен в `result.stdout` и `result.stderr`.

*   **`text=True` (или `universal_newlines=True` для совместимости):**
    *   Если `True`, потоки `stdout` и `stderr` (а также `stdin`, если передается строка) будут открыты в текстовом режиме с использованием кодировки по умолчанию (обычно UTF-8). Декодирование/кодирование происходит автоматически.
    *   Если `False` (по умолчанию), потоки обрабатываются как байтовые.
    *   Начиная с Python 3.7, `text` является предпочтительным псевдонимом для `universal_newlines`. Можно также указать конкретную кодировку через `encoding` и обработчик ошибок через `errors`.

*   **`shell=False` (по умолчанию):**
    *   Если `False` (рекомендуется из соображений безопасности и предсказуемости), `args` должен быть списком. Команда запускается напрямую.
    *   Если `True`, `args` передается как строка системной оболочке (например, `/bin/sh` в Unix, `cmd.exe` в Windows) для интерпретации. Это позволяет использовать возможности оболочки (переменные, подстановки, конвейеры), но **ОПАСНО**, если `args` содержит непроверенный пользовательский ввод (риск инъекции команд).

*   **`cwd=None`:**
    *   Задает текущий рабочий каталог для дочернего процесса. По умолчанию наследуется от родительского.

*   **`env=None`:**
    *   Словарь, определяющий переменные окружения для нового процесса. По умолчанию наследуется окружение родительского процесса. Если указан, он полностью заменяет наследуемое окружение. Чтобы добавить/изменить переменные, сохранив остальные, нужно сначала скопировать `os.environ` и затем модифицировать его.

*   **`timeout=None`:**
    *   Максимальное время в секундах, отведенное на выполнение команды. Если процесс не завершится за это время, будет выброшено исключение `subprocess.TimeoutExpired`. `Popen.communicate()` также принимает `timeout`.

*   **`check=False` (для `run()`):**
    *   Если `True` и процесс завершается с ненулевым кодом возврата, будет выброшено исключение `subprocess.CalledProcessError`.

---

### 4. Работа с результатами и ошибками

**Объект `CompletedProcess` (результат `run()`):**

```python
import subprocess

try:
    # Пытаемся выполнить команду, которая может завершиться с ошибкой
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - опечатка для демонстрации ошибки
        capture_output=True,
        text=True,
        check=True, # Вызовет исключение, если returncode != 0
        timeout=10
    )
    print("Команда выполнена успешно.")
    print("Код возврата:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Обычно пуст при успехе

except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения команды (CalledProcessError):")
    print(f"  Команда: {e.cmd}")
    print(f"  Код возврата: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # Может содержать вывод до ошибки
    print(f"  Stderr: {e.stderr}") # Обычно здесь информация об ошибке
except subprocess.TimeoutExpired as e:
    print(f"Команда не завершилась за {e.timeout} секунд.")
    print(f"  Команда: {e.cmd}")
    if e.stdout: print(f"  Stdout (частичный): {e.stdout.decode(errors='ignore')}") # stdout байтовый
    if e.stderr: print(f"  Stderr (частичный): {e.stderr.decode(errors='ignore')}") # stderr байтовый
except FileNotFoundError:
    print("Ошибка: команда или программа не найдена.")
except Exception as e:
    print(f"Произошла другая ошибка: {e}")
```

**Атрибуты `CompletedProcess`:**
*   `args`: Аргументы, использованные для запуска процесса.
*   `returncode`: Код возврата процесса. 0 обычно означает успех.
*   `stdout`: Стандартный вывод процесса (байты или строка, если `text=True` и `capture_output=True`).
*   `stderr`: Стандартный поток ошибок процесса (байты или строка, если `text=True` и `capture_output=True`).

**Исключения:**
*   `subprocess.CalledProcessError`: Выбрасывается, если `check=True` (для `run()`) или используются `check_call()`, `check_output()` и команда завершилась с ненулевым кодом. Содержит `returncode`, `cmd`, `output` (или `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: Если истек таймаут. Содержит `cmd`, `timeout`, `stdout`, `stderr` (частичный вывод, если был).
*   `FileNotFoundError`: Если исполняемый файл не найден.

**Взаимодействие с объектом `Popen`:**

Класс `Popen` дает больше контроля:

```python
import subprocess
import time

# Запускаем процесс в фоновом режиме
process = subprocess.Popen(["ping", "-c", "5", "google.com"], stdout=subprocess.PIPE, text=True)

print(f"Процесс PID: {process.pid} запущен.")

# Неблокирующая проверка статуса
while process.poll() is None: # poll() возвращает None, если процесс еще работает
    print("Процесс еще работает...")
    # Можно читать вывод по мере поступления (осторожно, может блокировать!)
    # line = process.stdout.readline()
    # if line: print(f"Вывод: {line.strip()}")
    time.sleep(1)

# Ожидание завершения и получение всего вывода/ошибок
# stdout_data, stderr_data = process.communicate(timeout=10) # Безопасный способ

# Если communicate() не использовался, после poll() != None можно прочитать остатки
if process.stdout:
    for line in process.stdout:
        print(f"Финальный вывод: {line.strip()}")

print(f"Процесс завершился с кодом: {process.returncode}")

# Если нужно принудительно завершить
# process.terminate() # Отправляет SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Если не завершился
#     process.kill()      # Отправляет SIGKILL
```

*   `process.poll()`: Проверяет, завершился ли дочерний процесс. Возвращает код возврата или `None`. Неблокирующий.
*   `process.wait(timeout=None)`: Ожидает завершения дочернего процесса. Возвращает код возврата. Блокирующий.
*   `process.communicate(input=None, timeout=None)`:
    *   Самый безопасный способ взаимодействия с процессом, когда используются `PIPE`.
    *   Отправляет данные в `stdin` (если `input` указан), читает все данные из `stdout` и `stderr` до конца и ждет завершения процесса.
    *   Возвращает кортеж `(stdout_data, stderr_data)`.
    *   Помогает избежать дедлоков, которые могут возникнуть при прямом чтении/записи в `process.stdout`/`process.stdin`, если буферы переполняются.
*   `process.terminate()`: Отправляет сигнал `SIGTERM` процессу (мягкое завершение).
*   `process.kill()`: Отправляет сигнал `SIGKILL` процессу (жесткое завершение).
*   `process.send_signal(signal)`: Отправляет указанный сигнал процессу.
*   `process.stdin`, `process.stdout`, `process.stderr`: Файлоподобные объекты для каналов, если они были созданы с `PIPE`.

---

### 5. Продвинутые сценарии использования

**Перенаправление вывода одной команды на ввод другой (пайплайны/конвейеры):**

Эмулируем `ps aux | grep python`:

```python
import subprocess

# Запускаем первую команду, ее stdout будет PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Запускаем вторую команду, ее stdin будет stdout первой команды
# stdout второй команды тоже PIPE, чтобы прочитать результат
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Связываем stdout от ps с stdin для grep
    stdout=subprocess.PIPE,
    text=True
)

# Важно! Закрыть stdout первой команды в родительском процессе,
# чтобы grep получил EOF, когда ps завершится.
if ps_process.stdout:
    ps_process.stdout.close()

# Получаем вывод от grep
stdout_data, stderr_data = grep_process.communicate()

print("Результат конвейера:")
print(stdout_data)

if stderr_data:
    print("Ошибки grep:", stderr_data)

# Убедимся, что оба процесса завершились
ps_process.wait()
# grep_process.wait() # communicate() уже дождался
print(f"ps return code: {ps_process.returncode}")
print(f"grep return code: {grep_process.returncode}")
```
*Примечание:* Для простых конвейеров `subprocess.run("ps aux | grep python", shell=True, ...)` может быть проще, но менее безопасно и гибко.

**Асинхронный запуск процессов:**

`Popen` по своей природе неблокирующий. Вы можете запустить несколько процессов и управлять ими параллельно.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Команда с ошибкой
]

processes = []
for cmd_args in commands:
    print(f"Запускаем: {' '.join(cmd_args)}")
    # Для асинхронности stdout/stderr лучше перенаправить,
    # чтобы не мешать друг другу или консоли родителя.
    # DEVNULL если вывод не нужен, PIPE если нужен позже.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Делаем другую работу или ждем завершения
while any(p.poll() is None for p in processes):
    print("Ожидание завершения всех процессов...")
    time.sleep(0.5)

print("\nРезультаты:")
for i, p in enumerate(processes):
    print(f"Команда '{' '.join(commands[i])}' завершилась с кодом: {p.returncode}")
```

**Интерактивное взаимодействие с процессом:**

Это сложная задача, требующая осторожного управления потоками, чтобы избежать блокировок. `communicate()` хорош для однократного обмена. Для длительного интерактивного сеанса может потребоваться прямое чтение/запись в `p.stdin`, `p.stdout`, `p.stderr` с использованием неблокирующего I/O или отдельных потоков.

```python
import subprocess

# Пример: запуск интерактивной python сессии
process = subprocess.Popen(
    ['python', '-i'], # -i для интерактивного режима
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Линейная буферизация для stdout/stderr (для интерактивности)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Важно!

def read_output():
    # Чтение вывода может быть сложным, т.к. нужно знать, когда остановиться.
    # Здесь очень упрощенный пример. Для реальных задач нужны более robust решения.
    # Например, читать до определенного паттерна (приглашения командной строки).
    output = ""
    # Читаем stdout. В реальном приложении это нужно делать неблокирующим способом или в отдельном потоке.
    # Здесь мы предполагаем, что после команды сразу будет какой-то вывод.
    # Это очень хрупкое предположение для общего случая!
    try:
        # У Popen нет readline с таймаутом, это одна из сложностей
        # Можно использовать select на process.stdout.fileno()
        # или читать посимвольно/построчно в отдельном потоке
        # Для простоты здесь этого нет
        while True: # Осторожно, может заблокироваться!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Примитивный детектор приглашения
                output += line
                break
            output += line
    except Exception as e:
        print(f"Ошибка чтения: {e}")
    return output.strip()

# Инициализация: прочитать первоначальное приглашение
initial_output = ""
# Чтение приветствия Python
# Это очень упрощенно, т.к. мы не знаем точно, сколько строк читать
for _ in range(5): # Попытаемся прочитать несколько строк
    try:
        # У Popen stdout нет timeout, нужно читать осторожно
        # stdout.readline() может заблокироваться.
        # В реальных приложениях здесь нужен select или потоки.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Нашли приглашение
    except BlockingIOError:
        break # Если бы было неблокирующее чтение
print(f"Initial output:\n{initial_output.strip()}")


send_command("a = 10")
# Для интерактивного взаимодействия чтение вывода - самая сложная часть.
# communicate() не подходит, т.к. он закрывает потоки.
# Нужно аккуратно читать из process.stdout и process.stderr,
# возможно, в отдельных потоках, чтобы не блокировать основной.
# Этот пример НЕ является production-ready для сложного интерактива.
# print(read_output()) # Этот read_output очень примитивен

send_command("print(a * 2)")
# print(read_output())

# Завершаем процесс
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Дождаться завершения и собрать остатки

print("\nFinal stdout:")
print(stdout_data)
if stderr_data:
    print("\nFinal stderr:")
    print(stderr_data)

print(f"Python process finished with code: {process.returncode}")

# Для настоящего интерактивного взаимодействия часто используют pty (псевдотерминалы)
# через модуль `pty` в Unix-like системах, или библиотеки типа `pexpect`.
```
*Предупреждение*: Прямое интерактивное взаимодействие с `Popen` через `stdin`/`stdout`/`stderr` сложно из-за блокировок и буферизации. Для надежного интерактива часто используют библиотеки вроде `pexpect` (для Unix) или аналоги, которые работают с псевдотерминалами (pty).

**Работа с кодировками:**
*   Используйте `text=True` (или `universal_newlines=True`) для автоматического декодирования/кодирования.
*   При необходимости можно указать `encoding="ваша-кодировка"` и `errors="обработчик-ошибок"` (например, `replace`, `ignore`).
*   Если `text=False` (по умолчанию), `stdout` и `stderr` будут байтовыми строками. Их нужно будет декодировать вручную: `result.stdout.decode('utf-8', errors='replace')`.

---

### 6. Безопасность и лучшие практики

*   **Риски `shell=True` и инъекции команд:**
    *   **Никогда** не используйте `shell=True` с командами, построенными из непроверенного пользовательского ввода. Это открывает путь к инъекции команд.
    *   Пример уязвимости:
        ```python
        # ОПАСНО!
        filename = input("Введите имя файла для удаления: ") # Пользователь вводит "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Если `shell=True` абсолютно необходим (например, для использования пайпов `|` или подстановок `*` прямо в строке команды), тщательно экранируйте все части команды, формируемые извне, с помощью `shlex.quote()` (начиная с Python 3.3).

*   **Валидация и экранирование пользовательского ввода:**
    *   Даже если `shell=False`, если аргументы команды формируются из пользовательского ввода, их следует валидировать. Например, если ожидается имя файла, убедитесь, что это действительно допустимое имя файла, а не что-то вроде `../../../etc/passwd`.

*   **Передача аргументов списком (когда `shell=False`):**
    *   Это самый безопасный способ. Каждый аргумент передается как отдельный элемент списка, и операционная система обрабатывает их корректно, не пытаясь интерпретировать как часть команды оболочки.
    *   Пример: `subprocess.run(["rm", filename_from_user])` — здесь `filename_from_user` будет всегда трактоваться как один аргумент (имя файла), даже если содержит пробелы или спецсимволы.

*   **Обработка ошибок и кодов возврата:**
    *   Всегда проверяйте `returncode` или используйте `check=True` (для `run()`) / `check_call()` / `check_output()`, чтобы убедиться, что команда выполнилась успешно.
    *   Обрабатывайте возможные исключения (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Управление ресурсами:**
    *   Если вы открываете каналы (`PIPE`), убедитесь, что они в конечном итоге закрываются. `Popen.communicate()` делает это автоматически. Если вы работаете с `p.stdin/stdout/stderr` напрямую, может потребоваться их явное закрытие.
    *   В долгоживущих приложениях убедитесь, что дочерние процессы корректно завершаются и не становятся "зомби". Используйте `p.wait()` или `p.communicate()`. При необходимости используйте `p.terminate()` или `p.kill()`.

*   **Кодировки:** Будьте внимательны к кодировкам при использовании `text=True` или при ручном декодировании байтовых строк. Проблемы с кодировками – частый источник ошибок.

---

### 7. Практические примеры

**1. Выполнение простой команды и проверка кода возврата:**
```python
import subprocess

try:
    # Запускаем 'ls' для существующего каталога
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Команда 'ls /tmp' выполнена, код возврата: {result.returncode}")

    # Запускаем 'ls' для несуществующего каталога
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Эта строка не выполнится, если check=True, т.к. будет исключение
except subprocess.CalledProcessError as e:
    print(f"Ошибка выполнения команды: {e.cmd}")
    print(f"Код возврата: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. Захват вывода команды:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Укажем текущий каталог как рабочий для git
    )
    print("Статус Git:")
    print(result.stdout)
except FileNotFoundError:
    print("Ошибка: команда 'git' не найдена. Установлен ли Git и есть ли он в PATH?")
except subprocess.CalledProcessError as e:
    print(f"Ошибка git: {e.stderr}")
```

**3. Отправка данных на ввод процессу (используя `communicate`):**
```python
import subprocess

# Отправляем текст в 'grep' для поиска
input_text = "hello world\npython is fun\nhello python"
try:
    process = subprocess.Popen(
        ["grep", "python"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout_data, stderr_data = process.communicate(input=input_text, timeout=5)

    if process.returncode == 0: # grep нашел совпадения
        print("Найденные строки:")
        print(stdout_data)
    elif process.returncode == 1: # grep не нашел совпадений
        print("Совпадения 'python' не найдены.")
    else: # другая ошибка grep
        print(f"Ошибка grep (код {process.returncode}):")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep не ответил вовремя.")
    process.kill() # Убить процесс, если он завис
    process.communicate() # Собрать оставшийся вывод/ошибки
```

**4. Создание конвейера (`ls -l | wc -l`) без `shell=True`:**
(Более подробный пример был в разделе 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Убедимся, что stdout существует
    ls_proc.stdout.close()  # Позволяет wc_proc получить EOF когда ls_proc закончит

output, _ = wc_proc.communicate()
print(f"Количество файлов/каталогов: {output.strip()}")
```

**5. Использование `timeout`:**
```python
import subprocess

try:
    # Команда, которая будет выполняться 5 секунд
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Команда 'sleep 5' завершилась (не должна была при timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Команда '{e.cmd}' не завершилась за {e.timeout} секунд.")
```

---

### 8. Заключение и полезные ресурсы

Модуль `subprocess` является незаменимым инструментом для любого Python-разработчика, которому необходимо взаимодействовать с внешними программами или системной средой. Он предлагает баланс между простотой использования (через `subprocess.run()`) и мощной гибкостью (через `subprocess.Popen()`).

**Ключевые моменты:**
*   Предпочитайте `subprocess.run()` для большинства задач.
*   Используйте `subprocess.Popen()` для асинхронного выполнения или сложного управления потоками.
*   **Избегайте `shell=True`**, особенно с пользовательским вводом, из-за рисков безопасности. Передавайте команды списком аргументов.
*   Всегда обрабатывайте коды возврата и возможные исключения.
*   Будьте внимательны к кодировкам при работе с текстовым выводом (`text=True` или ручное декодирование).
*   `communicate()` — ваш друг для безопасного обмена данными через `PIPE`.

**Полезные ресурсы:**
*   Официальная документация Python по модулю `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - A New Process Module: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)

