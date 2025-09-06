# GitHub CLI

## Was ist GitHub CLI?

**GitHub CLI** (kurz `gh`) ist ein Kommandozeilen-Tool, das die Arbeit mit GitHub direkt aus dem Terminal ermöglicht.
Damit können Sie Repositories, Issues, Pull Requests, Releases und andere Entitäten verwalten, ohne die GitHub-Weboberfläche aufrufen zu müssen.

CLI ist praktisch für Entwickler, DevOps-Ingenieure und alle, die die Arbeit mit GitHub automatisieren oder das Terminal dem Browser vorziehen.

---

## Installation

GitHub CLI wird unter **Windows**, **macOS** und **Linux** unterstützt.

*   **Linux (Ubuntu/Debian):**

    ```bash
    sudo apt install gh
    ```

*   **macOS (über Homebrew):**

    ```bash
    brew install gh
    ```

*   **Windows (über Winget):**

    ```powershell
    winget install --id GitHub.cli
    ```

Überprüfen Sie nach der Installation die Version:

```bash
gh --version
```

---

## Autorisierung

Um auf private Repositories und Aktionen zugreifen zu können, müssen Sie sich autorisieren:

```bash
gh auth login
```

CLI bietet an:

*   GitHub.com oder GitHub Enterprise auswählen
*   Autorisierungsmethode (Browser, Token, SSH)
*   Daten für zukünftige Starts speichern

Den Status können Sie mit dem Befehl überprüfen:

```bash
gh auth status
```

---

## Grundfunktionen

### Arbeiten mit Repositories

Neues Repository erstellen:

```bash
gh repo create my-project
```

Klonen:

```bash
gh repo clone owner/repo
```

Informationen anzeigen:

```bash
gh repo view owner/repo
```

---

### Issues

Issue erstellen:

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

Issues auflisten:

```bash
gh issue list
```

Bestimmte Issue anzeigen:

```bash
gh issue view 42
```

---

### Pull Requests

Pull Request erstellen:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Anzeigen:

```bash
gh pr list
gh pr view 123
```

Mergen:

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Actions (CI/CD)

Workflows ausführen:

```bash
gh workflow run build.yml
```

Status anzeigen:

```bash
gh run list
```

---

## Nützliche Befehle

| Befehl                          | Zweck                             |
| :------------------------------ | :-------------------------------- |
| `gh help`                       | Liste aller Befehle               |
| `gh alias set co "pr checkout"` | Alias für schnellen Befehl erstellen |
| `gh gist create file.txt`       | Datei als Gist hochladen          |
| `gh release create v1.0.0`      | Release erstellen                 |

---

## Vorteile von GitHub CLI

*   Zeitersparnis: Arbeiten mit GitHub ohne Browser.
*   Skripting: Bequem in Bash/PowerShell zu automatisieren.
*   Integration mit CI/CD.
*   Einheitliches Tool für Befehle und GitHub API.

---

Großartig 🚀 Dann erstellen wir eine **Checkliste "TOP-10 GitHub CLI-Befehle für den täglichen Gebrauch"**. Sie kann als Spickzettel verwendet werden.

---

# ✅ TOP-10 GitHub CLI-Befehle für den täglichen Gebrauch

## 1. Autorisierung

```bash
gh auth login
```

🔑 Autorisierung bei GitHub über Browser oder Token.
Nützlich bei der Ersteinrichtung oder beim Kontowechsel.

---

## 2. Überprüfung des Autorisierungsstatus

```bash
gh auth status
```

📌 Überprüft, ob CLI mit GitHub verbunden ist und wie.

---

## 3. Repository klonen

```bash
gh repo clone owner/repo
```

📥 Schnelles Klonen eines Repositorys ohne Suche nach dem Link in der Weboberfläche.

---

## 4. Neues Repository erstellen

```bash
gh repo create my-project
```

🆕 Erstellen eines Repositorys direkt aus dem Terminal (lokal + auf GitHub).

---

## 5. Informationen zum Repository anzeigen

```bash
gh repo view --web
```

📖 Zeigt Beschreibung und Einstellungen des Repositorys an.
Option `--web` öffnet die Seite sofort im Browser.

---

## 6. Issues auflisten

```bash
gh issue list
```

📋 Praktisch, um Aufgaben und Bugs direkt im Terminal anzuzeigen.

---

## 7. Issue erstellen

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Erstellt eine neue Aufgabe oder einen Bugreport.

---

## 8. Pull Request erstellen

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Hauptwerkzeug für die Teamarbeit: Öffnen eines Pull Requests aus Ihrem Branch.

---

## 9. PR anzeigen und überprüfen

```bash
gh pr view 123
```

👀 Pull Request mit Kommentaren und Überprüfungsstatus anzeigen.
Kann `--web` hinzufügen, um im Browser zu öffnen.

---

## 10. PR mergen und Branch löschen

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Pull Request mergen + Branch in einem Schritt löschen.

---

# 📌 GitHub CLI — Spickzettel

## 🔑 Autorisierung und Einstellungen

| Befehl                          | Zweck                             | Beispiel                          |
| :------------------------------ | :-------------------------------- | :-------------------------------- |
| `gh auth login`                 | Autorisierung (Browser, Token, SSH) | `gh auth login`                 |
| `gh auth status`                | Überprüfung der aktuellen Verbindung | `gh auth status`                |
| `gh alias set co "pr checkout"` | Alias für Befehl erstellen        | `gh alias set co "pr checkout"` |
| `gh config get`                 | CLI-Einstellungen abrufen         | `gh config get editor`          |

---

## 📂 Repositories

| Befehl          | Zweck                                  | Beispiel                         |
| :-------------- | :------------------------------------- | :------------------------------- |
| `gh repo create` | Repository erstellen                   | `gh repo create my-project`    |
| `gh repo clone`  | Repository klonen                      | `gh repo clone hypo69/hypotez` |
| `gh repo view`   | Repo-Info (oder im Web öffnen)         | `gh repo view --web`           |
| `gh repo fork`   | Repository forken                      | `gh repo fork owner/repo`      |

---

## 📝 Issues

| Befehl            | Zweck          | Beispiel                                            |
| :---------------- | :------------- | :-------------------------------------------------- |
| `gh issue list`   | Aufgabenliste  | `gh issue list`                                   |
| `gh issue create` | Issue erstellen | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Issue anzeigen | `gh issue view 42`                                |
| `gh issue close`  | Issue schließen | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Befehl           | Zweck                     | Beispiel                                      |
| :--------------- | :------------------------ | :-------------------------------------------- |
| `gh pr list`     | PRs auflisten             | `gh pr list`                                |
| `gh pr create`   | PR erstellen              | `gh pr create --base main --head feature-branch` |
| `gh pr view`     | PR anzeigen               | `gh pr view 123 --web`                      |
| `gh pr checkout` | Zu PR-Branch wechseln     | `gh pr checkout 123`                        |
| `gh pr merge`    | PR mergen                 | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Releases

| Befehl            | Zweck                  | Beispiel                                             |
| :---------------- | :--------------------- | :--------------------------------------------------- |
| `gh release list` | Releases auflisten     | `gh release list`                                  |
| `gh release create` | Release erstellen      | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Datei zu Release hinzufügen | `gh release upload v1.0.0 build.zip`               |
| `gh release view` | Release anzeigen       | `gh release view v1.0.0`                           |

---

## 📜 Gists

| Befehl           | Zweck          | Beispiel                    |
| :--------------- | :------------- | :-------------------------- |
| `gh gist create` | Gist erstellen | `gh gist create file.txt` |
| `gh gist list`   | Gists auflisten | `gh gist list`            |
| `gh gist view`   | Gist anzeigen  | `gh gist view abc123`     |
| `gh gist edit`   | Gist bearbeiten | `gh gist edit abc123`     |

---

## ⚙️ Workflows (GitHub Actions)

| Befehl             | Zweck             | Beispiel                       |
| :----------------- | :---------------- | :----------------------------- |
| `gh workflow list` | Workflows auflisten | `gh workflow list`           |
| `gh workflow view` | Workflow anzeigen | `gh workflow view build.yml` |
| `gh workflow run`  | Workflow ausführen | `gh workflow run build.yml`  |
| `gh run list`      | Läufe auflisten   | `gh run list`                |
| `gh run watch`     | Lauf beobachten   | `gh run watch 123456789`     |
