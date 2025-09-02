**מדריך פקודות PowerShell**

**1. יסודות ניווט ועבודה עם קבצים וספריות**

*   **`Get-ChildItem` (או `gci`, `ls`, `dir`)**: מקבל רשימה של קבצים ותתי-ספריות במיקום שצוין.
    *   **תחביר**: `Get-ChildItem [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Path`: מציין את הנתיב לספרייה.
        *   `-Include`: מסנן לפי שם קובץ (עם תווים כלליים `*` ו-`?`).
        *   `-Exclude`: מוציא קבצים לפי שם.
        *   `-Recurse`: מציג קבצים ותיקיות בכל תתי-הספריות.
        *   `-Force`: הצג קבצים מוסתרים.
        *   `-File`: הצג קבצים בלבד.
        *   `-Directory`: הצג תיקיות בלבד.
    *   **דוגמאות:**
        *   `Get-ChildItem`: רשימת קבצים ותיקיות בספרייה הנוכחית.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: רשימת קבצים ותיקיות ב-`C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: רשימת קבצי טקסט בלבד בספרייה הנוכחית.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: הצג את כל הספריות בכונן C.
        *  `Get-ChildItem -Force`: הצג את כל הקבצים, כולל מוסתרים.

*   **`Set-Location` (או `sl`, `cd`)**: משנה את הספרייה הנוכחית.
    *   **תחביר**: `Set-Location [נתיב]`
    *   **דוגמאות:**
        *   `Set-Location C:\Windows`: עבור לספריית `C:\Windows`.
        *   `Set-Location ..`: עבור לספריית האב.
        * `Set-Location /` - עבור לשורש הכונן.
*   **`New-Item`**: יוצר קובץ או ספרייה חדשים.
    *   **תחביר**: `New-Item -Path [נתיב] -ItemType [סוג] -Name [שם]`
    *   **פרמטרים עיקריים:**
        *   `-ItemType`: `file` או `directory`.
        *   `-Name`: שם הפריט החדש.
        *   `-Value`: תוכן הקובץ.
    *   **דוגמאות:**
        *   `New-Item -ItemType directory -Name NewFolder`: צור תיקייה `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: צור קובץ ריק `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: צור קובץ `myfile.txt` עם תוכן.

*  **`Remove-Item` (או `rm`, `del`, `erase`)**: מוחק קבצים וספריות.
    *   **תחביר:** `Remove-Item [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
         *   `-Recurse`:  מחק את כל תתי-הספריות.
        *   `-Force`: מחיקה כפויה (כולל קבצים "לקריאה בלבד" וספריות).
       *  `-Confirm` - בקש אישור לכל מחיקה.
    *   **דוגמאות:**
        *   `Remove-Item myfile.txt`: מחק את הקובץ `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: מחק את תיקיית `C:\Temp` עם כל התיקיות והקבצים המקוננים.

*   **`Copy-Item`**: מעתיק קבצים וספריות.
    *   **תחביר**: `Copy-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Recurse`: העתק את כל תתי-הספריות.
        *   `-Force`: דרוס קבצים קיימים ללא בקשה.
    *   **דוגמאות:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: העתק את הקובץ `myfile.txt` ל-`mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: העתק את תיקיית `C:\Source` לכל תתי-הספריות בתיקיית `D:\Backup`.

*   **`Move-Item`**: מעביר קבצים וספריות.
    *   **תחביר**: `Move-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
      *  `-Force` - העבר בכוח ודרוס.

    *   **דוגמאות:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: העבר את הקובץ `myfile.txt` לתיקיית `D:\Documents`.
         *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force`: העבר את תיקיית C:\MyFolder ל-D:\ בכוח, גם אם קיימת שם תיקייה באותו שם.

*   **`Rename-Item`**: משנה שם של קובץ או ספרייה.
    *   **תחביר**: `Rename-Item -Path [נתיב] -NewName [שם_חדש]`
    *   **דוגמה:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: שנה את שם הקובץ `myfile.txt` ל-`newfile.txt`.

*   **`Get-Content` (או `gc`)**: מציג או מקבל את תוכן הקובץ.
    *   **תחביר**: `Get-Content [נתיב]`
    *   **דוגמה:**
        *   `Get-Content myfile.txt`: הצג את תוכן הקובץ `myfile.txt`.
*   **`Set-Content`**: מחליף או יוצר את תוכן הקובץ.
    *  **תחביר:** `Set-Content [נתיב] [פרמטרים]`
        *  `-value` - טקסט לכתיבה.
   *   **דוגמה:** `Set-Content myfile.txt "טקסט חדש"` - החלף את תוכן הקובץ `myfile.txt`.

*   **`Add-Content`**: מוסיף תוכן לסוף הקובץ.
   * **תחביר:** `Add-Content [נתיב] [פרמטרים]`
       *  `-value` - טקסט להוספה.

   *   **דוגמה:** `Add-Content myfile.txt "טקסט נוסף"` - הוסף טקסט לסוף `myfile.txt`.

**2. ניהול תהליכים:**

*   **`Get-Process` (או `gps`)**: מקבל רשימה של תהליכים פועלים.
    *   **תחביר**: `Get-Process [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Name`: סנן לפי שם תהליך.
        *   `-Id`: סנן לפי מזהה תהליך.
        *    `-IncludeUserName`: הצג את המשתמש שהפעיל את התהליך.
    *   **דוגמאות:**
        *   `Get-Process`: רשימת כל התהליכים הפועלים.
        *   `Get-Process -Name notepad`: רשימת תהליכים בשם `notepad`.
        *    `Get-Process -IncludeUserName`: רשימת כל התהליכים הפועלים עם משתמשים.

*   **`Stop-Process`**: מסיים תהליך.
    *   **תחביר**: `Stop-Process [פרמטרים]`
     *  `-Id` - ציין מזהה תהליך.
    *   `-Name` - ציין שם תהליך.
    *  `-Force` - סיים תהליך בכוח.
    *   **דוגמאות:**
        *   `Stop-Process -Name notepad`: סיים את כל תהליכי `notepad`.
         *    `Stop-Process -Id 1234` : סיים תהליך עם מזהה 1234.
        *    `Stop-Process -Name chrome -Force` : סיים בכוח את כל תהליכי `chrome`.

**3. ניהול שירותים:**

*   **`Get-Service`**: מקבל רשימה של שירותים.
    *   **תחביר**: `Get-Service [פרמטרים]`
    *   **פרמטרים עיקריים:**
         * `-Name`: הצג רק שירותים עם השם שצוין.
         * `-DisplayName`: הצג רק שירותים עם השם המוצג שצוין.
        *   `-Status`: סנן לפי סטטוס (Running, Stopped).
    *   **דוגמאות:**
        *   `Get-Service`: רשימת כל השירותים.
        *   `Get-Service -Name Spooler`: הצג את שירות Spooler.
       *   `Get-Service -Status Running`: הצג שירותים פועלים.
*  **`Start-Service`**: מפעיל שירות.
   *   **תחביר**: `Start-Service [שם_שירות]`
   *   **דוגמה:** `Start-Service Spooler` - הפעל את שירות Spooler.

*   **`Stop-Service`**: עוצר שירות.
    *   **תחביר**: `Stop-Service [שם_שירות]`
        *  `-Force` - עצור שירות בכוח.
    *   **דוגמה:** `Stop-Service Spooler`: עצור את שירות Spooler.
        *   `Stop-Service Spooler -Force` - עצור את שירות Spooler בכוח.

*  **`Restart-Service`**: מפעיל מחדש שירות.
   *   **תחביר:** `Restart-Service [שם_שירות]`
   *   **דוגמה:** `Restart-Service Spooler` - הפעל מחדש את שירות Spooler.

**4. עבודה עם רשת**

*   **`Test-NetConnection`**: בודק חיבור רשת.
    *   **תחביר**: `Test-NetConnection [שם_מארח_או_כתובת_IP] [פרמטרים]`
    *  `-Port` - מספר פורט.
    *   **דוגמאות:**
        *   `Test-NetConnection google.com`: בדוק חיבור ל-`google.com`.
        * `Test-NetConnection google.com -Port 80`: בדוק חיבור ל-google.com בפורט 80.
*   **`Get-NetIPConfiguration`**: מקבל תצורת רשת.
    *   **תחביר**: `Get-NetIPConfiguration`
    *   **דוגמה:**
        *   `Get-NetIPConfiguration`: הצג תצורת רשת.
*   **`Resolve-DnsName`**: שולח שאילתת מידע DNS.
    *   **תחביר**: `Resolve-DnsName [שם_מארח]`
    *   **דוגמה:** `Resolve-DnsName google.com`: שלח שאילתת מידע DNS עבור `google.com`.

**5. עבודה עם הרישום**

*   **`Get-ItemProperty`**: מקבל ערך מאפיין מהרישום.
    *   **תחביר**: `Get-ItemProperty -Path [נתיב_ברישום]`
    *   **דוגמה:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`**: מגדיר ערך מאפיין ברישום.
    *   **תחביר**: `Set-ItemProperty -Path [נתיב_ברישום] -Name [שם_מאפיין] -Value [ערך]`
    *   **דוגמה:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

**6. אחר**

*   **`Clear-Host`**: מנקה את מסך הקונסולה.
    *   **תחביר:** `Clear-Host`
*   **`Get-Date`**: מקבל את התאריך והשעה הנוכחיים.
    *   **תחביר:** `Get-Date`
*    **`Start-Process`**: מפעיל תוכנית או פותח קובץ.
    *   **תחביר:** `Start-Process [שם_תוכנית_או_קובץ] [אפשרויות]`
   *   **דוגמאות:**
        *   `Start-Process notepad.exe`: הפעל את פנקס הרשימות.
        *   `Start-Process myfile.txt`: פתח את הקובץ `myfile.txt` באמצעות התוכנית המוגדרת כברירת מחדל.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"` - פתח אתר אינטרנט בכרום.

*   **`Get-Help`**: מציג עזרה עבור פקודה.
    *   **תחביר**: `Get-Help [שם_פקודה]`
    *   **דוגמה:** `Get-Help Get-Process`: הצג עזרה עבור הפקודה `Get-Process`.
*   **`Exit`**: מסיים את סשן PowerShell.
    *   **תחביר:** `Exit`
*  **`Get-Variable`**: מציג משתנים נוכחיים.
    *  **תחביר**: `Get-Variable`
*  **`Get-Alias`**: מציג כינויים לפקודות.
    *   **תחביר**: `Get-Alias`
*  **`Set-Alias`**: יוצר כינוי לפקודה.
    *  **תחביר**: `Set-Alias [שם_כינוי] [שם_פקודה]`
    *  **דוגמה**: `Set-Alias gci Get-ChildItem`

**הערות:**

*   פקודות `PowerShell` (cmdlets) בדרך כלל בעלות צורה של `פועל-שם עצם` (לדוגמה, `Get-Process`, `Set-Location`).
*   `PowerShell` אינו רגיש לרישיות, כך שתוכל לכתוב פקודות כ-`Get-ChildItem` או `get-childitem`.
*   `PowerShell` עובד עם אובייקטים, כך שתוכל להשתמש באופרטור `|` כדי להעביר את הפלט של פקודה אחת לקלט של אחרת (לדוגמה, `Get-Process | Sort-Object -Property CPU`).
*  פקודות רבות תומכות בשימוש בתווים כלליים (*) לעבודה עם מספר קבצים (לדוגמה `Get-ChildItem *.txt`).
*   עבור עבודה עם פקודות מסוימות נדרשות הרשאות מנהל מערכת.
