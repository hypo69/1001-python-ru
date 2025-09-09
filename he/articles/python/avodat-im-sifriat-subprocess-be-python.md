## עבודה עם ספריית `subprocess` בפייתון


### 1. **מהו `subprocess` ולמה הוא נחוץ?**

מודול `subprocess` בפייתון מספק ממשק ליצירת תהליכים חדשים,
חיבור לזרמי הקלט/פלט/שגיאות שלהם וקבלת קודי ההחזרה שלהם.
הוא מאפשר לסקריפטים של פייתון להפעיל ולנהל תוכניות אחרות,
כתובות בכל שפה, בין אם אלה כלי עזר מערכתיים, סקריפטים של מעטפת או קבצי הפעלה אחרים.

**הקשר היסטורי:**

לפני `subprocess`, להפעלת תהליכים חיצוניים שימשו פונקציות מהמודול `os`, כגון `os.system()`, `os.spawn*()`, וכן המודול `commands` (בפייתון 2). לגישות אלה היו מספר חסרונות:
*   `os.system()`: מפעיל פקודה דרך מעטפת המערכת, מה שאינו בטוח בעבודה עם קלט משתמש ופחות גמיש בניהול זרמים.
*   `os.spawn*()`: גמישים יותר, אך מסובכים לשימוש ותלויי פלטפורמה.
*   מודול `popen2` (ווריאציותיו): סיפק גישה לזרמים, אך היה מסובך וסבל מבעיות חסימה.

מודול `subprocess` הוצג בפייתון 2.4 (PEP 324) כדרך מאוחדת ובטוחה יותר לאינטראקציה עם תהליכי ילד. הוא מאגד את הפונקציונליות הטובה ביותר של המודולים הקודמים ומספק API נקי יותר.

**משימות עיקריות הנפתרות באמצעות `subprocess`:**

*   ביצוע פקודות מערכת הפעלה (לדוגמה, `ls`, `dir`, `ping`).
*   הפעלת כלי עזר חיצוניים לעיבוד נתונים (לדוגמה, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   שילוב עם מערכות בקרת גרסאות (`git`, `svn`).
*   הפעלת מהדרים או מפרשים של שפות אחרות.
*   אוטומציה של ניהול מערכת.
*   ארגון אינטראקציה בין תוכניות שונות.

---


### 2. פונקציות ומחלקות עיקריות

מודול `subprocess` מציע מספר דרכים להפעלת תהליכים:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   זהו ה-API הגבוה-רמה **המומלץ**, שהופיע בפייתון 3.5.
    *   מפעיל פקודה, ממתין לסיומה ומחזיר אובייקט `CompletedProcess`.
    *   מתאים לרוב המקרים שבהם צריך פשוט לבצע פקודה ולקבל תוצאה.

    ```python
    import subprocess

    # הפעלה פשוטה
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # אם check=True והפקודה החזירה ערך שאינו 0, תיזרק CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   זוהי המחלקה העיקרית ליצירה וניהול של תהליכי ילד.
    *   מספקת גמישות מירבית: הפעלה לא חוסמת, שליטה מפורטת בזרמי קלט/פלט, יכולת לשלוח אותות לתהליך.
    *   הפונקציה `run()` משתמשת ב-`Popen` באופן פנימי.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"תהליך הופעל עם PID: {process.pid}")
    # ... ניתן לבצע עבודה אחרת ...
    process.wait() # המתן לסיום
    print(f"תהליך הסתיים עם קוד: {process.returncode}")
    ```

*   **פונקציות מיושנות, אך עדיין קיימות (לפני פייתון 3.5 היו ה-API העיקרי):**
    *   `subprocess.call(args, ...)`: מבצע פקודה וממתין לסיומה. מחזיר את קוד ההחזרה. דומה ל-`os.system()`, אך בטוח יותר אם `shell=False`.
    *   `subprocess.check_call(args, ...)`: כמו `call()`, אך זורק `CalledProcessError` אם קוד ההחזרה אינו 0.
    *   `subprocess.check_output(args, ...)`: מבצע פקודה, ממתין לסיומה ומחזיר את הפלט הסטנדרטי שלה (stdout) כמחרוזת בתים. זורק `CalledProcessError` אם קוד ההחזרה אינו 0.

    למרות שפונקציות אלה עדיין עובדות, `subprocess.run()` מספק ממשק נוח ומאוחד יותר לאותן משימות.

---


### 3. ארגומנטים מרכזיים של פונקציות `run()` ו-`Popen()`

ארגומנטים אלה מאפשרים כוונון עדין של הפעלת התהליך ואינטראקציה עם תהליך הילד:

*   **`args`**: 
    *   הארגומנט הראשון והחובה.
    *   יכול להיות רשימת מחרוזות (מומלץ) או מחרוזת בודדת (אם `shell=True`).
    *   האלמנט הראשון ברשימה הוא שם קובץ ההפעלה, השאר הם הארגומנטים שלו.
    *   דוגמה: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**: 
    *   קובעים כיצד יטופלו זרמי הקלט, הפלט וזרם השגיאות הסטנדרטיים של תהליך הילד.
    *   ערכים אפשריים:
        *   `None` (ברירת מחדל): יורשים מתהליך האב.
        *   `subprocess.PIPE`: נוצר צינור (pipe), שדרכו ניתן להחליף נתונים. `process.stdin`, `process.stdout`, `process.stderr` הופכים לאובייקטים דמויי קובץ.
        *   `subprocess.DEVNULL`: מפנה את הזרם ל"שום מקום" (אנלוגי ל-`/dev/null`).
        *   תיאור קובץ פתוח (מספר שלם).
        *   אובייקט קובץ קיים (לדוגמה, קובץ פתוח `open('output.txt', 'w')`).

*   **`capture_output=True` (עבור `run()`):**
    *   אפשרות נוחה, שוות ערך להגדרת `stdout=subprocess.PIPE` ו-`stderr=subprocess.PIPE`.
    *   התוצאה תהיה זמינה ב-`result.stdout` וב-`result.stderr`.

*   **`text=True` (או `universal_newlines=True` לתאימות):**
    *   אם `True`, זרמי `stdout` ו-`stderr` (וכן `stdin`, אם מועברת מחרוזת) ייפתחו במצב טקסט באמצעות קידוד ברירת המחדל (בדרך כלל UTF-8). פענוח/קידוד מתרחש אוטומטית.
    *   אם `False` (ברירת מחדל), הזרמים מטופלים כבתים.
    *   החל מפייתון 3.7, `text` הוא כינוי מועדף עבור `universal_newlines`. ניתן גם לציין קידוד ספציפי באמצעות `encoding` ומטפל שגיאות באמצעות `errors`.

*   **`shell=False` (ברירת מחדל):**
    *   אם `False` (מומלץ מטעמי אבטחה וחיזוי), `args` חייב להיות רשימה. הפקודה מופעלת ישירות.
    *   אם `True`, `args` מועבר כמחרוזת למעטפת המערכת (לדוגמה, `/bin/sh` ביוניקס, `cmd.exe` ב-Windows) לפירוש. זה מאפשר שימוש בתכונות מעטפת (משתנים, החלפות, צינורות), אך **מסוכן** אם `args` מכיל קלט משתמש לא מהימן (סיכון להזרקת פקודות).

*   **`cwd=None`:**
    *   מגדיר את ספריית העבודה הנוכחית עבור תהליך הילד. כברירת מחדל, הוא יורש מתהליך האב.

*   **`env=None`:**
    *   מילון המגדיר משתני סביבה עבור התהליך החדש. כברירת מחדל, סביבת תהליך האב נורשת. אם צוין, הוא מחליף לחלוטין את הסביבה הנורשת. כדי להוסיף/לשנות משתנים תוך שמירה על השאר, יש להעתיק תחילה את `os.environ` ולאחר מכן לשנות אותו.

*   **`timeout=None`:**
    *   זמן מרבי בשניות המוקצה לביצוע פקודה. אם התהליך לא יסתיים בזמן זה, תיזרק חריגה `subprocess.TimeoutExpired`. `Popen.communicate()` גם מקבל `timeout`.

*   **`check=False` (עבור `run()`):**
    *   אם `True` והתהליך מסתיים עם קוד החזרה שאינו אפס, תיזרק חריגה `subprocess.CalledProcessError`.

---


### 4. עבודה עם תוצאות ושגיאות

**אובייקט `CompletedProcess` (תוצאת `run()`):**

```python
import subprocess

try:
    # נסה לבצע פקודה שעלולה להיכשל
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - שגיאת כתיב להדגמה
        capture_output=True,
        text=True,
        check=True, # יזרוק חריגה אם returncode != 0
        timeout=10
    )
    print("הפקודה בוצעה בהצלחה.")
    print("קוד החזרה:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # בדרך כלל ריק בהצלחה

except subprocess.CalledProcessError as e:
    print(f"שגיאת ביצוע פקודה (CalledProcessError):")
    print(f"  פקודה: {e.cmd}")
    print(f"  קוד החזרה: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # עשוי להכיל פלט לפני השגיאה
    print(f"  Stderr: {e.stderr}") # בדרך כלל מידע שגיאה כאן
except subprocess.TimeoutExpired as e:
    print(f"הפקודה לא הסתיימה תוך {e.timeout} שניות.")
    print(f"  פקודה: {e.cmd}")
    if e.stdout: print(f"  Stdout (חלקי): {e.stdout.decode(errors='ignore')}") # stdout הוא בתים
    if e.stderr: print(f"  Stderr (חלקי): {e.stderr.decode(errors='ignore')}") # stderr הוא בתים
except FileNotFoundError:
    print("שגיאה: פקודה או תוכנית לא נמצאו.")
except Exception as e:
    print(f"אירעה שגיאה אחרת: {e}")
```

**תכונות `CompletedProcess`:**
*   `args`: ארגומנטים ששימשו להפעלת התהליך.
*   `returncode`: קוד החזרה של התהליך. 0 בדרך כלל מציין הצלחה.
*   `stdout`: פלט סטנדרטי של התהליך (בתים או מחרוזת, אם `text=True` ו-`capture_output=True`).
*   `stderr`: זרם שגיאות סטנדרטי של התהליך (בתים או מחרוזת, אם `text=True` ו-`capture_output=True`).

**חריגות:**
*   `subprocess.CalledProcessError`: נזרקת אם `check=True` (עבור `run()`) או אם נעשה שימוש ב-`check_call()`, `check_output()` והפקודה יצאה עם קוד שאינו אפס. מכילה `returncode`, `cmd`, `output` (או `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: אם חלף הזמן הקצוב. מכילה `cmd`, `timeout`, `stdout`, `stderr` (פלט חלקי, אם קיים).
*   `FileNotFoundError`: אם קובץ ההפעלה לא נמצא.

**אינטראקציה עם אובייקט `Popen`:**

מחלקה `Popen` נותנת יותר שליטה:

```python
import subprocess
import time

# הפעלת תהליך ברקע
process = subprocess.Popen(["sleep", "5"])
print(f"תהליך PID: {process.pid} הופעל.")

# בדיקת סטטוס לא חוסמת
while process.poll() is None: # poll() מחזיר None אם התהליך עדיין פועל
    print("תהליך עדיין פועל...")
    # ניתן לקרוא פלט כשהוא מגיע (זהירות, עלול לחסום!)
    # line = process.stdout.readline()
    # if line: print(f"פלט: {line.strip()}")
    time.sleep(1)

# המתן לסיום וקבל את כל הפלט/שגיאות
# stdout_data, stderr_data = process.communicate(timeout=10) # דרך בטוחה

# אם communicate() לא שימש, לאחר poll() != None, ניתן לקרוא את הנותרים
if process.stdout:
    for line in process.stdout:
        print(f"פלט סופי: {line.strip()}")

print(f"תהליך הסתיים עם קוד: {process.returncode}")

# אם נדרשת סיום כפוי
# process.terminate() # שולח SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # אם לא הסתיים
#     process.kill()      # שולח SIGKILL
```

*   `process.poll()`: בודק אם תהליך הילד הסתיים. מחזיר את קוד ההחזרה או `None`. לא חוסם.
*   `process.wait(timeout=None)`: ממתין לסיום תהליך הילד. מחזיר את קוד ההחזרה. חוסם.
*   `process.communicate(input=None, timeout=None)`:
    *   הדרך הבטוחה ביותר ליצור אינטראקציה עם תהליך כאשר משתמשים ב-`PIPE`.
    *   שולח נתונים ל-`stdin` (אם `input` צוין), קורא את כל הנתונים מ-`stdout` ו-`stderr` עד הסוף, וממתין לסיום התהליך.
    *   מחזיר טופל `(stdout_data, stderr_data)`.
    *   עוזר למנוע קיפאון שעלול להתרחש בקריאה/כתיבה ישירה ל-`process.stdout`/`process.stdin` אם המאגרים עולים על גדותיהם.
*   `process.terminate()`: שולח אות `SIGTERM` לתהליך (סיום חסד).
*   `process.kill()`: שולח אות `SIGKILL` לתהליך (סיום כפוי).
*   `process.send_signal(signal)`: שולח את האות שצוין לתהליך.
*   `process.stdin`, `process.stdout`, `process.stderr`: אובייקטים דמויי קובץ עבור צינורות, אם נוצרו עם `PIPE`.

---


### 5. תרחישי שימוש מתקדמים

**הפניית פלט של פקודה אחת לקלט של אחרת (צינורות/pipelines):**

מדמה `ps aux | grep python`:

```python
import subprocess

# הפעלת הפקודה הראשונה, ה-stdout שלה יהיה PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# הפעלת הפקודה השנייה, ה-stdin שלה יהיה stdout של הפקודה הראשונה
# stdout של הפקודה השנייה גם הוא PIPE, כדי לקרוא את התוצאה
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # קישור stdout מ-ps ל-stdin עבור grep
    stdout=subprocess.PIPE,
    text=True
)

# חשוב! סגור את stdout של הפקודה הראשונה בתהליך האב,
# כך ש-grep יקבל EOF כאשר ps יסיים.
if ps_process.stdout:
    ps_process.stdout.close()

# קבלת פלט מ-grep
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

**הפעלת תהליכים אסינכרונית:**

`Popen` הוא מטבעו לא חוסם. ניתן להפעיל מספר תהליכים ולנהל אותם במקביל.

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
    print(f"מפעיל: {' '.join(cmd_args)}")
    # עבור אסינכרוניות, עדיף להפנות את stdout/stderr,
    # כדי למנוע הפרעה זה לזה או לקונסולת האב.
    # DEVNULL אם אין צורך בפלט, PIPE אם נחוץ מאוחר יותר.
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

זוהי משימה מורכבת, הדורשת ניהול זהיר של זרמים כדי למנוע קיפאון. `communicate()` טוב להחלפה חד פעמית. עבור סשן אינטראקטיבי ארוך, ייתכן שתידרש קריאה/כתיבה ישירה ל-`p.stdin`, `p.stdout`, `p.stderr` באמצעות I/O לא חוסם או תהליכים נפרדים.

```python
import subprocess

# דוגמה: הפעלת סשן פייתון אינטראקטיבי
process = subprocess.Popen(
    ['python', '-i'], # -i למצב אינטראקטיבי
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # בופר שורה עבור stdout/stderr (לאינטראקטיביות)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # חשוב!

def read_output():
    # קריאת פלט יכולה להיות מורכבת, מכיוון שצריך לדעת מתי לעצור.
    # זוהי דוגמה מאוד פשוטה. למשימות אמיתיות נדרשים פתרונות חזקים יותר.
    # לדוגמה, קריאה עד לדפוס מסוים (הנחיית שורת פקודה).
    output = ""
    # קוראים stdout. ביישום אמיתי, זה צריך להיעשות באופן לא חוסם או בתהליך נפרד.
    # כאן אנו מניחים שלאחר פקודה תהיה פלט כלשהו מיד.
    # זוהי הנחה מאוד שברירית למקרה הכללי!
    try:
        # ל-Popen אין readline עם timeout, זו אחת הקשיים
        # ניתן להשתמש ב-select על process.stdout.fileno()
        # או לקרוא תו אחר תו/שורה אחר שורה בתהליך נפרד
        # לפשטות, זה לא כלול כאן
        while True: # זהירות, עלול לחסום!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # גלאי הנחיה פרימיטיבי
                output += line
                break
            output += line
    except Exception as e:
        print(f"שגיאת קריאה: {e}")
    return output.strip()

# אתחול: קריאת ההנחיה הראשונית
initial_output = ""
# קריאת ברכת פייתון
# זה מאוד פשוט, מכיוון שאיננו יודעים בדיוק כמה שורות לקרוא
for _ in range(5): # ננסה לקרוא כמה שורות
    try:
        # ל-Popen stdout אין timeout, צריך לקרוא בזהירות
        # stdout.readline() עלול לחסום.
        # ביישומים אמיתיים, נדרש כאן select או תהליכים.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # נמצאה הנחיה
    except BlockingIOError:
        break # אם נעשה שימוש בקריאה לא חוסמת
print(f"פלט ראשוני:\n{initial_output.strip()}")


send_command("a = 10")
# לאינטראקציה אינטראקטיבית, קריאת פלט היא החלק המורכב ביותר.
# communicate() אינו מתאים, מכיוון שהוא סוגר זרמים.
# יש לקרוא בזהירות מ-process.stdout ו-process.stderr, 
# ייתכן שבתהליכים נפרדים, כדי למנוע חסימת התהליך הראשי.
# דוגמה זו אינה מוכנה לייצור עבור אינטראקטיביות מורכבת.
# print(read_output()) # read_output זה מאוד פרימיטיבי

send_command("print(a * 2)")
# print(read_output())

# סיום תהליך
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # המתן לסיום ואסוף את הנותר

print("\nפלט סטנדרטי סופי:")
print(stdout_data)
if stderr_data:
    print("\nזרם שגיאות סופי:")
    print(stderr_data)

print(f"תהליך פייתון הסתיים עם קוד: {process.returncode}")

# לאינטראקציה אינטראקטיבית אמיתית, משתמשים לעיתים קרובות ב-pty (פסאודו-טרמינלים)
# באמצעות מודול `pty` במערכות דמויות יוניקס, או ספריות כמו `pexpect`.
```
*אזהרה*: אינטראקציה אינטראקטיבית ישירה עם `Popen` באמצעות `stdin`/`stdout`/`stderr` מורכבת עקב חסימות ובאפרינג. לאינטראקטיביות אמינה, משתמשים לעיתים קרובות בספריות כמו `pexpect` (עבור יוניקס) או מקבילות שעובדות עם פסאודו-טרמינלים (pty).

**עבודה עם קידודים:**
*   השתמש ב-`text=True` (או `universal_newlines=True`) לפענוח/קידוד אוטומטי.
*   במידת הצורך, תוכל לציין `encoding="הקידוד-שלך"` ו-`errors="מטפל-שגיאות"` (לדוגמה, `replace`, `ignore`).
*   אם `text=False` (ברירת מחדל), `stdout` ו-`stderr` יהיו מחרוזות בתים. יהיה עליך לפענח אותן ידנית: `result.stdout.decode('utf-8', errors='replace')`.

---


### 6. אבטחה ושיטות עבודה מומלצות

*   **סיכונים של `shell=True` והזרקת פקודות:**
    *   **לעולם אל** תשתמש ב-`shell=True` עם פקודות הבנויות מקלט משתמש לא מהימן. זה פותח פתח להזרקת פקודות.
    *   דוגמה לפגיעות:
        ```python
        # מסוכן!
        filename = input("הכנס שם קובץ למחיקה: ") # המשתמש מכניס "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   אם `shell=True` נחוץ לחלוטין (לדוגמה, לשימוש בצינורות `|` או החלפות `*` ישירות במחרוזת הפקודה), יש לברוח בזהירות את כל חלקי הפקודה הנוצרים מקלט חיצוני באמצעות `shlex.quote()` (החל מפייתון 3.3).

*   **אימות ובריחת קלט משתמש:**
    *   גם אם `shell=False`, אם ארגומנטים של פקודה נוצרים מקלט משתמש, יש לאמת אותם. לדוגמה, אם צפוי שם קובץ, ודא שזהו אכן שם קובץ חוקי, ולא משהו כמו `../../../etc/passwd`.

*   **העברת ארגומנטים כרשימה (כאשר `shell=False`):**
    *   זוהי הדרך הבטוחה ביותר. כל ארגומנט מועבר כאלמנט רשימה נפרד, ומערכת ההפעלה מטפלת בהם נכון, מבלי לנסות לפרש אותם כחלק מפקודת המעטפת.
    *   דוגמה: `subprocess.run(["rm", filename_from_user])` — כאן `filename_from_user` תמיד יטופל כארגומנט יחיד (שם קובץ), גם אם הוא מכיל רווחים או תווים מיוחדים.

*   **טיפול בשגיאות וקודי החזרה:**
    *   תמיד בדוק את `returncode` או השתמש ב-`check=True` (עבור `run()`) / `check_call()` / `check_output()` כדי לוודא שהפקודה בוצעה בהצלחה.
    *   טפל בחריגות אפשריות (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **ניהול משאבים:**
    *   אם אתה פותח צינורות (`PIPE`), ודא שהם נסגרים בסופו של דבר. `Popen.communicate()` עושה זאת אוטומטית. אם אתה עובד עם `p.stdin/stdout/stderr` ישירות, ייתכן שתידרש סגירה מפורשת שלהם.
    *   ביישומים ארוכי טווח, ודא שתהליכי הילד מסתיימים כהלכה ולא הופכים ל"זומבים". השתמש ב-`p.wait()` או ב-`p.communicate()`. במידת הצורך, השתמש ב-`p.terminate()` או ב-`p.kill()`.

*   **קידודים:** היזהר עם קידודים בעת שימוש ב-`text=True` או בעת פענוח ידני של מחרוזות בתים. בעיות קידוד הן מקור שכיח לשגיאות.

---


### 7. דוגמאות מעשיות

**1. ביצוע פקודה פשוטה ובדיקת קוד החזרה:**
```python
import subprocess

try:
    # מפעילים 'ls' עבור ספרייה קיימת
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"הפקודה 'ls /tmp' בוצעה, קוד החזרה: {result.returncode}")

    # מפעילים 'ls' עבור ספרייה לא קיימת
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # שורה זו לא תבוצע אם check=True, מכיוון שתיזרק חריגה
except subprocess.CalledProcessError as e:
    print(f"שגיאת ביצוע פקודה: {e.cmd}")
    print(f"קוד החזרה: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. לכידת פלט פקודה:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # ציין את הספרייה הנוכחית כספריית עבודה עבור git
    )
    print("סטטוס Git:")
    print(result.stdout)
except FileNotFoundError:
    print("שגיאה: פקודה 'git' לא נמצאה. האם Git מותקן וב-PATH?")
except subprocess.CalledProcessError as e:
    print(f"שגיאת Git: {e.stderr}")
```

**3. שליחת נתונים לקלט תהליך (באמצעות `communicate`):**
```python
import subprocess

# שליחת טקסט ל-'grep' לחיפוש
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
        print("לא נמצאו התאמות 'python'.")
    else: # שגיאת grep אחרת
        print(f"שגיאת grep (קוד {process.returncode}):")
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
    ls_proc.stdout.close()  # מאפשר ל-wc_proc לקבל EOF כאשר ls_proc יסיים

output, _ = wc_proc.communicate()
print(f"מספר קבצים/ספריות: {output.strip()}")
```

**5. שימוש ב-`timeout`:**
```python
import subprocess

try:
    # פקודה שתרוץ 5 שניות
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("הפקודה 'sleep 5' הסתיימה (לא הייתה אמורה עם timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"הפקודה '{e.cmd}' לא הסתיימה תוך {e.timeout} שניות.")
```

---


### 8. סיכום ומשאבים שימושיים

מודול `subprocess` הוא כלי הכרחי לכל מפתח פייתון שצריך ליצור אינטראקציה עם תוכניות חיצוניות או עם סביבת המערכת. הוא מציע איזון בין קלות שימוש (באמצעות `subprocess.run()`) וגמישות עוצמתית (באמצעות `subprocess.Popen()`).

**נקודות מפתח:**
*   העדף את `subprocess.run()` עבור רוב המשימות.
*   השתמש ב-`subprocess.Popen()` לביצוע אסינכרוני או לניהול זרמים מורכב.
*   **הימנע מ-`shell=True`**, במיוחד עם קלט משתמש, עקב סיכוני אבטחה. העבר פקודות כרשימת ארגומנטים.
*   תמיד טפל בקודי החזרה ובחריגות אפשריות.
*   היזהר עם קידודים בעת עבודה עם פלט טקסט (`text=True` או פענוח ידני).
*   `communicate()` — חברך להחלפת נתונים בטוחה באמצעות `PIPE`.

**משאבים שימושיים:**
*   תיעוד רשמי של פייתון למודול `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - מודול תהליכים חדש: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)
