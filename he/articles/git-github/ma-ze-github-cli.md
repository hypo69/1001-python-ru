# GitHub CLI

## מה זה GitHub CLI?

**GitHub CLI** (בקיצור `gh`) — הוא כלי שורת פקודה המאפשר לעבוד עם GitHub ישירות מהטרמינל שלך.
באמצעותו ניתן לנהל מאגרים, issues, pull requests, releases וישויות אחרות, מבלי להיכנס לממשק האינטרנט של GitHub.

CLI נוח למפתחים, מהנדסי DevOps וכל מי שמבצע אוטומציה של עבודה עם GitHub או מעדיף את הטרמינל על פני הדפדפן.

---

## התקנה

GitHub CLI נתמך ב-**Windows**, **macOS** ו-**Linux**.

*   **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

*   **macOS (באמצעות Homebrew):**

```bash
brew install gh
```

*   **Windows (באמצעות Winget):**

```powershell
winget install --id GitHub.cli
```

לאחר ההתקנה, בדוק את הגרסה:

```bash
gh --version
```

---

## אימות

כדי לקבל גישה למאגרים פרטיים ולפעולות, עליך לבצע אימות:

```bash
gh auth login
```

CLI יציע:

*   לבחור GitHub.com או GitHub Enterprise
*   שיטת אימות (דפדפן, אסימון, SSH)
*   לשמור נתונים להרצות הבאות

ניתן לבדוק סטטוס באמצעות הפקודה:

```bash
gh auth status
```

---

## תכונות עיקריות

### עבודה עם מאגרים

יצירת מאגר חדש:

```bash
gh repo create my-project
```

שיבוט:

```bash
gh repo clone owner/repo
```

הצגת מידע:

```bash
gh repo view owner/repo
```

---

### Issues

יצירת issue:

```bash
gh issue create --title "באג: קריסה בהפעלה" --body "שלבים לשחזור..."
```

רשימת issues:

```bash
gh issue list
```

הצגת issue ספציפית:

```bash
gh issue view 42
```

---

### Pull Requests

יצירת pull request:

```bash
gh pr create --base main --head feature-branch --title "תכונה חדשה" --body "נוספה פונקציונליות חדשה"
```

הצגה:

```bash
gh pr list
gh pr view 123
```

מיזוג:

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Actions (CI/CD)

הפעלת workflows:

```bash
gh workflow run build.yml
```

הצגת סטטוס:

```bash
gh run list
```

---

## פקודות שימושיות

| פקודה                           | מטרה                              | דוגמה                           |
| :------------------------------ | :-------------------------------- | :------------------------------ |
| `gh help`                       | רשימת כל הפקודות                  | `gh help`                       |
| `gh alias set co "pr checkout"` | יצירת כינוי לפקודה מהירה          | `gh alias set co "pr checkout"` |
| `gh gist create file.txt`       | העלאת קובץ כ-gist                 | `gh gist create file.txt`       |
| `gh release create v1.0.0`      | יצירת release                    | `gh release create v1.0.0`      |

---

## יתרונות GitHub CLI

*   חיסכון בזמן: עבודה עם GitHub ללא דפדפן.
*   סקריפטים: נוח לאוטומציה ב-bash/PowerShell.
*   שילוב עם CI/CD.
*   כלי יחיד לפקודות ו-GitHub API.

---

מצוין 🚀 אז בואו ניצור **רשימת בדיקה "10 פקודות GitHub CLI מובילות לשימוש יומיומי"**. ניתן להשתמש בה כדף עזר.

---

# ✅ 10 פקודות GitHub CLI מובילות לשימוש יומיומי

## 1. אימות

```bash
gh auth login
```

🔑 אימות ל-GitHub באמצעות דפדפן או אסימון.
שימושי להגדרה ראשונית או שינוי חשבון.

---

## 2. בדיקת סטטוס אימות

```bash
gh auth status
```

📌 בודק אם ה-CLI מחובר ל-GitHub וכיצד.

---

## 3. שיבוט מאגר

```bash
gh repo clone owner/repo
```

📥 שיבוט מהיר של מאגר ללא חיפוש קישור בממשק האינטרנט.

---

## 4. יצירת מאגר חדש

```bash
gh repo create my-project
```

🆕 יצירת מאגר ישירות מהטרמינל (מקומי + ב-GitHub).

---

## 5. הצגת מידע על מאגר

```bash
gh repo view --web
```

📖 מציג תיאור והגדרות מאגר.
אפשרות `--web` פותחת מיד את הדף בדפדפן.

---

## 6. רשימת issues

```bash
gh issue list
```

📋 נוח לצפייה במשימות ובבאגים ישירות בטרמינל.

---

## 7. יצירת issue

```bash
gh issue create --title "באג: כניסה נכשלה" --body "שלבים לשחזור..."
```

🐞 יוצר משימה חדשה או דוח באג.

---

## 8. יצירת Pull Request

```bash
gh pr create --base main --head feature-branch --title "תכונה חדשה" --body "תיאור..."
```

🔀 כלי עיקרי לעבודת צוות: פתיחת Pull Request מהענף שלך.

---

## 9. הצגה ובדיקת PR

```bash
gh pr view 123
```

👀 הצגת Pull Request עם הערות וסטטוסי בדיקה.
ניתן להוסיף `--web` כדי לפתוח בדפדפן.

---

## 10. מיזוג PR עם מחיקת ענף

```bash
gh pr merge 123 --squash --delete-branch
```

✅ מיזוג Pull Request + מחיקת ענף בצעד אחד.


---

# 📌 GitHub CLI — דף עזר

## 🔑 אימות והגדרות

| פקודה                           | מטרה                              | דוגמה                           |
| :------------------------------ | :-------------------------------- | :------------------------------ |
| `gh auth login`                 | אימות (דפדפן, אסימון, SSH)        | `gh auth login`                 |
| `gh auth status`                | בדיקת חיבור נוכחי                 | `gh auth status`                |
| `gh alias set co "pr checkout"` | יצירת כינוי לפקודה                | `gh alias set co "pr checkout"` |
| `gh config get`                 | קבלת הגדרות CLI                   | `gh config get editor`          |

---

## 📂 מאגרים

| פקודה           | מטרה                               | דוגמה                          |
| :--------------- | :--------------------------------- | :----------------------------- |
| `gh repo create` | יצירת מאגר                         | `gh repo create my-project`    |
| `gh repo clone`  | שיבוט מאגר                        | `gh repo clone hypo69/hypotez` |
| `gh repo view`   | מידע על מאגר (או פתיחה ב-web)     | `gh repo view --web`           |
| `gh repo fork`   | יצירת fork למאגר                  | `gh repo fork owner/repo`      |

---

## 📝 Issues

| פקודה            | מטרה           | דוגמה                                           |
| :--------------- | :------------- | :---------------------------------------------- |
| `gh issue list`  | רשימת משימות   | `gh issue list`                                 |
| `gh issue create`| יצירת issue   | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`  | הצגת issue     | `gh issue view 42`                              |
| `gh issue close` | סגירת issue   | `gh issue close 42`                             |

---

## 🔀 Pull Requests

| פקודה           | מטרה                     | דוגמה                                     |
| :--------------- | :----------------------- | :---------------------------------------- |
| `gh pr list`     | רשימת PRs                | `gh pr list`                              |
| `gh pr create`   | יצירת PR                  | `gh pr create --base main --head feature-x` |
| `gh pr view`     | הצגת PR                  | `gh pr view 123 --web`                    |
| `gh pr checkout` | מעבר לענף PR             | `gh pr checkout 123`                      |
| `gh pr merge`    | מיזוג PR                 | `gh pr merge 123 --squash --delete-branch`|

---

## 📦 Releases

| פקודה            | מטרה                  | דוגמה                                            |
| :--------------- | :-------------------- | :----------------------------------------------- |
| `gh release list`| רשימת releases        | `gh release list`                                |
| `gh release create`| יצירת release        | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload`| הוספת קובץ ל-release  | `gh release upload v1.0.0 build.zip`             |
| `gh release view`| הצגת release          | `gh release view v1.0.0`                         |

---

## 📜 Gists

| פקודה           | מטרה          | דוגמה                    |
| :--------------- | :------------ | :----------------------- |
| `gh gist create` | יצירת gist   | `gh gist create file.txt`|
| `gh gist list`   | רשימת gists   | `gh gist list`           |
| `gh gist view`   | הצגת gist     | `gh gist view abc123`    |
| `gh gist edit`   | עריכת gist    | `gh gist edit abc123`    |

---

## ⚙️ Workflows (GitHub Actions)

| פקודה            | מטרה            | דוגמה                      |
| :--------------- | :-------------- | :------------------------- |
| `gh workflow list`| רשימת workflows | `gh workflow list`         |
| `gh workflow view`| הצגת workflow   | `gh workflow view build.yml`|
| `gh workflow run` | הפעלת workflow  | `gh workflow run build.yml` |
| `gh run list`    | רשימת runs      | `gh run list`              |
| `gh run watch`   | צפייה ב-run    | `gh run watch 123456789`   |
