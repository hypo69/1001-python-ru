# GitHub CLI

## Что такое GitHub CLI?

**GitHub CLI** (коротко `gh`) — это инструмент командной строки, который позволяет работать с GitHub прямо из терминала.
С его помощью можно управлять репозиториями, issues, pull requests, релизами и другими сущностями, не заходя в веб-интерфейс GitHub.

CLI удобен для разработчиков, DevOps-инженеров и всех, кто автоматизирует работу с GitHub или предпочитает терминал вместо браузера.

---

## Установка

GitHub CLI поддерживается на **Windows**, **macOS** и **Linux**.

* **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

* **macOS (через Homebrew):**

```bash
brew install gh
```

* **Windows (через Winget):**

```powershell
winget install --id GitHub.cli
```

После установки проверь версию:

```bash
gh --version
```

---

## Авторизация

Чтобы получить доступ к приватным репозиториям и действиям, нужно авторизоваться:

```bash
gh auth login
```

CLI предложит:

* выбрать GitHub.com или GitHub Enterprise
* метод авторизации (браузер, токен, SSH)
* сохранить данные для последующих запусков

Проверить статус можно командой:

```bash
gh auth status
```

---

## Основные возможности

### Работа с репозиториями

Создание нового репозитория:

```bash
gh repo create my-project
```

Клонирование:

```bash
gh repo clone owner/repo
```

Просмотр информации:

```bash
gh repo view owner/repo
```

---

### Issues

Создание issue:

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

Список issues:

```bash
gh issue list
```

Просмотр конкретной issue:

```bash
gh issue view 42
```

---

### Pull Requests

Создание pull request:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Просмотр:

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

Просмотр статуса:

```bash
gh run list
```

---

## Полезные команды

| Команда                         | Назначение                        |
| ------------------------------- | --------------------------------- |
| `gh help`                       | список всех команд                |
| `gh alias set co "pr checkout"` | создать алиас для быстрой команды |
| `gh gist create file.txt`       | загрузить файл как gist           |
| `gh release create v1.0.0`      | создать релиз                     |

---

## Преимущества GitHub CLI

* Экономия времени: работа с GitHub без браузера.
* Скриптование: удобно автоматизировать в bash/PowerShell.
* Интеграция с CI/CD.
* Единый инструмент для команд и GitHub API.

---

Отлично 🚀 Тогда сделаем **чеклист "ТОП-10 команд GitHub CLI для ежедневного использования"**. Его можно использовать как шпаргалку.

---

# ✅ ТОП-10 команд GitHub CLI для ежедневного использования

## 1. Авторизация

```bash
gh auth login
```

🔑 Авторизация в GitHub через браузер или токен.
Полезно при первой настройке или смене аккаунта.

---

## 2. Проверка статуса авторизации

```bash
gh auth status
```

📌 Проверяет, подключен ли CLI к GitHub и каким образом.

---

## 3. Клонирование репозитория

```bash
gh repo clone owner/repo
```

📥 Быстрое клонирование репозитория без поиска ссылки в веб-интерфейсе.

---

## 4. Создание нового репозитория

```bash
gh repo create my-project
```

🆕 Создание репозитория прямо из терминала (локально + на GitHub).

---

## 5. Просмотр информации о репозитории

```bash
gh repo view --web
```

📖 Показывает описание и настройки репозитория.
Опция `--web` сразу открывает страницу в браузере.

---

## 6. Список issues

```bash
gh issue list
```

📋 Удобно для просмотра задач и багов прямо в терминале.

---

## 7. Создание issue

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Создает новую задачу или багрепорт.

---

## 8. Создание Pull Request

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Основной инструмент командной работы: открытие Pull Request из своей ветки.

---

## 9. Просмотр и проверка PR

```bash
gh pr view 123
```

👀 Просмотр Pull Request с комментариями и статусами проверок.
Можно добавить `--web`, чтобы открыть в браузере.

---

## 10. Мерж PR с удалением ветки

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Мерж Pull Request + удаление ветки за один шаг.


---

# 📌 GitHub CLI — Шпаргалка

## 🔑 Авторизация и настройки

| Команда                         | Назначение                        | Пример                          |
| ------------------------------- | --------------------------------- | ------------------------------- |
| `gh auth login`                 | Авторизация (браузер, токен, SSH) | `gh auth login`                 |
| `gh auth status`                | Проверка текущего подключения     | `gh auth status`                |
| `gh alias set co "pr checkout"` | Создать алиас для команды         | `gh alias set co "pr checkout"` |
| `gh config get`                 | Получить настройки CLI            | `gh config get editor`          |

---

## 📂 Репозитории

| Команда          | Назначение                             | Пример                         |
| ---------------- | -------------------------------------- | ------------------------------ |
| `gh repo create` | Создать репозиторий                    | `gh repo create my-project`    |
| `gh repo clone`  | Клонировать репозиторий                | `gh repo clone hypo69/hypotez` |
| `gh repo view`   | Инфо о репозитории (или открыть в web) | `gh repo view --web`           |
| `gh repo fork`   | Сделать форк репозитория               | `gh repo fork owner/repo`      |

---

## 📝 Issues

| Команда           | Назначение     | Пример                                            |
| ----------------- | -------------- | ------------------------------------------------- |
| `gh issue list`   | Список задач   | `gh issue list`                                   |
| `gh issue create` | Создать issue  | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Просмотр issue | `gh issue view 42`                                |
| `gh issue close`  | Закрыть issue  | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Команда          | Назначение                | Пример                                      |
| ---------------- | ------------------------- | ------------------------------------------- |
| `gh pr list`     | Список PR                 | `gh pr list`                                |
| `gh pr create`   | Создать PR                | `gh pr create --base main --head feature-x` |
| `gh pr view`     | Просмотр PR               | `gh pr view 123 --web`                      |
| `gh pr checkout` | Переключиться на ветку PR | `gh pr checkout 123`                        |
| `gh pr merge`    | Смёржить PR               | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Releases

| Команда             | Назначение             | Пример                                             |
| ------------------- | ---------------------- | -------------------------------------------------- |
| `gh release list`   | Список релизов         | `gh release list`                                  |
| `gh release create` | Создать релиз          | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Добавить файл к релизу | `gh release upload v1.0.0 build.zip`               |
| `gh release view`   | Просмотр релиза        | `gh release view v1.0.0`                           |

---

## 📜 Gists

| Команда          | Назначение         | Пример                    |
| ---------------- | ------------------ | ------------------------- |
| `gh gist create` | Создать gist       | `gh gist create file.txt` |
| `gh gist list`   | Список gist        | `gh gist list`            |
| `gh gist view`   | Просмотр gist      | `gh gist view abc123`     |
| `gh gist edit`   | Редактировать gist | `gh gist edit abc123`     |

---

## ⚙️ Workflows (GitHub Actions)

| Команда            | Назначение          | Пример                       |
| ------------------ | ------------------- | ---------------------------- |
| `gh workflow list` | Список workflows    | `gh workflow list`           |
| `gh workflow view` | Просмотр workflow   | `gh workflow view build.yml` |
| `gh workflow run`  | Запустить workflow  | `gh workflow run build.yml`  |
| `gh run list`      | Список запусков     | `gh run list`                |
| `gh run watch`     | Следить за запуском | `gh run watch 123456789`     |

