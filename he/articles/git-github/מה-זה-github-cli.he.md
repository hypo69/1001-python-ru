# GitHub CLI

## מה זה GitHub CLI?

**GitHub CLI** (בקיצור `gh`) – זהו כלי שורת פקודה המאפשר לעבוד עם GitHub ישירות מהטרמינל.
באמצעותו ניתן לנהל מאגרים, issues, pull requests, releases וישויות אחרות, מבלי להיכנס לממשק האינטרנט של GitHub.

CLI נוח למפתחים, מהנדסי DevOps ולכל מי שמבצע אוטומציה של עבודה עם GitHub או מעדיף את הטרמינל על פני הדפדפן.

---

## התקנה

GitHub CLI נתמך ב-**Windows**, **macOS** ו-**Linux**.

* **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

* **macOS (דרך Homebrew):**

```bash
brew install gh
```

* **Windows (דרך Winget):**

```powershell
winget install --id GitHub.cli
```

לאחר ההתקנה, בדוק את הגרסה:

```bash
gh --version
```

---

## אימות

כדי לקבל גישה למאגרים ופעולות פרטיות, עליך לאמת:

```bash
gh auth login
```

CLI יציע:

* לבחור GitHub.com או GitHub Enterprise
* שיטת אימות (דפדפן, טוקן, SSH)
* לשמור נתונים להפעלות הבאות

ניתן לבדוק את הסטטוס באמצעות הפקודה:

```bash
gh auth status
```

---

## יכולות עיקריות

### עבודה עם מאגרים

יצירת מאגר חדש:

```bash
gh repo create my-project
```

שכפול:

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
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

רשימת issues:

```bash
gh issue list
```

הצגת issue ספציפי:

```bash
gh issue view 42
```

---

### Pull Requests

יצירת pull request:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
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

| פקודה                         | ייעוד                        |
| ------------------------------- | --------------------------------- |
| `gh help`                       | רשימת כל הפקודות                |
| `gh alias set co "pr checkout"` | יצירת כינוי לפקודה מהירה |
| `gh gist create file.txt`       | העלאת קובץ כ-gist           |
| `gh release create v1.0.0`      | יצירת release                     |

---

## יתרונות GitHub CLI

* חיסכון בזמן: עבודה עם GitHub ללא דפדפן.
* סקריפטים: נוח לאוטומציה ב-bash/PowerShell.
* אינטגרציה עם CI/CD.
* כלי אחיד לפקודות ו-GitHub API.

---

מצוין 🚀 אז בואו ניצור **רשימת בדיקה "10 הפקודות המובילות של GitHub CLI לשימוש יומיומי"**. ניתן להשתמש בה כדף עזר.

---

# ✅ 10 הפקודות המובילות של GitHub CLI לשימוש יומיומי

## 1. אימות

```bash
gh auth login
```

🔑 אימות ב-GitHub דרך דפדפן או טוקן.
שימושי להגדרה ראשונית או שינוי חשבון.

---

## 2. בדיקת סטטוס אימות

```bash
gh auth status
```

📌 בודק אם ה-CLI מחובר ל-GitHub וכיצד.

---

## 3. שכפול מאגר

```bash
gh repo clone owner/repo
```

📥 שכפול מהיר של מאגר ללא חיפוש קישור בממשק האינטרנט.

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

📋 נוח להצגת משימות ובאגים ישירות בטרמינל.

---

## 7. יצירת issue

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 יוצר משימה חדשה או דוח באגים.

---

## 8. יצירת Pull Request

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
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

| פקודה                         | ייעוד                        | דוגמה                          |
| ------------------------------- | --------------------------------- | ------------------------------- |
| `gh auth login`                 | אימות (דפדפן, טוקן, SSH) | `gh auth login`                 |
| `gh auth status`                | בדיקת חיבור נוכחי     | `gh auth status`                |
| `gh alias set co "pr checkout"` | יצירת כינוי לפקודה מהירה |
| `gh config get`                 | קבלת הגדרות CLI            | `gh config get editor`          |

---

## 📂 מאגרים

| פקודה          | ייעוד                             | דוגמה                          |
| ---------------- | -------------------------------------- | ------------------------------ |
| `gh repo create` | יצירת מאגר                      | `gh repo create my-project`    |
| `gh repo clone`  | שכפול מאגר                | `gh repo clone hypo69/hypotez` |
| `gh repo view`   | מידע על מאגר (או פתיחה ב-web) | `gh repo view --web`           |
| `gh repo fork`   | יצירת פורק למאגר               | `gh repo fork owner/repo`      |

---

## 📝 Issues

| פקודה           | ייעוד     | דוגמה                                            |
| ----------------- | -------------- | ------------------------------------------------- |
| `gh issue list`   | רשימת משימות   | `gh issue list`                                   |
| `gh issue create` | יצירת issue  | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | הצגת issue | `gh issue view 42`                                |
| `gh issue close`  | סגירת issue  | `gh issue issue close 42`                               |

---

## 🔀 Pull Requests

| פקודה          | ייעוד                | דוגמה                                      |
| ---------------- | ------------------------- | ------------------------------------------- |
| `gh pr list`     | רשימת PR                 | `gh pr list`                                |
| `gh pr create`   | יצירת PR                | `gh pr create --base main --head feature-x` |
| `gh pr view`     | הצגת PR               | `gh pr view 123 --web`                      |
| `gh pr checkout` | מעבר לענף PR | `gh pr checkout 123`                        |
| `gh pr merge`    | מיזוג PR               | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Releases

| פקודה             | ייעוד             | דוגמה                                             |
| ------------------- | ---------------------- | -------------------------------------------------- |
| `gh release list`   | רשימת releases         | `gh release list`                                  |
| `gh release create` | יצירת release          | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | הוספת קובץ ל-release | `gh release upload v1.0.0 build.zip`               |
| `gh release view`   | הצגת release        | `gh release view v1.0.0`                           |

---

## 📜 Gists

| פקודה          | ייעוד         | דוגמה                    |
| ---------------- | ------------------ | ------------------------- |
| `gh gist create` | יצירת gist       | `gh gist create file.txt` |
| `gh gist list`   | רשימת gists     | `gh gist list`            |
| `gh gist view`   | הצגת gist      | `gh gist gist view abc123`     |
| `gh gist edit`   | עריכת gist | `gh gist edit abc123`     |

---

## ⚙️ Workflows (GitHub Actions)

| פקודה            | ייעוד          | דוגמה                       |
| ------------------ | ------------------- | ---------------------------- |
| `gh workflow list` | רשימת workflows    | `gh workflow list`           |
| `gh workflow view` | הצגת workflow   | `gh workflow view build.yml` |
| `gh workflow run`  | הפעלת workflow  | `gh workflow run build.yml`  |
| `gh run list`      | רשימת הרצות     | `gh run list`                |
| `gh run watch`     | מעקב אחר הרצה | `gh run watch 123456789`     |
