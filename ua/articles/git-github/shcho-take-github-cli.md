# GitHub CLI

## Що таке GitHub CLI?

**GitHub CLI** (скорочено `gh`) — це інструмент командного рядка, який дозволяє працювати з GitHub прямо з терміналу.
За його допомогою можна керувати репозиторіями, issues, pull requests, релізами та іншими сутностями, не заходячи у веб-інтерфейс GitHub.

CLI зручний для розробників, DevOps-інженерів та всіх, хто автоматизує роботу з GitHub або віддає перевагу терміналу замість браузера.

---

## Встановлення

GitHub CLI підтримується на **Windows**, **macOS** та **Linux**.

*   **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

*   **macOS (через Homebrew):**

```bash
brew install gh
```

*   **Windows (через Winget):**

```powershell
winget install --id GitHub.cli
```

Після встановлення перевірте версію:

```bash
gh --version
```

---

## Авторизація

Щоб отримати доступ до приватних репозиторіїв та дій, потрібно авторизуватися:

```bash
gh auth login
```

CLI запропонує:

*   вибрати GitHub.com або GitHub Enterprise
*   метод авторизації (браузер, токен, SSH)
*   зберегти дані для подальших запусків

Перевірити статус можна командою:

```bash
gh auth status
```

---

## Основні можливості

### Робота з репозиторіями

Створення нового репозиторію:

```bash
gh repo create my-project
```

Клонування:

```bash
gh repo clone owner/repo
```

Перегляд інформації:

```bash
gh repo view owner/repo
```

---

### Issues

Створення issue:

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

Список issues:

```bash
gh issue list
```

Перегляд конкретної issue:

```bash
gh issue view 42
```

---

### Pull Requests

Створення pull request:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Перегляд:

```bash
gh pr list
gh pr view 123
```

Мерж:

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Actions (CI/CD)

Запуск workflows:

```bash
gh workflow run build.yml
```

Перегляд статусу:

```bash
gh run list
```

---

## Корисні команди

| Команда                         | Призначення                       |
| :------------------------------ | :-------------------------------- |
| `gh help`                       | список усіх команд                |
| `gh alias set co "pr checkout"` | створити псевдонім для швидкої команди |
| `gh gist create file.txt`       | завантажити файл як gist          |
| `gh release create v1.0.0`      | створити реліз                    |

---

## Переваги GitHub CLI

*   Економія часу: робота з GitHub без браузера.
*   Скриптування: зручно автоматизувати в bash/PowerShell.
*   Інтеграція з CI/CD.
*   Єдиний інструмент для команд та GitHub API.

---

Чудово 🚀 Тоді зробимо **чеклист "ТОП-10 команд GitHub CLI для щоденного використання"**. Його можна використовувати як шпаргалку.

---

# ✅ ТОП-10 команд GitHub CLI для щоденного використання

## 1. Авторизація

```bash
gh auth login
```

🔑 Авторизація в GitHub через браузер або токен.
Корисно при першому налаштуванні або зміні облікового запису.

---

## 2. Перевірка статусу авторизації

```bash
gh auth status
```

📌 Перевіряє, чи підключений CLI до GitHub і яким чином.

---

## 3. Клонування репозиторію

```bash
gh repo clone owner/repo
```

📥 Швидке клонування репозиторію без пошуку посилання у веб-інтерфейсі.

---

## 4. Створення нового репозиторію

```bash
gh repo create my-project
```

🆕 Створення репозиторію прямо з терміналу (локально + на GitHub).

---

## 5. Перегляд інформації про репозиторій

```bash
gh repo view --web
```

📖 Показує опис та налаштування репозиторію.
Опція `--web` одразу відкриває сторінку в браузері.

---

## 6. Список issues

```bash
gh issue list
```

📋 Зручно для перегляду завдань та багів прямо в терміналі.

---

## 7. Створення issue

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Створює нове завдання або баг-репорт.

---

## 8. Створення Pull Request

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Основний інструмент командної роботи: відкриття Pull Request зі своєї гілки.

---

## 9. Перегляд та перевірка PR

```bash
gh pr view 123
```

👀 Перегляд Pull Request з коментарями та статусами перевірок.
Можна додати `--web`, щоб відкрити в браузері.

---

## 10. Мерж PR з видаленням гілки

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Мерж Pull Request + видалення гілки за один крок.


---

# 📌 GitHub CLI — Шпаргалка

## 🔑 Авторизація та налаштування

| Команда                         | Призначення                       | Приклад                         |
| :------------------------------ | :-------------------------------- | :------------------------------ |
| `gh auth login`                 | Авторизація (браузер, токен, SSH) | `gh auth login`                 |
| `gh auth status`                | Перевірка поточного підключення   | `gh auth status`                |
| `gh alias set co "pr checkout"` | Створити псевдонім для команди    | `gh alias set co "pr checkout"` |
| `gh config get`                 | Отримати налаштування CLI         | `gh config get editor`          |

---

## 📂 Репозиторії

| Команда          | Призначення                            | Приклад                        |
| :--------------- | :------------------------------------- | :----------------------------- |
| `gh repo create` | Створити репозиторій                   | `gh repo create my-project`    |
| `gh repo clone`  | Клонувати репозиторій                  | `gh repo clone hypo69/hypotez` |
| `gh repo view`   | Інфо про репозиторій (або відкрити в web) | `gh repo view --web`           |
| `gh repo fork`   | Зробити форк репозиторію               | `gh repo fork owner/repo`      |

---

## 📝 Issues

| Команда           | Призначення     | Приклад                                           |
| :---------------- | :-------------- | :------------------------------------------------ |
| `gh issue list`   | Список завдань  | `gh issue list`                                   |
| `gh issue create` | Створити issue  | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Перегляд issue  | `gh issue view 42`                                |
| `gh issue close`  | Закрити issue   | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Команда          | Призначення               | Приклад                                     |
| :--------------- | :------------------------ | :------------------------------------------ |
| `gh pr list`     | Список PR                 | `gh pr list`                                |
| `gh pr create`   | Створити PR               | `gh pr create --base main --head feature-x` |
| `gh pr view`     | Перегляд PR               | `gh pr view 123 --web`                      |
| `gh pr checkout` | Переключитися на гілку PR | `gh pr checkout 123`                        |
| `gh pr merge`    | Злити PR                  | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Releases

| Команда             | Призначення            | Приклад                                            |
| :------------------ | :--------------------- | :------------------------------------------------- |
| `gh release list`   | Список релізів         | `gh release list`                                  |
| `gh release create` | Створити реліз         | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Додати файл до релізу  | `gh release upload v1.0.0 build.zip`               |
| `gh release view`   | Перегляд релізу        | `gh release view v1.0.0`                           |

---

## 📜 Gists

| Команда          | Призначення        | Приклад                   |
| :--------------- | :----------------- | :------------------------ |
| `gh gist create` | Створити gist      | `gh gist create file.txt` |
| `gh gist list`   | Список gist        | `gh gist list`            |
| `gh gist view`   | Перегляд gist      | `gh gist view abc123`     |
| `gh gist edit`   | Редагувати gist    | `gh gist edit abc123`     |

---

## ⚙️ Workflows (GitHub Actions)

| Команда            | Призначення         | Приклад                       |
| :----------------- | :------------------ | :---------------------------- |
| `gh workflow list` | Список workflows    | `gh workflow list`            |
| `gh workflow view` | Перегляд workflow   | `gh workflow view build.yml`  |
| `gh workflow run`  | Запустити workflow  | `gh workflow run build.yml`   |
| `gh run list`      | Список запусків     | `gh run list`                 |
| `gh run watch`     | Слідкувати за запуском | `gh run watch 123456789`      |
