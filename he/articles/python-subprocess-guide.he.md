## עבודה עם ספריית `subprocess` בפייתון


### 1. **מהו `subprocess` ולמה הוא נחוץ?**

מודול `subprocess` בפייתון מספק ממשק ליצירת תהליכים חדשים,
התחברות לזרמי הקלט/פלט/שגיאות שלהם, וקבלת קודי ההחזרה שלהם.
הוא מאפשר לסקריפטים של פייתון להריץ ולנהל תוכניות אחרות,
כתובות בכל שפה, בין אם הן כלי עזר מערכתיים, סקריפטים של מעטפת או קבצי הפעלה אחרים.

**הקשר היסטורי:**

לפני הופעת `subprocess`, שימשו פונקציות ממודול `os`, כגון `os.system()`, `os.spawn*()`, ומודול `commands` (בפייתון 2) להרצת תהליכים חיצוניים. לגישות אלו היו מספר חסרונות:
*   `os.system()`: מריץ פקודה דרך מעטפת המערכת, מה שאינו בטוח בעבודה עם קלט משתמש ופחות גמיש בניהול זרמים.
*   `os.spawn*()`: גמישים יותר, אך קשים לשימוש ותלויי פלטפורמה.
*   מודול `popen2` (ווריאציותיו): סיפק גישה לזרמים, אך היה מורכב וסבל מבעיות של קיפאון (deadlocks).

מודול `subprocess` הוצג בפייתון 2.4 (PEP 324) כדרך מאוחדת ובטוחה יותר לאינטראקציה עם תהליכי ילד. הוא מאגד את הפונקציונליות הטובה ביותר של המודולים הקודמים ומספק API נקי יותר.

**משימות עיקריות הנפתרות באמצעות `subprocess`:**

*   ביצוע פקודות מערכת הפעלה (לדוגמה, `ls`, `dir`, `ping`).
*   הרצת כלי עזר חיצוניים לעיבוד נתונים (לדוגמה, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   אינטגרציה עם מערכות בקרת גרסאות (`git`, `svn`).
*   הרצת מהדרים או מפרשים של שפות אחרות.
*   אוטומציה של ניהול מערכת.
*   ארגון אינטראקציה בין תוכניות שונות.

--- 

### 2. פונקציות ומחלקות עיקריות

מודול `subprocess` מציע מספר דרכים להרצת תהליכים:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   זוהי ה-API ברמה גבוהה **המומלצת**, שהוצגה בפייתון 3.5.
    *   מריצה פקודה, ממתינה לסיומה, ומחזירה אובייקט `CompletedProcess`.
    *   מתאימה לרוב המקרים שבהם אתה רק צריך להריץ פקודה ולקבל את התוצאה.

    ```python
    import subprocess

    # הרצה פשוטה
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # אם check=True והפקודה החזירה ערך שאינו אפס, תועלה חריגה מסוג CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   זוהי המחלקה הראשית ליצירה וניהול של תהליכי ילד.
    *   מספקת גמישות מירבית: ביצוע לא חוסם, שליטה מפורטת על זרמי קלט/פלט, היכולת לשלוח אותות לתהליך.
    *   הפונקציה `run()` משתמשת ב-`Popen` באופן פנימי.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"תהליך הופעל עם PID: {process.pid}")
    # ... ניתן לבצע עבודה אחרת ...
    process.wait() # המתן לסיום
    print(f"התהליך הסתיים עם קוד: {process.returncode}")
    ```

*   **פונקציות שהוצאו משימוש, אך עדיין נתקלות (היו ה-API הראשי לפני פייתון 3.5):**
    *   `subprocess.call(args, ...)`: מריצה פקודה וממתינה לסיומה. מחזירה את קוד ההחזרה. דומה ל-`os.system()`, אך בטוחה יותר אם `shell=False`.
    *   `subprocess.check_call(args, ...)`: כמו `call()`, אך מעלה `CalledProcessError` אם קוד ההחזרה אינו 0.
    *   `subprocess.check_output(args, ...)`: מריצה פקודה, ממתינה לסיומה, ומחזירה את הפלט הסטנדרטי שלה (stdout) כמחרוזת בתים. מעלה `CalledProcessError` אם קוד ההחזרה אינו 0.

    למרות שפונקציות אלו עדיין עובדות, `subprocess.run()` מספקת ממשק נוח ומאוחד יותר עבור אותן משימות.

--- 

### 3. ארגומנטים עיקריים של פונקציות `run()` ו-`Popen()`

ארגומנטים אלו מאפשרים לכוונן את ההפעלה והאינטראקציה עם תהליך הילד:

*   **`args`**: 
    *   הארגומנט הראשון והחובה.
    *   יכול להיות רשימת מחרוזות (מומלץ) או מחרוזת בודדת (אם `shell=True`).
    *   האיבר הראשון ברשימה הוא שם קובץ ההפעלה, השאר הם הארגומנטים שלו.
    *   דוגמה: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**: 
    *   מגדירים כיצד יטופלו זרמי הקלט, הפלט והשגיאות הסטנדרטיים של תהליך הילד.
    *   ערכים אפשריים:
        *   `None` (ברירת מחדל): יורש מתהליך האב.
        *   `subprocess.PIPE`: נוצר צינור (pipe) שדרכו ניתן להחליף נתונים. `process.stdin`, `process.stdout`, `process.stderr` הופכים לאובייקטים דמויי קובץ.
        *   `subprocess.DEVNULL`: מפנה את הזרם ל"שום מקום" (אנלוגי ל-`/dev/null`).
        *   תיאור קובץ פתוח (מספר שלם).
        *   אובייקט קובץ קיים (לדוגמה, קובץ פתוח `open('output.txt', 'w')`).

*   **`capture_output=True` (עבור `run()`):**
    *   אפשרות נוחה, שוות ערך להגדרת `stdout=subprocess.PIPE` ו-`stderr=subprocess.PIPE`.
    *   התוצאה תהיה זמינה ב-`result.stdout` וב-`result.stderr`.

*   **`text=True` (או `universal_newlines=True` לתאימות):**
    *   אם `True`, זרמי `stdout` ו-`stderr` (וכן `stdin`, אם מועברת מחרוזת) ייפתחו במצב טקסט באמצעות קידוד ברירת המחדל (בדרך כלל UTF-8). פענוח/קידוד מתרחש אוטומטית.
    *   אם `False` (ברירת מחדל), הזרמים מטופלים כבתים.
    *   מאז פייתון 3.7, `text` הוא הכינוי המועדף עבור `universal_newlines`. ניתן גם לציין קידוד ספציפי באמצעות `encoding` ומטפל שגיאות באמצעות `errors`. 

*   **`shell=False` (ברירת מחדל):**
    *   אם `False` (מומלץ מטעמי אבטחה וחיזוי), `args` חייב להיות רשימה. הפקודה מורצת ישירות.
    *   אם `True`, `args` מועבר כמחרוזת למעטפת המערכת (לדוגמה, `/bin/sh` ביוניקס, `cmd.exe` ב-Windows) לצורך פירוש. זה מאפשר להשתמש בתכונות מעטפת (משתנים, החלפות, צינורות), אך **מסוכן** אם `args` מכיל קלט משתמש לא מהימן (סיכון להזרקת פקודות).

*   **`cwd=None`:**
    *   מגדיר את ספריית העבודה הנוכחית עבור תהליך הילד. כברירת מחדל, הוא יורש מהאב.

*   **`env=None`:**
    *   מילון המגדיר את משתני הסביבה עבור התהליך החדש. כברירת מחדל, סביבת תהליך האב נורשת. אם צוין, הוא מחליף לחלוטין את הסביבה הנורשת. כדי להוסיף/לשנות משתנים תוך שמירה על השאר, עליך תחילה להעתיק את `os.environ` ולאחר מכן לשנות אותו.

*   **`timeout=None`:**
    *   הזמן המרבי בשניות המוקצה לביצוע הפקודה. אם התהליך לא מסתיים בתוך זמן זה, תועלה חריגה מסוג `subprocess.TimeoutExpired`. `Popen.communicate()` גם מקבל `timeout`.

*   **`check=False` (עבור `run()`):**
    *   אם `True` והתהליך יוצא עם קוד החזרה שאינו אפס, תועלה חריגה מסוג `subprocess.CalledProcessError`.

--- 

### 4. עבודה עם תוצאות ושגיאות

**אובייקט `CompletedProcess` (התוצאה של `run()`):**

```python
import subprocess

try:
    # ניסיון להריץ פקודה שעלולה להיכשל
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - שגיאת הקלדה כדי להדגים שגיאה
        capture_output=True,
        text=True,
        check=True, # תעלה חריגה אם returncode != 0
        timeout=10
    )
    print("הפקודה בוצעה בהצלחה.")
    print("קוד החזרה:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # בדרך כלל ריק בהצלחה

except subprocess.CalledProcessError as e:
    print(f"שגיאה בביצוע פקודה (CalledProcessError):")
    print(f"  פקודה: {e.cmd}")
    print(f"  קוד החזרה: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # עשוי להכיל פלט לפני השגיאה
    print(f"  Stderr: {e.stderr}") # בדרך כלל מכיל מידע על שגיאה
except subprocess.TimeoutExpired as e:
    print(f"הפקודה לא הסתיימה בתוך {e.timeout} שניות.")
    print(f"  פקודה: {e.cmd}")
    if e.stdout: print(f"  Stdout (חלקי): {e.stdout.decode(errors='ignore')}") # stdout הוא בתים
    if e.stderr: print(f"  Stderr (חלקי): {e.stderr.decode(errors='ignore')}") # stderr הוא בתים
except FileNotFoundError:
    print("שגיאה: פקודה או תוכנית לא נמצאו.")
except Exception as e:
    print(f"אירעה שגיאה אחרת: {e}")
```

**תכונות `CompletedProcess`:**
*   `args`: הארגומנטים ששימשו להפעלת התהליך.
*   `returncode`: קוד ההחזרה של התהליך. 0 בדרך כלל מציין הצלחה.
*   `stdout`: הפלט הסטנדרטי של התהליך (בתים או מחרוזת אם `text=True` ו-`capture_output=True`).
*   `stderr`: זרם השגיאות הסטנדרטי של התהליך (בתים או מחרוזת אם `text=True` ו-`capture_output=True`).

**חריגות:**
*   `subprocess.CalledProcessError`: מועלה אם `check=True` (עבור `run()`) או אם נעשה שימוש ב-`check_call()`, `check_output()` והפקודה יוצאת עם קוד שאינו אפס. מכיל `returncode`, `cmd`, `output` (או `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: אם פג הזמן הקצוב. מכיל `cmd`, `timeout`, `stdout`, `stderr` (פלט חלקי, אם קיים).
*   `FileNotFoundError`: אם קובץ ההפעלה לא נמצא.

**אינטראקציה עם אובייקט `Popen`:**

מחלקה `Popen` נותנת יותר שליטה:

```python
import subprocess
import time

# הרצת תהליך ברקע
process = subprocess.Popen(["sleep", "5"])
print(f"PID תהליך: {process.pid} הופעל.")

# בדיקת סטטוס לא חוסמת
while process.poll() is None: # poll() מחזיר None אם התהליך עדיין רץ
    print("התהליך עדיין רץ...")
    # ניתן לקרוא את הפלט כשהוא מגיע (זהירות, זה יכול לחסום!)
    # line = process.stdout.readline()
    # if line: print(f"פלט: {line.strip()}")
    time.sleep(1)

# המתן לסיום וקבל את כל הפלט/שגיאות
# stdout_data, stderr_data = process.communicate(timeout=10) # דרך בטוחה

# אם communicate() לא שימש, לאחר poll() != None ניתן לקרוא את השאר
if process.stdout:
    for line in process.stdout:
        print(f"פלט סופי: {line.strip()}")

print(f"התהליך הסתיים עם קוד: {process.returncode}")

# אם אתה צריך לכפות סיום
# process.terminate() # שולח SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # אם הוא לא הסתיים
#     process.kill()      # שולח SIGKILL
```

*   `process.poll()`: בודק אם תהליך הילד הסתיים. מחזיר את קוד ההחזרה או `None`. לא חוסם.
*   `process.wait(timeout=None)`: ממתין לסיום תהליך הילד. מחזיר את קוד ההחזרה. חוסם.
*   `process.communicate(input=None, timeout=None)`:
    *   הדרך הבטוחה ביותר לאינטראקציה עם תהליך בעת שימוש ב-`PIPE`.
    *   שולח נתונים ל-`stdin` (אם `input` צוין), קורא את כל הנתונים מ-`stdout` ו-`stderr` עד הסוף, וממתין לסיום התהליך.
    *   מחזיר טופל `(stdout_data, stderr_data)`.
    *   עוזר למנוע קיפאון (deadlocks) שיכול להתרחש עם קריאה/כתיבה ישירה ל-`process.stdout`/`process.stdin` אם המאגרים עולים על גדותיהם.
*   `process.terminate()`: שולח את האות `SIGTERM` לתהליך (סיום רך).
*   `process.kill()`: שולח את האות `SIGKILL` לתהליך (סיום קשה).
*   `process.send_signal(signal)`: שולח את האות שצוין לתהליך.
*   `process.stdin`, `process.stdout`, `process.stderr`: אובייקטים דמויי קובץ עבור צינורות, אם נוצרו עם `PIPE`.

--- 

### 5. תרחישי שימוש מתקדמים

**הפניית פלט של פקודה אחת לקלט של אחרת (צינורות):**

חיקוי `ps aux | grep python`:

```python
import subprocess

# הרצת הפקודה הראשונה, ה-stdout שלה יהיה PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# הרצת הפקודה השנייה, ה-stdin שלה יהיה ה-stdout של הפקודה הראשונה
# ה-stdout של הפקודה השנייה הוא גם PIPE כדי לקרוא את התוצאה
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # קישור stdout מ-ps ל-stdin עבור grep
    stdout=subprocess.PIPE,
    text=True
)

# חשוב! סגור את ה-stdout של הפקודה הראשונה בתהליך האב,
# כך ש-grep יקבל EOF כאשר ps יסיים.
if ps_process.stdout:
    ps_process.stdout.close()  

# קבל את הפלט מ-grep
stdout_data, stderr_data = grep_process.communicate()

print("תוצאת הצינור:")
print(stdout_data)

if stderr_data:
    print("שגיאות grep:", stderr_data)

# ודא ששני התהליכים הסתיימו
ps_process.wait() 
# grep_process.wait() # communicate() כבר המתין
print(f"קוד החזרה של ps: {ps_process.returncode}")
print(f"קוד החזרה של grep: {grep_process.returncode}")
```
*הערה:* עבור צינורות פשוטים, `subprocess.run("ps aux | grep python", shell=True, ...)` עשוי להיות פשוט יותר, אך פחות בטוח וגמיש.

**ביצוע תהליכים אסינכרוני:**

`Popen` הוא לא חוסם מטבעו. ניתן להריץ מספר תהליכים ולנהל אותם במקביל.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # פקודה עם שגיאה
]

processes = []
for cmd_args in commands:
    print(f"מריץ: {' '.join(cmd_args)}")
    # עבור אסינכרוניות, עדיף להפנות stdout/stderr,
    # כדי לא להפריע זה לזה או לקונסולת האב.
    # DEVNULL אם הפלט לא נחוץ, PIPE אם הוא נחוץ מאוחר יותר.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# בצע עבודה אחרת או המתן לסיום
while any(p.poll() is None for p in processes):
    print("ממתין לסיום כל התהליכים...")
    time.sleep(0.5)

print("\nתוצאות:")
for i, p in enumerate(processes):
    print(f"פקודה '{' '.join(commands[i])}' הסתיימה עם קוד: {p.returncode}")
```

**אינטראקציה אינטראקטיבית עם תהליך:**

זוהי משימה מורכבת הדורשת ניהול קפדני של זרמים כדי למנוע קיפאון. `communicate()` טוב להחלפה חד-פעמית. עבור סשן אינטראקטיבי ארוך, ייתכן שתצטרך לקרוא/לכתוב ישירות ל-`p.stdin`, `p.stdout`, `p.stderr` באמצעות קלט/פלט לא חוסם או תהליכים נפרדים.

```python
import subprocess

# דוגמה: הפעלת סשן פייתון אינטראקטיבי
process = subprocess.Popen(
    ['python', '-i'], # -i למצב אינטראקטיבי
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # חיץ שורה עבור stdout/stderr (לאינטראקטיביות)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # חשוב!

def read_output():
    # קריאת הפלט יכולה להיות מסובכת, מכיוון שצריך לדעת מתי לעצור.
    # זוהי דוגמה מאוד פשוטה. למשימות אמיתיות, נדרשים פתרונות חזקים יותר.
    # לדוגמה, קריאה עד לדפוס מסוים (הנחיה של שורת הפקודה).
    output = ""
    # קריאת stdout. ביישום אמיתי, זה צריך להיעשות באופן לא חוסם או בתהליך נפרד.
    # כאן אנו מניחים שאחרי הפקודה יהיה פלט כלשהו מיד.
    # זוהי הנחה מאוד שברירית למקרה הכללי!
    try:
        # ל-Popen אין readline עם timeout, זו אחת הקשיים
        # ניתן להשתמש ב-select על process.stdout.fileno()
        # או לקרוא תו אחר תו/שורה אחר שורה בתהליך נפרד
        # לשם הפשטות, זה לא כאן
        while True: # זהירות, זה יכול לחסום!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # גלאי הנחיה פרימיטיבי
                output += line
                break
            output += line
    except Exception as e:
        print(f"שגיאת קריאה: {e}")
    return output.strip()

# אתחול: קרא את ההנחיה הראשונית
initial_output = ""
# קריאת הודעת הפתיחה של פייתון
# זה מאוד פשוט, מכיוון שאיננו יודעים בדיוק כמה שורות לקרוא
for _ in range(5): # ננסה לקרוא כמה שורות
    try:
        # ל-Popen stdout אין timeout, צריך לקרוא בזהירות
        # stdout.readline() יכול לחסום.
        # ביישומים אמיתיים, select או threads נחוצים כאן.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # נמצאה ההנחיה
    except BlockingIOError:
        break # אם הייתה קריאה לא חוסמת
print(f"פלט ראשוני:\n{initial_output.strip()}")


send_command("a = 10")
# עבור אינטראקציה אינטראקטיבית, קריאת הפלט היא החלק הקשה ביותר.
# communicate() אינו מתאים, מכיוון שהוא סוגר את הזרמים.
# עליך לקרוא בזהירות מ-process.stdout ו-process.stderr, 
# אולי בתהליכים נפרדים, כדי לא לחסום את הראשי.
# דוגמה זו אינה מוכנה לייצור עבור אינטראקטיביות מורכבת.
# print(read_output()) # read_output זה מאוד פרימיטיבי

send_command("print(a * 2)")
# print(read_output())

# סיים את התהליך
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # המתן לסיום ואסוף את השאר

print("\nפלט סטנדרטי סופי:")
print(stdout_data)
if stderr_data:
    print("\nשגיאה סטנדרטית סופית:")
    print(stderr_data)

print(f"תהליך פייתון הסתיים עם קוד: {process.returncode}")

# עבור אינטראקציה אינטראקטיבית אמיתית, משתמשים לעיתים קרובות ב-pty (פסאודו-טרמינלים)
# באמצעות מודול `pty` במערכות דמויות יוניקס, או ספריות כמו `pexpect`.
```
*אזהרה*: אינטראקציה אינטראקטיבית ישירה עם `Popen` באמצעות `stdin`/`stdout`/`stderr` קשה בגלל קיפאון וחיץ. לאינטראקטיביות אמינה, משתמשים לעיתים קרובות בספריות כמו `pexpect` (עבור יוניקס) או דומות, שעובדות עם פסאודו-טרמינלים (pty).

**עבודה עם קידודים:**
*   השתמש ב-`text=True` (או `universal_newlines=True`) עבור פענוח/קידוד אוטומטי.
*   במידת הצורך, ניתן לציין `encoding="הקידוד שלך"` ו-`errors="מטפל-שגיאות"` (לדוגמה, `replace`, `ignore`).
*   אם `text=False` (ברירת מחדל), `stdout` ו-`stderr` יהיו מחרוזות בתים. תצטרך לפענח אותם ידנית: `result.stdout.decode('utf-8', errors='replace')`.

--- 

### 6. אבטחה ושיטות עבודה מומלצות

*   **סיכונים של `shell=True` והזרקת פקודות:**
    *   **לעולם אל** תשתמש ב-`shell=True` עם פקודות הבנויות מקלט משתמש לא מהימן. זה פותח את הדרך להזרקת פקודות.
    *   דוגמה לפגיעות:
        ```python
        # מסוכן!
        filename = input("הכנס שם קובץ למחיקה: ") # המשתמש מכניס "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   אם `shell=True` נחוץ לחלוטין (לדוגמה, כדי להשתמש בצינורות `|` או בתווים כלליים `*` ישירות בשורת הפקודה), יש לברוח בזהירות את כל חלקי הפקודה שנוצרו מבחוץ באמצעות `shlex.quote()` (מאז פייתון 3.3).

*   **אימות ובריחה של קלט משתמש:**
    *   גם אם `shell=False`, אם ארגומנטים של פקודה נוצרים מקלט משתמש, יש לאמת אותם. לדוגמה, אם צפוי שם קובץ, ודא שהוא שם קובץ חוקי ולא משהו כמו `../../../etc/passwd`.

*   **העברת ארגומנטים כרשימה (כאשר `shell=False`):**
    *   זוהי הדרך הבטוחה ביותר. כל ארגומנט מועבר כאיבר נפרד ברשימה, ומערכת ההפעלה מטפלת בהם נכון, מבלי לנסות לפרש אותם כחלק מפקודת מעטפת.
    *   דוגמה: `subprocess.run(["rm", filename_from_user])` — כאן `filename_from_user` תמיד יטופל כארגומנט בודד (שם קובץ), גם אם הוא מכיל רווחים או תווים מיוחדים.

*   **טיפול בשגיאות וקודי החזרה:**
    *   תמיד בדוק את `returncode` או השתמש ב-`check=True` (עבור `run()`) / `check_call()` / `check_output()` כדי לוודא שהפקודה בוצעה בהצלחה.
    *   טפל בחריגות אפשריות (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **ניהול משאבים:**
    *   אם אתה פותח צינורות (`PIPE`), ודא שהם נסגרים בסופו של דבר. `Popen.communicate()` עושה זאת אוטומטית. אם אתה עובד ישירות עם `p.stdin`/`stdout`/`stderr`, ייתכן שתצטרך לסגור אותם במפורש.
    *   ביישומים ארוכי טווח, ודא שתהליכי ילד מסתיימים נכון ולא הופכים ל"זומבים". השתמש ב-`p.wait()` או ב-`p.communicate()`. במידת הצורך, השתמש ב-`p.terminate()` או ב-`p.kill()`.

*   **קידודים:** היזהר עם קידודים בעת שימוש ב-`text=True` או בעת פענוח ידני של מחרוזות בתים. בעיות קידוד הן מקור נפוץ לשגיאות.

--- 

### 7. דוגמאות מעשיות

**1. ביצוע פקודה פשוטה ובדיקת קוד החזרה:**
```python
import subprocess

try:
    # הרצת 'ls' עבור ספרייה קיימת
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"פקודה 'ls /tmp' בוצעה, קוד החזרה: {result.returncode}")

    # הרצת 'ls' עבור ספרייה לא קיימת
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # שורה זו לא תבוצע אם check=True, מכיוון שתועלה חריגה
except subprocess.CalledProcessError as e:
    print(f"שגיאה בביצוע פקודה: {e.cmd}")
    print(f"קוד החזרה: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. לכידת פלט של פקודה:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # ציין את הספרייה הנוכחית כספריית העבודה עבור git
    )
    print("סטטוס Git:")
    print(result.stdout)
except FileNotFoundError:
    print("שגיאה: פקודת 'git' לא נמצאה. האם Git מותקן וב-PATH?")
except subprocess.CalledProcessError as e:
    print(f"שגיאת Git: {e.stderr}")
```

**3. שליחת נתונים לקלט של תהליך (באמצעות `communicate`):**
```python
import subprocess

# שלח טקסט ל-'grep' לחיפוש
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

    if process.returncode == 0: # grep מצא התאמות
        print("שורות שנמצאו:")
        print(stdout_data)
    elif process.returncode == 1: # grep לא מצא התאמות
        print("לא נמצאו התאמות עבור 'python'.")
    else: # שגיאת grep אחרת
        print(f"שגיאת Grep (קוד {process.returncode}):")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep לא הגיב בזמן.")
    process.kill() # הרוג את התהליך אם הוא נתקע
    process.communicate() # אסוף את הפלט/שגיאות הנותרים
```

**4. יצירת צינור (`ls -l | wc -l`) ללא `shell=True`:**
(דוגמה מפורטת יותר הייתה בסעיף 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # ודא ש-stdout קיים
    ls_proc.stdout.close()  # מאפשר ל-wc_proc לקבל EOF כאשר ls_proc מסיים

output, _ = wc_proc.communicate()
print(f"מספר קבצים/ספריות: {output.strip()}")
```

**5. שימוש ב-`timeout`:**
```python
import subprocess

try:
    # פקודה שתרוץ 5 שניות
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("פקודה 'sleep 5' הסתיימה (לא אמורה הייתה עם timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"פקודה '{e.cmd}' לא הסתיימה בתוך {e.timeout} שניות.")
```

--- 

### 8. מסקנה ומשאבים שימושיים

מודול `subprocess` הוא כלי חיוני לכל מפתח פייתון שצריך ליצור אינטראקציה עם תוכניות חיצוניות או עם סביבת המערכת. הוא מציע איזון בין קלות שימוש (באמצעות `subprocess.run()`) וגמישות עוצמתית (באמצעות `subprocess.Popen()`).

**נקודות מפתח:**
*   העדף `subprocess.run()` עבור רוב המשימות.
*   השתמש ב-`subprocess.Popen()` עבור ביצוע אסינכרוני או ניהול זרמים מורכב.
*   **הימנע מ-`shell=True`**, במיוחד עם קלט משתמש, עקב סיכוני אבטחה. העבר פקודות כרשימת ארגומנטים.
*   תמיד טפל בקודי החזרה ובחריגות אפשריות.
*   היזהר עם קידודים בעת עבודה עם פלט טקסט (`text=True` או פענוח ידני).
*   `communicate()` הוא חברך להחלפת נתונים בטוחה באמצעות `PIPE`.

**משאבים שימושיים:**
*   תיעוד רשמי של פייתון עבור מודול `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - מודול תהליכים חדש: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)

