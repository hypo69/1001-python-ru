![1]('assets/Screenshot 2025-09-02 074636.png')

לצערנו, בממשק GitHub אין כפתור למחיקת כל הרצות ה-workflow בלחיצה אחת. עם זאת, ניתן לעשות זאת בכמה דרכים.

### שימוש ב-GitHub CLI (השיטה המומלצת למחיקה המונית)

זוהי הדרך היעילה ביותר למחוק מספר רב של הרצות.
תצטרך להתקין את [GitHub CLI](https://cli.github.com/).

1.  **אימות (אם עדיין לא עשית זאת):**
    ```bash
    gh auth login
    ```

2.  **מחיקת הרצות:**
    ניתן להשתמש בפקודה כדי לקבל רשימה של כל ההרצות ולאחר מכן למחוק אותן. הנה דוגמה לסקריפט עבור `bash`:

    ```bash
    gh run list --json databaseId -q '.[].databaseId' | xargs -IID gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" -X DELETE
    ```

    פקודה זו מקבלת את מזהי כל ההרצות ולכל אחת מהן מבצעת את פקודת המחיקה באמצעות GitHub API.

    עבור PowerShell, הסקריפט ייראה כך:
    ```powershell
    $workflowRuns = gh api "repos/$OWNER/$REPO/actions/runs" --paginate --jq '.workflow_runs[].id'
    foreach ($runId in $workflowRuns) {
      Write-Host "מוחק הרצת workflow ID: $runId"
      gh api "repos/$OWNER/$REPO/actions/runs/$runId" -X DELETE
    }
    ```
    יהיה עליך להחליף את `$OWNER` ו-`$REPO` בשם הבעלים ובשם המאגר שלך בהתאמה.

### מחיקה ידנית דרך ממשק האינטרנט של GitHub

שיטה זו מתאימה אם יש לך מספר קטן של הרצות למחיקה.

1.  עבור לדף הראשי של המאגר שלך ב-GitHub.
2.  מתחת לשם המאגר, לחץ על לשונית **Actions**.
3.  בסרגל הצד השמאלי, בחר את ה-workflow שהרצות שלו ברצונך למחוק.
4.  תראה רשימה של הרצות של אותו workflow.
5.  עבור כל הרצה שברצונך למחוק, לחץ על תפריט "..." מימין ובחר **Delete workflow run**.
6.  אשר את המחיקה.

ראוי לציין שלאחר מחיקת כל ההרצות, ה-workflow עצמו עשוי להיעלם מהרשימה אם קובץ ה-`.yml` המתאים אינו קיים יותר במאגר.

### שימוש ב-GitHub Actions מוכנות

קיימות פעולות מוכנות ב-[GitHub Marketplace](https://github.com/marketplace?type=actions) שניתן להגדיר למחיקה אוטומטית של הרצות ישנות. לדוגמה, `delete-workflow-runs` מאפשר למחוק הרצות לפי לוח זמנים או לאחר תקופה מסוימת. זוהי דרך נוחה לשמור על ניקיון יומני ה-Actions שלך ללא התערבות ידנית.