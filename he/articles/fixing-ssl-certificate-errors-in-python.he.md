# כיצד לתקן את השגיאה SSLCertVerificationError בפייתון

    נתקלת בשגיאה `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` בעת ניסיון לבצע בקשת HTTPS בפייתון באמצעות `requests` או `urllib3`?
במאמר זה, אראה לך כיצד לאבחן ולתקן בעיה זו.

השגיאה אומרת שפייתון לא הצליח לאמת את תעודת ה-SSL/TLS של האתר שאליו אתה מתחבר מכיוון שלא הצליח למצוא תעודת שורש מהימנה במאגר שלו.

## שלב 1: אבחון הבעיה באמצעות OpenSSL (מומלץ)

    לפני שינוי קוד הפייתון, בדוק את חיבור ה-SSL באמצעות כלי השירות `openssl`. זה יעזור לך להבין אם הבעיה ספציפית לפייתון או קשורה להגדרות מערכת או לשרת עצמו.

1.  **התקן את OpenSSL** אם אין לך אותו (לרוב מותקן מראש בלינוקס/macOS; עבור Windows, הורד מה[אתר הרשמי](https://www.openssl.org/source/) או השתמש במנהלי חבילות כמו Chocolatey/Scoop).
2.  **הפעל את הפקודה** בטרמינל שלך (שורת הפקודה), החלף את `<hostname>` בכתובת האתר (ללא `https://`) ואת `<port>` בפורט (בדרך כלל 443 עבור HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # דוגמה עבור rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **נתח את הפלט:** שים לב לשורה `Verify return code`. אם היא מכילה שגיאה כמו `unable to get local issuer certificate` (קוד 20) או `certificate verify failed` (קוד 21), זה מאשר בעיה באמון בתעודה ברמת המערכת או במאגר שבו OpenSSL משתמש.

## שלב 2: בחר שיטת פתרון

    ישנן מספר דרכים לתקן את השגיאה `SSLCertVerificationError`. בחר את המתאימה ביותר למצבך.

### שיטה 1: השבת אימות SSL (מהיר, אך לא מאובטח)

    שיטה זו משביתה לחלוטין את אימות התעודה. השתמש בה **רק** לבדיקות זמניות, סקריפטים חד-פעמיים, ו**רק** עבור אתרים שאתה בוטח בהם לחלוטין.

⚠️ **אזהרה:** השבתת אימות הופכת את החיבור שלך לפגיע להתקפות אדם בתווך (MITM). **לעולם אל תשתמש ב-`verify=False` בקוד ייצור או בעת עבודה עם נתונים רגישים!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # דוגמת URL

# השבת אימות SSL
try:
    # דיכוי אזהרות לגבי בקשות לא מאובטחות (אופציונלי)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # בדוק שגיאות HTTP (4xx, 5xx)

    # הקוד שלך לטיפול בתגובה, לדוגמה, שמירת קובץ
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("קובץ הורד בהצלחה (עם אימות SSL מושבת).")

except requests.exceptions.RequestException as e:
    print(f"שגיאה בהורדת קובץ: {e}")

finally:
    # חשוב: אם השבתת אזהרות גלובלית,
    # ייתכן שתרצה להפעיל אותן מחדש לאחר השלמת הבקשה,
    # אם כי זה בדרך כלל לא נחוץ אם הסקריפט מסתיים.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### שיטה 2: התקנה/עדכון תעודות עבור פייתון (תלוי פלטפורמה)

    פייתון עשוי להגיע עם סקריפטים להתקנה או עדכון של סט תעודות השורש מחבילת `certifi`.

*   **ב-macOS:**
    1.  עבור לתיקיית ההתקנה של פייתון (בדרך כלל `/Applications/Python <version>/`).
    2.  מצא ולחץ פעמיים על הקובץ `Install Certificates.command`. הוא יתקין/יעדכן את `certifi` ויקשר את מודול `ssl` הסטנדרטי לתעודות אלו.
*   **ב-Windows:**
    1.  לפעמים בעת התקנת פייתון, נוצר סקריפט `install_certificates.bat`. חפש אותו בתיקיית `Scripts` בתוך תיקיית ההתקנה של פייתון (לדוגמה, `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\Scripts\`).
    2.  אם מצאת אותו, הפעל אותו.
    3.  אם הסקריפט אינו שם, שיטה זו ככל הנראה לא תעבוד. השתמש בשיטה 3.

### שיטה 3: השתמש בחבילת `certifi` ישירות (מומלץ, חוצה פלטפורמות)

    זוהי הדרך האמינה ביותר להורות לפייתון במפורש באיזה סט של תעודות שורש להשתמש.

1.  **התקן את `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **השתמש ב-`certifi` בקוד שלך:** העבר את הנתיב לקובץ התעודה של `certifi` לפרמטר `verify` של הפונקציה `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # דוגמת URL

    try:
        # ציין במפורש להשתמש בתעודות מ-certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # הקוד שלך לטיפול בתגובה
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("קובץ הורד בהצלחה באמצעות תעודות certifi.")

    except requests.exceptions.RequestException as e:
        print(f"שגיאה בהורדת קובץ: {e}")
    ```
    גם אם `requests` יכול להשתמש ב-`certifi` כברירת מחדל, ציון מפורש של `verify=certifi.where()` מבטיח התנהגות זו.

### שיטה 4: השתמש במאגרי מערכת או במשתני סביבה (מתקדם)

    מודול `ssl` של פייתון יכול גם לחפש תעודות במאגרי מערכת או בנתיבים שצוינו במשתני סביבה. זה שימושי, לדוגמה, בסביבות ארגוניות עם רשויות אישורים (CAs) משלהן.

1.  **מאגרי מערכת:**
    *   **לינוקס/macOS:** פייתון משתמש לעיתים קרובות אוטומטית בתעודות מערכת (לדוגמה, מ-`/etc/ssl/certs/`). ודא שלמערכת שלך יש תעודות שורש עדכניות (`sudo apt update && sudo apt install ca-certificates` עבור דביאן/אובונטו, `sudo yum update ca-certificates` עבור CentOS/RHEL).
    *   **Windows:** פייתון *עשוי* לנסות להשתמש במאגר המערכת של Windows, אך זה לא תמיד עובד באופן אמין ללא חבילות נוספות (לדוגמה, `python-certifi-win32`). מומלץ להשתמש ב-`certifi` (שיטה 3).
2.  **משתני סביבה:** ניתן לציין במפורש את הנתיב לקובץ או לתיקייה עם תעודות:
    *   `SSL_CERT_FILE`: ציין את הנתיב ל*קובץ* (בפורמט PEM) המכיל את כל תעודות השורש המהימנות.
    *   `SSL_CERT_DIR`: ציין את הנתיב ל*תיקייה* שבה כל תעודה נמצאת בקובץ PEM נפרד עם שם בצורת hash (השתמש ב-`c_rehash` מ-OpenSSL כדי להכין את התיקייה).

    **כיצד להגדיר משתני סביבה:**

    *   **לינוקס/macOS (זמני, עבור הסשן הנוכחי):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, זמני):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, זמני):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    כדי להוסיף CA משלך (לדוגמה, ארגוני), עליך להוסיף את התעודה שלו לקובץ `SSL_CERT_FILE` או לתיקיית `SSL_CERT_DIR`.

## שלב 3 (בונוס): כיצד ליצור תעודה בחתימה עצמית לפיתוח מקומי

    אם אתה מפתח שרת אינטרנט מקומי (API, אתר אינטרנט) ורוצה לבדוק אותו באמצעות HTTPS, תזדקק לתעודת SSL. מכיוון שאין לך דומיין ציבורי כדי להשיג תעודה מ-CA רגיל, תוכל ליצור תעודה *בחתימה עצמית*.

**שימוש ב-OpenSSL (חוצה פלטפורמות):**

1.  **הפעל את הפקודה:** פקודה זו תיצור מפתח פרטי (`key.pem`) ואת התעודה עצמה (`cert.pem`), תקפים ל-10 שנים, עבור `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: יוצר מפתח ללא סיסמה (נוח לפיתוח).
    *   `-subj "/CN=localhost"`: מגדיר את השם הנפוץ.
    *   `-addext "subjectAltName = ..."`: מוסיף שמות חלופיים לנושא (חשוב לדפדפנים ולקוחות מודרניים).

2.  **השתמש ב-`key.pem` וב-`cert.pem`** בהגדרות של שרת האינטרנט המקומי שלך (Flask, Django, Node.js וכו') כדי לאפשר HTTPS.

**שימוש ב-PowerShell (Windows 10/11):**

1.  **הפעל את הפקודה ב-PowerShell (עם הרשאות מנהל):** פקודה זו תיצור תעודה ותמקם אותה במאגר התעודות של המחשב.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    ייתכן שתצטרך לייצא תעודה זו מהמאגר (`certlm.msc`) לקבצי `.pfx` או `.pem` לשימוש על ידי שרת האינטרנט שלך.

**הערה:** דפדפנים ולקוחות HTTP (כולל `requests` של פייתון כברירת מחדל) לא יבטחו בתעודות בחתימה עצמית. בעת גישה לשרת כזה, תקבל אזהרה או שגיאת SSL. לבדיקה, תצטרך להוסיף תעודה זו לתעודות השורש המהימנות של המערכת/דפדפן שלך, או להשתמש ב-`verify=False` (עבור `requests`), או לציין את הנתיב ל-`cert.pem` שלך באמצעות `verify='/path/to/cert.pem'`.
