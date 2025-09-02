CHIEF:
=================
קושי: 4
-----------------
המשחק "CHIEF" - זהו משחק שבו השחקן משמש כמנהל מפעל, המתכנן ייצור. השחקן קובע את כמות המוצרים המיוצרים מכל סוג, והמחשב קובע האם ערכים אלו עומדים בדרישות הנדרשות. אם לא, השחקן מקבל הודעה אילו ערכים היו שגויים. מטרת המשחק - להגיע לייצור אופטימלי, על ידי ניחוש נכון של כמות המוצרים.

כללי המשחק:
1. המחשב מנחש שלושה ערכים בטווח של 1 עד 10: `targetA`, `targetB` ו-`targetC`.
2. השחקן מזין את ניחושיו לגבי הערכים `userA`, `userB` ו-`userC`.
3. המחשב בודק האם הערכים שהוזנו תואמים לערכים הנסתרים.
4. אם כל שלושת הערכים נוחשו נכון, המשחק מסתיים בניצחון.
5. אם לפחות ערך אחד אינו תואם, המחשב מציג אילו ערכים היו שגויים.
6. המשחק נמשך עד שהשחקן מנחש את כל שלושת הערכים.
-----------------
אלגוריתם:
1.  צור מספרים שלמים אקראיים `targetA`, `targetB` ו-`targetC` בטווח של 1 עד 10.
2.  התחל לולאה "כל עוד לא נוחשו כל המספרים":
    2.1. בקש מהשחקן להזין שלושה מספרים שלמים: `userA`, `userB` ו-`userC`.
    2.2. אתחל את המחרוזת `message` כריקה.
    2.3. אם `userA` אינו שווה ל-`targetA`, הוסף "A" ל-`message`.
    2.4. אם `userB` אינו שווה ל-`targetB`, הוסף "B" ל-`message`.
    2.5. אם `userC` אינו שווה ל-`targetC`, הוסף "C" ל-`message`.
    2.6. אם `message` אינה ריקה, הצג הודעה "שגיאה ב-" ו-`message`.
    2.7. אחרת, הצג הודעה "ניחשת נכון!".
3. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    targetA = random(1, 10)
    targetB = random(1, 10)
    targetC = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחל לולאה: כל עוד לא נוחש"}
    LoopStart --> InputValues["<p align='left'>הכנסת מספרים על ידי המשתמש:
    <code><b>
    userA
    userB
    userC
    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"בדיקה: <code><b>userA == targetA?</b></code>"}
    CheckA -- לא --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"בדיקה: <code><b>userB == targetB?</b></code>"}
    CheckA -- כן --> CheckB
    CheckB -- לא --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"בדיקה: <code><b>userC == targetC?</b></code>"}
    CheckB -- כן --> CheckC
    CheckC -- לא --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"בדיקה: <code><b>message != "" ?</b></code>"}
    CheckC -- כן --> CheckMessage
    CheckMessage -- כן --> OutputWrong["הצג הודעה: <b>שגיאה ב- {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- לא --> OutputWin["הצג הודעה: <b>ניחשת נכון!</b>"]
    OutputWin --> End["סיום"]
    LoopStart -- לא --> End
```
מקרא:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: `targetA`, `targetB`, `targetC` נוצרים באופן אקראי מ-1 עד 10.
    LoopStart - התחלת הלולאה, הנמשכת עד שהשחקן מנחש את כל המספרים.
    InputValues - בקשת המשתמש להזין שלושה מספרים `userA`, `userB`, `userC`.
    InitializeMessage - אתחול מחרוזת ריקה `message`.
    CheckA - בדיקה האם המספר שהוזן `userA` שווה למספר הנסתר `targetA`.
    AppendA - הוספת 'A' ל-`message`, אם `userA` אינו שווה ל-`targetA`.
    CheckB - בדיקה האם המספר שהוזן `userB` שווה למספר הנסתר `targetB`.
    AppendB - הוספת 'B' ל-`message`, אם `userB` אינו שווה ל-`targetB`.
    CheckC - בדיקה האם המספר שהוזן `userC` שווה למספר הנסתר `targetC`.
    AppendC - הוספת 'C' ל-`message`, אם `userC` אינו שווה ל-`targetC`.
    CheckMessage - בדיקה האם המחרוזת `message` ריקה.
    OutputWrong - הצגת הודעה "שגיאה ב-" ותוכן `message`, אם המחרוזת אינה ריקה.
    OutputWin - הצגת הודעה "ניחשת נכון!", אם המחרוזת `message` ריקה.
    End - סיום התוכנית.