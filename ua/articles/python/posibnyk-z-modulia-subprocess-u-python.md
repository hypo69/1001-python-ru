## Робота з бібліотекою `subprocess` у Python


### 1. **Що таке `subprocess` і навіщо він потрібен?**

Модуль `subprocess` у Python надає інтерфейс для створення нових процесів,
підключення до їхніх потоків введення/виведення/помилок та отримання їхніх кодів повернення.
Він дозволяє Python-скриптам запускати та керувати іншими програмами,
написаними будь-якою мовою, будь то системні утиліти, скрипти оболонки чи інші виконувані файли.

**Історичний контекст:**

До появи `subprocess` для запуску зовнішніх процесів використовувалися функції з модуля `os`, такі як `os.system()`, `os.spawn*()`, а також модуль `commands` (у Python 2). Ці підходи мали низку недоліків:
*   `os.system()`: Запускає команду через системну оболонку, що є небезпечним при роботі з введенням користувача та менш гнучким у керуванні потоками.
*   `os.spawn*()`: Більш гнучкі, але складні у використанні та залежні від платформи.
*   Модуль `popen2` (та його варіації): Надавав доступ до потоків, але був складним і мав проблеми з блокуваннями.

Модуль `subprocess` був представлений у Python 2.4 (PEP 324) як уніфікований та безпечніший спосіб взаємодії з дочірніми процесами. Він інкапсулює найкращу функціональність попередніх модулів та надає чистіший API.

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
    *   Це **рекомендований** високорівневий API, що з'явився в Python 3.5.
    *   Запускає команду, очікує її завершення та повертає об'єкт `CompletedProcess`.
    *   Підходить для більшості випадків, коли потрібно просто виконати команду та отримати результат.

    ```python
    import subprocess

    # Простий запуск
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Якщо check=True і команда повернула не 0, буде викинуто CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Це основний клас для створення та керування дочірніми процесами.
    *   Надає максимальну гнучкість: неблокуючий запуск, детальний контроль потоків введення/виведення, можливість надсилати сигнали процесу.
    *   Функція `run()` всередині себе використовує `Popen`.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Процес запущено з PID: {process.pid}")
    # ... можна робити іншу роботу ...
    process.wait() # Очікувати завершення
    print(f"Процес завершився з кодом: {process.returncode}")
    ```

*   **Застарілі, але зустрічаються функції (до Python 3.5 були основним API):**
    *   `subprocess.call(args, ...)`: Виконує команду та чекає її завершення. Повертає код повернення. Схоже на `os.system()`, але безпечніше, якщо `shell=False`.
    *   `subprocess.check_call(args, ...)`: Як `call()`, але викидає `CalledProcessError`, якщо код повернення не 0.
    *   `subprocess.check_output(args, ...)`: Виконує команду, чекає завершення та повертає її стандартний вивід (stdout) у вигляді байтового рядка. Викидає `CalledProcessError`, якщо код повернення не 0.

    Хоча ці функції все ще працюють, `subprocess.run()` надає більш зручний та уніфікований інтерфейс для тих самих завдань.

---

### 3. Ключові аргументи функцій `run()` та `Popen()`

Ці аргументи дозволяють тонко налаштувати запуск та взаємодію з дочірнім процесом:

*   **`args`**: 
    *   Перший і обов'язковий аргумент.
    *   Може бути списком рядків (рекомендується) або одним рядком (якщо `shell=True`).
    *   Перший елемент списку – це ім'я виконуваного файлу, решта – його аргументи.
    *   Приклад: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**: 
    *   Визначають, як будуть оброблятися стандартний ввід, вивід та потік помилок дочірнього процесу.
    *   Можливі значення:
        *   `None` (за замовчуванням): Успадковуються від батьківського процесу.
        *   `subprocess.PIPE`: Створюється канал (pipe), через який можна обмінюватися даними. `process.stdin`, `process.stdout`, `process.stderr` стають файлоподібними об'єктами.
        *   `subprocess.DEVNULL`: Перенаправляє потік у "нікуди" (аналог `/dev/null`).
        *   Відкритий файловий дескриптор (ціле число).
        *   Існуючий файловий об'єкт (наприклад, відкритий файл `open('output.txt', 'w')`).

*   **`capture_output=True` (для `run()`):**
    *   Зручна опція, еквівалентна встановленню `stdout=subprocess.PIPE` та `stderr=subprocess.PIPE`.
    *   Результат буде доступний у `result.stdout` та `result.stderr`.

*   **`text=True` (або `universal_newlines=True` для сумісності):**
    *   Якщо `True`, потоки `stdout` та `stderr` (а також `stdin`, якщо передається рядок) будуть відкриті в текстовому режимі з використанням кодування за замовчуванням (зазвичай UTF-8). Декодування/кодування відбувається автоматично.
    *   Якщо `False` (за замовчуванням), потоки обробляються як байтові.
    *   Починаючи з Python 3.7, `text` є кращим псевдонімом для `universal_newlines`. Можна також вказати конкретне кодування через `encoding` та обробник помилок через `errors`.

*   **`shell=False` (за замовчуванням):**
    *   Якщо `False` (рекомендується з міркувань безпеки та передбачуваності), `args` повинен бути списком. Команда запускається безпосередньо.
    *   Якщо `True`, `args` передається як рядок системній оболонці (наприклад, `/bin/sh` в Unix, `cmd.exe` в Windows) для інтерпретації. Це дозволяє використовувати можливості оболонки (змінні, підстановки, конвеєри), але **НЕБЕЗПЕЧНО**, якщо `args` містить неперевірене введення користувача (ризик ін'єкції команд).

*   **`cwd=None`:**
    *   Задає поточний робочий каталог для дочірнього процесу. За замовчуванням успадковується від батьківського.

*   **`env=None`:**
    *   Словник, що визначає змінні середовища для нового процесу. За замовчуванням успадковується середовище батьківського процесу. Якщо вказано, він повністю замінює успадковане середовище. Щоб додати/змінити змінні, зберігаючи решту, потрібно спочатку скопіювати `os.environ` і потім модифікувати його.

*   **`timeout=None`:**
    *   Максимальний час у секундах, відведений на виконання команди. Якщо процес не завершиться за цей час, буде викинуто виняток `subprocess.TimeoutExpired`. `Popen.communicate()` також приймає `timeout`.

*   **`check=False` (для `run()`):**
    *   Якщо `True` і процес завершується з ненульовим кодом повернення, буде викинуто виняток `subprocess.CalledProcessError`.

---

### 4. Робота з результатами та помилками

**Об'єкт `CompletedProcess` (результат `run()`):**

```python
import subprocess

try:
    # Намагаємося виконати команду, яка може завершитися з помилкою
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - друкарська помилка для демонстрації помилки
        capture_output=True,
        text=True,
        check=True, # Викличе виняток, якщо returncode != 0
        timeout=10
    )
    print("Команда виконана успішно.")
    print("Код повернення:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Зазвичай порожній при успіху

except subprocess.CalledProcessError as e:
    print(f"Помилка виконання команди (CalledProcessError):")
    print(f"  Команда: {e.cmd}")
    print(f"  Код повернення: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # Може містити вивід до помилки
    print(f"  Stderr: {e.stderr}") # Зазвичай тут інформація про помилку
except subprocess.TimeoutExpired as e:
    print(f"Команда не завершилася за {e.timeout} секунд.")
    print(f"  Команда: {e.cmd}")
    if e.stdout: print(f"  Stdout (частковий): {e.stdout.decode(errors='ignore')}") # stdout байтовий
    if e.stderr: print(f"  Stderr (частковий): {e.stderr.decode(errors='ignore')}") # stderr байтовий
except FileNotFoundError:
    print("Помилка: команда або програма не знайдена.")
except Exception as e:
    print(f"Сталася інша помилка: {e}")
```

**Атрибути `CompletedProcess`:**
*   `args`: Аргументи, використані для запуску процесу.
*   `returncode`: Код повернення процесу. 0 зазвичай означає успіх.
*   `stdout`: Стандартний вивід процесу (байти або рядок, якщо `text=True` та `capture_output=True`).
*   `stderr`: Стандартний потік помилок процесу (байти або рядок, якщо `text=True` та `capture_output=True`).

**Винятки:**
*   `subprocess.CalledProcessError`: Викидається, якщо `check=True` (для `run()`) або використовуються `check_call()`, `check_output()` і команда завершилася з ненульовим кодом. Містить `returncode`, `cmd`, `output` (або `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: Якщо закінчився таймаут. Містить `cmd`, `timeout`, `stdout`, `stderr` (частковий вивід, якщо був).
*   `FileNotFoundError`: Якщо виконуваний файл не знайдено.

**Взаємодія з об'єктом `Popen`:**

Клас `Popen` дає більше контролю:

```python
import subprocess
import time

# Запускаємо процес у фоновому режимі
process = subprocess.Popen(["ping", "-c", "5", "google.com"], stdout=subprocess.PIPE, text=True)

print(f"Процес PID: {process.pid} запущено.")

# Неблокуюча перевірка статусу
while process.poll() is None: # poll() повертає None, якщо процес ще працює
    print("Процес ще працює...")
    # Можна читати вивід по мірі надходження (обережно, може блокувати!)
    # line = process.stdout.readline()
    # if line: print(f"Вивід: {line.strip()}")
    time.sleep(1)

# Очікування завершення та отримання всього виводу/помилок
# stdout_data, stderr_data = process.communicate(timeout=10) # Безпечний спосіб

# Якщо communicate() не використовувався, після poll() != None можна прочитати залишки
if process.stdout:
    for line in process.stdout:
        print(f"Фінальний вивід: {line.strip()}")

print(f"Процес завершився з кодом: {process.returncode}")

# Якщо потрібно примусово завершити
# process.terminate() # Надсилає SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Якщо не завершився
#     process.kill()      # Надсилає SIGKILL
```

*   `process.poll()`: Перевіряє, чи завершився дочірній процес. Повертає код повернення або `None`. Неблокуючий.
*   `process.wait(timeout=None)`: Очікує завершення дочірнього процесу. Повертає код повернення. Блокуючий.
*   `process.communicate(input=None, timeout=None)`:
    *   Найбезпечніший спосіб взаємодії з процесом, коли використовуються `PIPE`.
    *   Надсилає дані в `stdin` (якщо `input` вказано), читає всі дані з `stdout` та `stderr` до кінця та чекає завершення процесу.
    *   Повертає кортеж `(stdout_data, stderr_data)`.
    *   Допомагає уникнути дедлоків, які можуть виникнути при прямому читанні/запису в `process.stdout`/`process.stdin`, якщо буфери переповнюються.
*   `process.terminate()`: Надсилає сигнал `SIGTERM` процесу (м'яке завершення).
*   `process.kill()`: Надсилає сигнал `SIGKILL` процесу (жорстке завершення).
*   `process.send_signal(signal)`: Надсилає вказаний сигнал процесу.
*   `process.stdin`, `process.stdout`, `process.stderr`: Файлоподібні об'єкти для каналів, якщо вони були створені з `PIPE`.

---

### 5. Просунуті сценарії використання

**Перенаправлення виводу однієї команди на ввід іншої (пайплайни/конвеєри):**

Емулюємо `ps aux | grep python`:

```python
import subprocess

# Запускаємо першу команду, її stdout буде PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Запускаємо другу команду, її stdin буде stdout першої команди
# stdout другої команди теж PIPE, щоб прочитати результат
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Зв'язуємо stdout від ps з stdin для grep
    stdout=subprocess.PIPE,
    text=True
)

# Важливо! Закрити stdout першої команди в батьківському процесі,
# щоб grep отримав EOF, коли ps завершиться.
if ps_process.stdout:
    ps_process.stdout.close()

# Отримуємо вивід від grep
stdout_data, stderr_data = grep_process.communicate()

print("Результат конвеєра:")
print(stdout_data)

if stderr_data:
    print("Помилки grep:", stderr_data)

# Переконаємося, що обидва процеси завершилися
ps_process.wait() # communicate() вже дочекався
# grep_process.wait() # communicate() вже дочекався
print(f"ps return code: {ps_process.returncode}")
print(f"grep return code: {grep_process.returncode}")
```
*Примітка:* Для простих конвеєрів `subprocess.run("ps aux | grep python", shell=True, ...)` може бути простіше, але менш безпечно та гнучко.

**Асинхронний запуск процесів:**

`Popen` за своєю природою неблокуючий. Ви можете запустити кілька процесів і керувати ними паралельно.

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
    print(f"Запускаємо: {' '.join(cmd_args)}")
    # Для асинхронності stdout/stderr краще перенаправити,
    # щоб не заважати один одному або консолі батьківського процесу.
    # DEVNULL якщо вивід не потрібен, PIPE якщо потрібен пізніше.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Робимо іншу роботу або чекаємо завершення
while any(p.poll() is None for p in processes):
    print("Очікування завершення всіх процесів...")
    time.sleep(0.5)

print("\nРезультати:")
for i, p in enumerate(processes):
    print(f"Команда '{' '.join(commands[i])}' завершилася з кодом: {p.returncode}")
```

**Інтерактивна взаємодія з процесом:**

Це складне завдання, що вимагає обережного керування потоками, щоб уникнути блокувань. `communicate()` добре підходить для одноразового обміну. Для тривалого інтерактивного сеансу може знадобитися пряме читання/запис у `p.stdin`, `p.stdout`, `p.stderr` з використанням неблокуючого вводу/виводу або окремих потоків.

```python
import subprocess

# Приклад: запуск інтерактивної python сесії
process = subprocess.Popen(
    ['python', '-i'], # -i для інтерактивного режиму
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Лінійна буферизація для stdout/stderr (для інтерактивності)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Важливо!

def read_output():
    # Читання виводу може бути складним, оскільки потрібно знати, коли зупинитися.
    # Тут дуже спрощений приклад. Для реальних завдань потрібні більш надійні рішення.
    # Наприклад, читати до певного патерну (запрошення командного рядка).
    output = ""
    # Читаємо stdout. У реальному додатку це потрібно робити неблокуючим способом або в окремому потоці.
    # Тут ми припускаємо, що після команди одразу буде якийсь вивід.
    # Це дуже крихке припущення для загального випадку!
    try:
        # У Popen немає readline з таймаутом, це одна зі складностей
        # Можна використовувати select на process.stdout.fileno() 
        # або читати посимвольно/построково в окремому потоці
        # Для простоти тут цього немає
        while True: # Обережно, може заблокуватися!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Примітивний детектор запрошення
                output += line
                break
            output += line
    except Exception as e:
        print(f"Помилка читання: {e}")
    return output.strip()

# Ініціалізація: прочитати початкове запрошення
initial_output = ""
# Читання привітання Python
# Це дуже спрощено, оскільки ми не знаємо точно, скільки рядків читати
for _ in range(5): # Спробуємо прочитати кілька рядків
    try:
        # У Popen stdout немає timeout, потрібно читати обережно
        # stdout.readline() може заблокуватися.
        # У реальних додатках тут потрібен select або потоки.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Знайшли запрошення
    except BlockingIOError:
        break # Якщо б було неблокуюче читання
print(f"Початковий вивід:\n{initial_output.strip()}")


send_command("a = 10")
# Для інтерактивної взаємодії читання виводу - найскладніша частина.
# communicate() не підходить, оскільки він закриває потоки.
# Потрібно акуратно читати з process.stdout та process.stderr, 
# можливо, в окремих потоках, щоб не блокувати основний.
# Цей приклад НЕ є production-ready для складного інтерактиву.
# print(read_output()) # Цей read_output дуже примітивний

send_command("print(a * 2)")
# print(read_output())

# Завершуємо процес
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Дочекатися завершення та зібрати залишки

print("\nКінцевий stdout:")
print(stdout_data)
if stderr_data:
    print("\nКінцевий stderr:")
    print(stderr_data)

print(f"Python process finished with code: {process.returncode}")

# Для справжньої інтерактивної взаємодії часто використовують pty (псевдотермінали)
# через модуль `pty` в Unix-подібних системах, або бібліотеки типу `pexpect`.
```
*Попередження*: Пряма інтерактивна взаємодія з `Popen` через `stdin`/`stdout`/`stderr` є складною через блокування та буферизацію. Для надійного інтерактиву часто використовують бібліотеки на кшталт `pexpect` (для Unix) або аналоги, які працюють з псевдотерміналами (pty).

**Робота з кодуваннями:**
*   Використовуйте `text=True` (або `universal_newlines=True`) для автоматичного декодування/кодування.
*   За необхідності можна вказати `encoding="ваше-кодування"` та `errors="обробник-помилок"` (наприклад, `replace`, `ignore`).
*   Якщо `text=False` (за замовчуванням), `stdout` та `stderr` будуть байтовими рядками. Їх потрібно буде декодувати вручну: `result.stdout.decode('utf-8', errors='replace')`.

---

### 6. Безпека та найкращі практики

*   **Ризики `shell=True` та ін'єкції команд:**
    *   **Ніколи** не використовуйте `shell=True` з командами, побудованими з неперевіреного введення користувача. Це відкриває шлях до ін'єкції команд.
    *   Приклад вразливості:
        ```python
        # НЕБЕЗПЕЧНО!
        filename = input("Введіть ім'я файлу для видалення: ") # Користувач вводить "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Якщо `shell=True` абсолютно необхідний (наприклад, для використання пайпів `|` або підстановок `*` прямо в рядку команди), ретельно екрануйте всі частини команди, що формуються ззовні, за допомогою `shlex.quote()` (починаючи з Python 3.3).

*   **Валідація та екранування введення користувача:**
    *   Навіть якщо `shell=False`, якщо аргументи команди формуються з введення користувача, їх слід валідувати. Наприклад, якщо очікується ім'я файлу, переконайтеся, що це дійсно допустиме ім'я файлу, а не щось на кшталт `../../../etc/passwd`.

*   **Передача аргументів списком (коли `shell=False`):**
    *   Це найбезпечніший спосіб. Кожен аргумент передається як окремий елемент списку, і операційна система обробляє їх коректно, не намагаючись інтерпретувати як частину команди оболонки.
    *   Приклад: `subprocess.run(["rm", filename_from_user])` — тут `filename_from_user` буде завжди трактуватися як один аргумент (ім'я файлу), навіть якщо містить пробіли або спецсимволи.

*   **Обробка помилок та кодів повернення:**
    *   Завжди перевіряйте `returncode` або використовуйте `check=True` (для `run()`) / `check_call()` / `check_output()`, щоб переконатися, що команда виконана успішно.
    *   Обробляйте можливі винятки (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Керування ресурсами:**
    *   Якщо ви відкриваєте канали (`PIPE`), переконайтеся, що вони в кінцевому підсумку закриваються. `Popen.communicate()` робить це автоматично. Якщо ви працюєте з `p.stdin/stdout/stderr` безпосередньо, може знадобитися їх явне закриття.
    *   У довготривалих додатках переконайтеся, що дочірні процеси коректно завершуються і не стають "зомбі". Використовуйте `p.wait()` або `p.communicate()`. За необхідності використовуйте `p.terminate()` або `p.kill()`.

*   **Кодування:** Будьте уважні до кодувань при використанні `text=True` або при ручному декодуванні байтових рядків. Проблеми з кодуваннями – часте джерело помилок.

---

### 7. Практичні приклади

**1. Виконання простої команди та перевірка коду повернення:**
```python
import subprocess

try:
    # Запускаємо 'ls' для існуючого каталогу
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Команда 'ls /tmp' виконана, код повернення: {result.returncode}")

    # Запускаємо 'ls' для неіснуючого каталогу
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Цей рядок не виконається, якщо check=True, оскільки буде виняток
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
        cwd="."  # Вкажемо поточний каталог як робочий для git
    )
    print("Статус Git:")
    print(result.stdout)
except FileNotFoundError:
    print("Помилка: команда 'git' не знайдена. Чи встановлений Git і чи є він у PATH?")
except subprocess.CalledProcessError as e:
    print(f"Помилка git: {e.stderr}")
```

**3. Надсилання даних на ввід процесу (використовуючи `communicate`):**
```python
import subprocess

# Надсилаємо текст у 'grep' для пошуку
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
        print("Збігів 'python' не знайдено.")
    else: # інша помилка grep
        print(f"Помилка grep (код {process.returncode}):")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep не відповів вчасно.")
    process.kill() # Вбити процес, якщо він завис
    process.communicate() # Зібрати залишковий вивід/помилки
```

**4. Створення конвеєра (`ls -l | wc -l`) без `shell=True`:**
(Більш детальний приклад був у розділі 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Переконаємося, що stdout існує
    ls_proc.stdout.close()  # Дозволяє wc_proc отримати EOF, коли ls_proc закінчить

output, _ = wc_proc.communicate()
print(f"Кількість файлів/каталогів: {output.strip()}")
```

**5. Використання `timeout`:**
```python
import subprocess

try:
    # Команда, яка буде виконуватися 5 секунд
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Команда 'sleep 5' завершилася (не повинна була при timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Команда '{e.cmd}' не завершилася за {e.timeout} секунд.")
```

---

### 8. Висновок та корисні ресурси

Модуль `subprocess` є незамінним інструментом для будь-якого Python-розробника, якому необхідно взаємодіяти із зовнішніми програмами або системним середовищем. Він пропонує баланс між простотою використання (через `subprocess.run()`) та потужною гнучкістю (через `subprocess.Popen()`).

**Ключові моменти:**
*   Віддавайте перевагу `subprocess.run()` для більшості завдань.
*   Використовуйте `subprocess.Popen()` для асинхронного виконання або складного керування потоками.
*   **Уникайте `shell=True`**, особливо з введенням користувача, через ризики безпеки. Передавайте команди списком аргументів.
*   Завжди обробляйте коди повернення та можливі винятки.
*   Будьте уважні до кодувань при роботі з текстовим виводом (`text=True` або ручне декодування).
*   `communicate()` — ваш друг для безпечного обміну даними через `PIPE`.

**Корисні ресурси:**
*   Офіційна документація Python щодо модуля `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - A New Process Module: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)
