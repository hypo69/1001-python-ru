## Робота з бібліотекою `subprocess` у Python


### 1. **Що таке `subprocess` і навіщо він потрібен?**

Модуль `subprocess` у Python надає інтерфейс для створення нових процесів,
підключення до їхніх потоків введення/виведення/помилок та отримання їхніх кодів повернення.
Він дозволяє скриптам Python запускати та керувати іншими програмами,
написаними будь-якою мовою, будь то системні утиліти, скрипти оболонки або інші виконувані файли.

**Історичний контекст:**

До появи `subprocess` для запуску зовнішніх процесів використовувалися функції з модуля `os`, такі як `os.system()`, `os.spawn*()`, а також модуль `commands` (у Python 2). Ці підходи мали низку недоліків:
*   `os.system()`: Запускає команду через системну оболонку, що є небезпечним при роботі з введенням користувача та менш гнучким у керуванні потоками.
*   `os.spawn*()`: Більш гнучкі, але складні у використанні та залежні від платформи.
*   Модуль `popen2` (та його варіації): Надавав доступ до потоків, але був складним і мав проблеми з взаємними блокуваннями.

Модуль `subprocess` був представлений у Python 2.4 (PEP 324) як уніфікований та безпечніший спосіб взаємодії з дочірніми процесами. Він інкапсулює найкращі функції попередніх модулів і надає чистіший API.

**Основні завдання, що вирішуються за допомогою `subprocess`:**

*   Виконання команд операційної системи (наприклад, `ls`, `dir`, `ping`).
*   Запуск зовнішніх утиліт для обробки даних (наприклад, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Інтеграція з системами контролю версій (`git`, `svn`).
*   Запуск компіляторів або інтерпретаторів інших мов.
*   Автоматизація системного адміністрування.
*   Організація взаємодії між різними програмами.

---

### 2. Основні функції та класи

Модуль `subprocess` пропонує кілька способів запуску процесів:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   Це **рекомендований** високорівневий API, представлений у Python 3.5.
    *   Запускає команду, чекає її завершення та повертає об'єкт `CompletedProcess`.
    *   Підходить для більшості випадків, коли вам просто потрібно виконати команду та отримати результат.

    ```python
    import subprocess

    # Простий запуск
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Якщо check=True і команда повернула ненульове значення, буде викликано CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Це основний клас для створення та керування дочірніми процесами.
    *   Забезпечує максимальну гнучкість: неблокуюче виконання, детальний контроль потоків вводу/виводу, можливість надсилати сигнали процесу.
    *   Функція `run()` використовує `Popen` внутрішньо.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Процес запущено з PID: {process.pid}")
    # ... можна виконувати іншу роботу ...
    process.wait() # Чекати завершення
    print(f"Процес завершився з кодом: {process.returncode}")
    ```

*   **Застарілі, але все ще зустрічаються функції (були основним API до Python 3.5):**
    *   `subprocess.call(args, ...)`: Виконує команду та чекає її завершення. Повертає код повернення. Схоже на `os.system()`, але безпечніше, якщо `shell=False`.
    *   `subprocess.check_call(args, ...)`: Як `call()`, але викликає `CalledProcessError`, якщо код повернення не 0.
    *   `subprocess.check_output(args, ...)`: Виконує команду, чекає завершення та повертає її стандартний вивід (stdout) як байтовий рядок. Викликає `CalledProcessError`, якщо код повернення не 0.

    Хоча ці функції все ще працюють, `subprocess.run()` надає більш зручний та уніфікований інтерфейс для тих самих завдань.

---

### 3. Ключові аргументи функцій `run()` та `Popen()`

Ці аргументи дозволяють точно налаштувати запуск та взаємодію з дочірнім процесом:

*   **`args`**:
    *   Перший і обов'язковий аргумент.
    *   Може бути списком рядків (рекомендовано) або одним рядком (якщо `shell=True`).
    *   Перший елемент списку — це ім'я виконуваного файлу, решта — його аргументи.
    *   Приклад: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**:
    *   Визначають, як будуть оброблятися стандартні потоки введення, виведення та помилок дочірнього процесу.
    *   Можливі значення:
        *   `None` (за замовчуванням): Успадковується від батьківського процесу.
        *   `subprocess.PIPE`: Створюється канал, через який можна обмінюватися даними. `process.stdin`, `process.stdout`, `process.stderr` стають об'єктами, схожими на файли.
        *   `subprocess.DEVNULL`: Перенаправляє потік у "нікуди" (аналогічно `/dev/null`).
        *   Відкритий файловий дескриптор (ціле число).
        *   Існуючий файловий об'єкт (наприклад, відкритий файл `open('output.txt', 'w')`).

*   **`capture_output=True` (для `run()`):**
    *   Зручна опція, еквівалентна встановленню `stdout=subprocess.PIPE` та `stderr=subprocess.PIPE`.
    *   Результат буде доступний у `result.stdout` та `result.stderr`.

*   **`text=True` (або `universal_newlines=True` для сумісності):**
    *   Якщо `True`, потоки `stdout` та `stderr` (а також `stdin`, якщо передається рядок) будуть відкриті в текстовому режимі з використанням кодування за замовчуванням (зазвичай UTF-8). Декодування/кодування відбувається автоматично.
    *   Якщо `False` (за замовчуванням), потоки обробляються як байти.
    *   З Python 3.7 `text` є кращим псевдонімом для `universal_newlines`. Ви також можете вказати конкретне кодування через `encoding` та обробник помилок через `errors`.

*   **`shell=False` (за замовчуванням):**
    *   Якщо `False` (рекомендовано для безпеки та передбачуваності), `args` має бути списком. Команда запускається безпосередньо.
    *   Якщо `True`, `args` передається як рядок системній оболонці (наприклад, `/bin/sh` у Unix, `cmd.exe` у Windows) для інтерпретації. Це дозволяє використовувати функції оболонки (змінні, підстановки, конвеєри), але є **НЕБЕЗПЕЧНИМ**, якщо `args` містить ненадійне введення користувача (ризик ін'єкції команд).

*   **`cwd=None`:**
    *   Встановлює поточний робочий каталог для дочірнього процесу. За замовчуванням успадковується від батьківського.

*   **`env=None`:**
    *   Словник, який визначає змінні середовища для нового процесу. За замовчуванням успадковується середовище батьківського процесу. Якщо вказано, він повністю замінює успадковане середовище. Щоб додати/змінити змінні, зберігаючи решту, ви повинні спочатку скопіювати `os.environ`, а потім змінити його.

*   **`timeout=None`:**
    *   Максимальний час у секундах, відведений для виконання команди. Якщо процес не завершиться протягом цього часу, буде викликано виняток `subprocess.TimeoutExpired`. `Popen.communicate()` також приймає `timeout`.

*   **`check=False` (для `run()`):**
    *   Якщо `True` і процес завершується з ненульовим кодом повернення, буде викликано виняток `subprocess.CalledProcessError`.

---

### 4. Робота з результатами та помилками

**Об'єкт `CompletedProcess` (результат `run()`):**

```python
import subprocess

try:
    # Спроба виконати команду, яка може завершитися помилкою
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - друкарська помилка для демонстрації помилки
        capture_output=True,
        text=True,
        check=True, # Викличе виняток, якщо returncode != 0
        timeout=10
    )
    print("Команду виконано успішно.")
    print("Код повернення:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Зазвичай порожній у разі успіху

except subprocess.CalledProcessError as e:
    print(f"Помилка виконання команди (CalledProcessError):")
    print(f"  Команда: {e.cmd}")
    print(f"  Код повернення: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # Може містити вивід до помилки
    print(f"  Stderr: {e.stderr}") # Зазвичай містить інформацію про помилку
except subprocess.TimeoutExpired as e:
    print(f"Команда не завершилася за {e.timeout} секунд.")
    print(f"  Команда: {e.cmd}")
    if e.stdout: print(f"  Stdout (частковий): {e.stdout.decode(errors='ignore')}") # stdout - байти
    if e.stderr: print(f"  Stderr (частковий): {e.stderr.decode(errors='ignore')}") # stderr - байти
except FileNotFoundError:
    print("Помилка: команду або програму не знайдено.")
except Exception as e:
    print(f"Виникла інша помилка: {e}")
```

**Атрибути `CompletedProcess`:**
*   `args`: Аргументи, використані для запуску процесу.
*   `returncode`: Код повернення процесу. 0 зазвичай означає успіх.
*   `stdout`: Стандартний вивід процесу (байти або рядок, якщо `text=True` та `capture_output=True`).
*   `stderr`: Стандартний потік помилок процесу (байти або рядок, якщо `text=True` та `capture_output=True`).

**Винятки:**
*   `subprocess.CalledProcessError`: Викликається, якщо `check=True` (для `run()`) або використовуються `check_call()`, `check_output()` і команда завершується з ненульовим кодом. Містить `returncode`, `cmd`, `output` (або `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: Якщо час очікування минув. Містить `cmd`, `timeout`, `stdout`, `stderr` (частковий вивід, якщо є).
*   `FileNotFoundError`: Якщо виконуваний файл не знайдено.

**Взаємодія з об'єктом `Popen`:**

Клас `Popen` дає більше контролю:

```python
import subprocess
import time

# Запуск процесу у фоновому режимі
process = subprocess.Popen(["sleep", "5"])
print(f"PID процесу: {process.pid} запущено.")

# Неблокуюча перевірка стану
while process.poll() is None: # poll() повертає None, якщо процес все ще працює
    print("Процес все ще працює...")
    # Ви можете читати вивід по мірі надходження (будьте обережні, це може заблокувати!)
    # line = process.stdout.readline()
    # if line: print(f"Вивід: {line.strip()}")
    time.sleep(1)

# Чекати завершення та отримати весь вивід/помилки
# stdout_data, stderr_data = process.communicate(timeout=10) # Безпечний спосіб

# Якщо communicate() не використовувався, після poll() != None ви можете прочитати решту
if process.stdout:
    for line in process.stdout:
        print(f"Кінцевий вивід: {line.strip()}")

print(f"Процес завершився з кодом: {process.returncode}")

# Якщо потрібно примусово завершити
# process.terminate() # Надсилає SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Якщо він не завершився
#     process.kill()      # Надсилає SIGKILL
```

*   `process.poll()`: Перевіряє, чи завершився дочірній процес. Повертає код повернення або `None`. Неблокуючий.
*   `process.wait(timeout=None)`: Чекає завершення дочірнього процесу. Повертає код повернення. Блокуючий.
*   `process.communicate(input=None, timeout=None)`:
    *   Найбезпечніший спосіб взаємодії з процесом при використанні `PIPE`.
    *   Надсилає дані до `stdin` (якщо вказано `input`), читає всі дані з `stdout` та `stderr` до кінця та чекає завершення процесу.
    *   Повертає кортеж `(stdout_data, stderr_data)`.
    *   Допомагає уникнути взаємних блокувань, які можуть виникнути при прямому читанні/записі до `process.stdout`/`process.stdin`, якщо буфери переповнюються.
*   `process.terminate()`: Надсилає сигнал `SIGTERM` процесу (м'яке завершення).
*   `process.kill()`: Надсилає сигнал `SIGKILL` процесу (жорстке завершення).
*   `process.send_signal(signal)`: Надсилає вказаний сигнал процесу.
*   `process.stdin`, `process.stdout`, `process.stderr`: Об'єкти, схожі на файли, для каналів, якщо вони були створені за допомогою `PIPE`.

---

### 5. Розширені сценарії використання

**Перенаправлення виводу однієї команди на ввід іншої (конвеєри):**

Емуляція `ps aux | grep python`:

```python
import subprocess

# Запуск першої команди, її stdout буде PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Запуск другої команди, її stdin буде stdout першої команди
# Stdout другої команди також є PIPE для читання результату
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Зв'язати stdout з ps до stdin для grep
    stdout=subprocess.PIPE,
    text=True
)

# Важливо! Закрити stdout першої команди в батьківському процесі,
# щоб grep отримав EOF, коли ps завершиться.
if ps_process.stdout:
    ps_process.stdout.close()  

# Отримати вивід від grep
stdout_data, stderr_data = grep_process.communicate()

print("Результат конвеєра:")
print(stdout_data)

if stderr_data:
    print("Помилки grep:", stderr_data)

# Переконайтеся, що обидва процеси завершилися
ps_process.wait() 
# grep_process.wait() # communicate() вже чекав
print(f"Код повернення ps: {ps_process.returncode}")
print(f"Код повернення grep: {grep_process.returncode}")
```
*Примітка:* Для простих конвеєрів `subprocess.run("ps aux | grep python", shell=True, ...)` може бути простішим, але менш безпечним та гнучким.

**Асинхронне виконання процесу:**

`Popen` за своєю природою неблокуючий. Ви можете запускати кілька процесів і керувати ними паралельно.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Команда з помилкою
]

processes = []
for cmd_args in commands:
    print(f"Виконується: {' '.join(cmd_args)}")
    # Для асинхронності краще перенаправляти stdout/stderr,
    # щоб не заважати один одному або консолі батьківського процесу.
    # DEVNULL, якщо вивід не потрібен, PIPE, якщо він потрібен пізніше.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Виконати іншу роботу або чекати завершення
while any(p.poll() is None for p in processes):
    print("Чекаємо завершення всіх процесів...")
    time.sleep(0.5)

print("\nРезультати:")
for i, p in enumerate(processes):
    print(f"Команда '{' '.join(commands[i])}' завершилася з кодом: {p.returncode}")
```

**Інтерактивна взаємодія з процесом:**

Це складне завдання, яке вимагає ретельного керування потоками, щоб уникнути взаємних блокувань. `communicate()` добре підходить для одноразового обміну. Для тривалої інтерактивної сесії вам може знадобитися читати/записувати безпосередньо до `p.stdin`, `p.stdout`, `p.stderr` за допомогою неблокуючого вводу/виводу або окремих потоків.

```python
import subprocess

# Приклад: запуск інтерактивної сесії python
process = subprocess.Popen(
    ['python', '-i'], # -i для інтерактивного режиму
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Буферизація рядків для stdout/stderr (для інтерактивності)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Важливо!

def read_output():
    # Читання виводу може бути складним, оскільки потрібно знати, коли зупинитися.
    # Це дуже спрощений приклад. Для реальних завдань потрібні більш надійні рішення.
    # Наприклад, читати до певного шаблону (підказка командного рядка).
    output = ""
    # Читання stdout. У реальному додатку це має бути зроблено неблокуючим способом або в окремому потоці.
    # Тут ми припускаємо, що після команди відразу буде якийсь вивід.
    # Це дуже крихке припущення для загального випадку!
    try:
        # Popen не має readline з таймаутом, це одна з труднощів
        # Ви можете використовувати select на process.stdout.fileno()
        # або читати символ за символом/рядок за рядком в окремому потоці
        # Для простоти, цього тут немає
        while True: # Будьте обережні, це може заблокувати!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Примітивний детектор підказки
                output += line
                break
            output += line
    except Exception as e:
        print(f"Помилка читання: {e}")
    return output.strip()

# Ініціалізація: читання початкової підказки
initial_output = ""
# Читання привітального повідомлення Python
# Це дуже спрощено, оскільки ми не знаємо точно, скільки рядків читати
for _ in range(5): # Спробуємо прочитати кілька рядків
    try:
        # Popen stdout не має таймауту, потрібно читати обережно
        # stdout.readline() може заблокувати.
        # У реальних додатках тут потрібні select або потоки.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Знайдено підказку
    except BlockingIOError:
        break # Якщо було неблокуюче читання
print(f"Початковий вивід:\n{initial_output.strip()}")


send_command("a = 10")
# Для інтерактивної взаємодії читання виводу є найскладнішою частиною.
# communicate() не підходить, оскільки він закриває потоки.
# Вам потрібно ретельно читати з process.stdout та process.stderr, 
# можливо, в окремих потоках, щоб не блокувати основний.
# Цей приклад НЕ готовий до виробництва для складної інтерактивності.
# print(read_output()) # Цей read_output дуже примітивний

send_command("print(a * 2)")
# print(read_output())

# Завершити процес
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Чекати завершення та зібрати решту

print("\nКінцевий стандартний вивід:")
print(stdout_data)
if stderr_data:
    print("\nКінцевий стандартний вивід помилок:")
    print(stderr_data)

print(f"Процес Python завершився з кодом: {process.returncode}")

# Для реальної інтерактивної взаємодії часто використовуються pty (псевдотермінали)
# через модуль `pty` у Unix-подібних системах або бібліотеки, такі як `pexpect`.
```
*Попередження*: Пряма інтерактивна взаємодія з `Popen` через `stdin`/`stdout`/`stderr` є складною через взаємні блокування та буферизацію. Для надійної інтерактивності часто використовуються бібліотеки, такі як `pexpect` (для Unix) або аналогічні, які працюють з псевдотерміналами (pty).

**Робота з кодуваннями:**
*   Використовуйте `text=True` (або `universal_newlines=True`) для автоматичного декодування/кодування.
*   За потреби ви можете вказати `encoding="ваше-кодування"` та `errors="обробник-помилок"` (наприклад, `replace`, `ignore`).
*   Якщо `text=False` (за замовчуванням), `stdout` та `stderr` будуть байтовими рядками. Вам потрібно буде декодувати їх вручну: `result.stdout.decode('utf-8', errors='replace')`.

---

### 6. Безпека та найкращі практики

*   **Ризики `shell=True` та ін'єкції команд:**
    *   **Ніколи** не використовуйте `shell=True` з командами, створеними з ненадійного введення користувача. Це відкриває шлях для ін'єкції команд.
    *   Приклад вразливості:
        ```python
        # НЕБЕЗПЕЧНО!
        filename = input("Введіть ім'я файлу для видалення: ") # Користувач вводить "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Якщо `shell=True` абсолютно необхідний (наприклад, для використання каналів `|` або символів підстановки `*` безпосередньо в командному рядку), ретельно екрануйте всі частини команди, сформовані ззовні, за допомогою `shlex.quote()` (з Python 3.3).

*   **Валідація та екранування введення користувача:**
    *   Навіть якщо `shell=False`, якщо аргументи команди формуються з введення користувача, їх слід перевіряти. Наприклад, якщо очікується ім'я файлу, переконайтеся, що це дійсне ім'я файлу, а не щось на кшталт `../../../etc/passwd`.

*   **Передача аргументів як списку (коли `shell=False`):**
    *   Це найбезпечніший спосіб. Кожен аргумент передається як окремий елемент списку, і операційна система обробляє їх правильно, не намагаючись інтерпретувати їх як частину команди оболонки.
    *   Приклад: `subprocess.run(["rm", filename_from_user])` — тут `filename_from_user` завжди буде розглядатися як один аргумент (ім'я файлу), навіть якщо він містить пробіли або спеціальні символи.

*   **Обробка помилок та кодів повернення:**
    *   Завжди перевіряйте `returncode` або використовуйте `check=True` (для `run()`) / `check_call()` / `check_output()`, щоб переконатися, що команда виконана успішно.
    *   Обробляйте можливі винятки (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Управління ресурсами:**
    *   Якщо ви відкриваєте канали (`PIPE`), переконайтеся, що вони зрештою закриті. `Popen.communicate()` робить це автоматично. Якщо ви працюєте безпосередньо з `p.stdin`/`stdout`/`stderr`, вам може знадобитися закрити їх явно.
    *   У довготривалих програмах переконайтеся, що дочірні процеси завершуються правильно і не стають "зомбі". Використовуйте `p.wait()` або `p.communicate()`. За потреби використовуйте `p.terminate()` або `p.kill()`.

*   **Кодування:** Будьте обережні з кодуваннями при використанні `text=True` або при ручному декодуванні байтових рядків. Проблеми з кодуванням є поширеним джерелом помилок.

---

### 7. Практичні приклади

**1. Виконання простої команди та перевірка коду повернення:**
```python
import subprocess

try:
    # Виконати 'ls' для існуючого каталогу
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Команду 'ls /tmp' виконано, код повернення: {result.returncode}")

    # Виконати 'ls' для неіснуючого каталогу
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Цей рядок не буде виконано, якщо check=True, оскільки буде викликано виняток
except subprocess.CalledProcessError as e:
    print(f"Помилка виконання команди: {e.cmd}")
    print(f"Код повернення: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. Захоплення виводу команди:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Вказати поточний каталог як робочий каталог для git
    )
    print("Статус Git:")
    print(result.stdout)
except FileNotFoundError:
    print("Помилка: команду 'git' не знайдено. Чи встановлено Git і чи є він у PATH?")
except subprocess.CalledProcessError as e:
    print(f"Помилка Git: {e.stderr}")
```

**3. Надсилання даних на вхід процесу (використовуючи `communicate`):**
```python
import subprocess

# Надіслати текст до 'grep' для пошуку
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

    if process.returncode == 0: # grep знайшов збіги
        print("Знайдені рядки:")
        print(stdout_data)
    elif process.returncode == 1: # grep не знайшов збігів
        print("Збігів для 'python' не знайдено.")
    else: # інша помилка grep
        print(f"Помилка Grep (код {process.returncode}):")
        if stderr_data:
            print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep не відповів вчасно.")
    process.kill() # Вбити процес, якщо він завис
    process.communicate() # Зібрати решту виводу/помилок
```

**4. Створення конвеєра (`ls -l | wc -l`) без `shell=True`:**
(Більш детальний приклад був у розділі 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Переконайтеся, що stdout існує
    ls_proc.stdout.close()  # Дозволяє wc_proc отримати EOF, коли ls_proc завершиться

output, _ = wc_proc.communicate()
print(f"Кількість файлів/каталогів: {output.strip()}")
```

**5. Використання `timeout`:**
```python
import subprocess

try:
    # Команда, яка виконуватиметься 5 секунд
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Команда 'sleep 5' завершилася (не повинна була з timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Команда '{e.cmd}' не завершилася за {e.timeout} секунд.")
```

---

### 8. Висновок та корисні ресурси

Модуль `subprocess` є незамінним інструментом для будь-якого розробника Python, якому потрібно взаємодіяти із зовнішніми програмами або системним середовищем. Він пропонує баланс між простотою використання (через `subprocess.run()`) та потужною гнучкістю (через `subprocess.Popen()`).

**Ключові моменти:**
*   Віддавайте перевагу `subprocess.run()` для більшості завдань.
*   Використовуйте `subprocess.Popen()` для асинхронного виконання або складного керування потоками.
*   **Уникайте `shell=True`**, особливо з введенням користувача, через ризики безпеки. Передавайте команди як список аргументів.
*   Завжди обробляйте коди повернення та можливі винятки.
*   Будьте обережні з кодуваннями при роботі з текстовим виводом (`text=True` або ручне декодування).
*   `communicate()` — ваш друг для безпечного обміну даними через `PIPE`.

**Корисні ресурси:**
*   Офіційна документація Python для модуля `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - Новий модуль процесів: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)

```