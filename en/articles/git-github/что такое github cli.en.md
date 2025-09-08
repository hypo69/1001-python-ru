<!-- Translated to en -->
# GitHub CLI

## What is GitHub CLI?

**GitHub CLI** (short for `gh`) is a command-line tool that allows you to work with GitHub directly from your terminal.
With it, you can manage repositories, issues, pull requests, releases, and other entities without going to the GitHub web interface.

CLI is convenient for developers, DevOps engineers, and anyone who automates work with GitHub or prefers the terminal over a browser.

---

## Installation

GitHub CLI is supported on **Windows**, **macOS**, and **Linux**.

* **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

* **macOS (via Homebrew):**

```bash
brew install gh
```

* **Windows (via Winget):**

```powershell
winget install --id GitHub.cli
```

After installation, check the version:

```bash
gh --version
```

---

## Authorization

To access private repositories and actions, you need to authorize:

```bash
gh auth login
```

CLI will prompt you to:

* choose GitHub.com or GitHub Enterprise
* authorization method (browser, token, SSH)
* save data for subsequent launches

You can check the status with the command:

```bash
gh auth status
```

---

## Main features

### Working with repositories

Creating a new repository:

```bash
gh repo create my-project
```

Cloning:

```bash
gh repo clone owner/repo
```

Viewing information:

```bash
gh repo view owner/repo
```

---

### Issues

Creating an issue:

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

List of issues:

```bash
gh issue list
```

Viewing a specific issue:

```bash
gh issue view 42
```

---

### Pull Requests

Creating a pull request:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Viewing:

```bash
gh pr list
gh pr view 123
```

Merging:

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Actions (CI/CD)

Running workflows:

```bash
gh workflow run build.yml
```

Viewing status:

```bash
gh run list
```

---

## Useful commands

| Command                         | Purpose                           |
| ------------------------------- | --------------------------------- |
| `gh help`                       | list all commands                 |
| `gh alias set co "pr checkout"` | create an alias for a quick command |
| `gh gist create file.txt`       | upload file as gist               |
| `gh release create v1.0.0`      | create release                    |

---

## Advantages of GitHub CLI

* Time saving: work with GitHub without a browser.
* Scripting: convenient to automate in bash/PowerShell.
* CI/CD integration.
* Single tool for commands and GitHub API.

---

Great 🚀 Then let's make a **checklist "TOP-10 GitHub CLI commands for daily use"**. It can be used as a cheat sheet.

---

# ✅ TOP-10 GitHub CLI commands for daily use

## 1. Authorization

```bash
gh auth login
```

🔑 Authorize to GitHub via browser or token.
Useful for first-time setup or account changes.

---

## 2. Check authorization status

```bash
gh auth status
```

📌 Checks if the CLI is connected to GitHub and how.

---

## 3. Clone repository

```bash
gh repo clone owner/repo
```

📥 Quick cloning of a repository without searching for a link in the web interface.

---

## 4. Create a new repository

```bash
gh repo create my-project
```

🆕 Create a repository directly from the terminal (locally + on GitHub).

---

## 5. View repository information

```bash
gh repo view --web
```

📖 Shows repository description and settings.
The `--web` option immediately opens the page in the browser.

---

## 6. List issues

```bash
gh issue list
```

📋 Convenient for viewing tasks and bugs directly in the terminal.

---

## 7. Create an issue

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Creates a new task or bug report.

---

## 8. Create Pull Request

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Main tool for teamwork: opening a Pull Request from your branch.

---

## 9. View and check PR

```bash
gh pr view 123
```

👀 View Pull Request with comments and check statuses.
You can add `--web` to open in browser.

---

## 10. Merge PR with branch deletion

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Merge Pull Request + delete branch in one step.


---

# 📌 GitHub CLI — Cheat Sheet

## 🔑 Authorization and settings

| Команда                         | Purpose                           |
| ------------------------------- | --------------------------------- |
| `gh auth login`                 | Authorization (browser, token, SSH) | `gh auth login`                 |
| `gh auth status`                | Check current connection          | `gh auth status`` |
| `gh alias set co "pr checkout"` | Create alias for command          | `gh alias set co "pr checkout"` |
| `gh config get`                 | Get CLI settings                  | `gh config get editor`          |

---

## 📂 Repositories

| Command          | Purpose                                |
| ---------------- | -------------------------------------- |
| `gh repo create` | Create repository                      | `gh repo create my-project`    |
| `gh repo clone`  | Clone repository                       | `gh repo clone hypo69/hypotez` |
| `gh repo view`   | Repo info (or open in web)             | `gh repo view --web`           |
| `gh repo fork`   | Fork repository                        | `gh repo fork owner/repo`      |

---

## 📝 Issues

| Command           | Purpose        |
| ----------------- | -------------- |
| `gh issue list`   | List tasks     | `gh issue list`                                   |
| `gh issue create` | Create issue   | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | View issue     | `gh issue view 42`                                |
| `gh issue close`  | Close issue    | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Command          | Purpose                   |
| ---------------- | ------------------------- |
| `gh pr list`     | List PRs                  | `gh pr list`                                |
| `gh pr create`   | Create PR                 | `gh pr create --base main --head feature-x` |
| `gh pr view`     | View PR                   | `gh pr view 123 --web`                      |
| `gh pr checkout` | Switch to PR branch       | `gh pr checkout 123`                        |
| `gh pr merge`    | Merge PR                  | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Releases

| Command             | Purpose                |
| ------------------- | ---------------------- |
| `gh release list`   | List releases          | `gh release list`                                  |
| `gh release create` | Create release         | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Add file to release    | `gh release upload v1.0.0 build.zip`               |
| `gh release view`   | View release           | `gh release view v1.0.0`                           |

---

## 📜 Gists

| Command          | Purpose        |
| ---------------- | -------------- |
| `gh gist create` | Create gist    | `gh gist create file.txt` |
| `gh gist list`   | List gists     | `gh gist list`            |
| `gh gist view`   | View gist      | `gh gist view abc123`     |
| `gh gist edit`   | Edit gist      | `gh gist edit abc123`     |

---

## ⚙️ Workflows (GitHub Actions)

| Command            | Purpose             |
| ------------------ | ------------------- |
| `gh workflow list` | List workflows      | `gh workflow list`           |
| `gh workflow view` | View workflow       | `gh workflow view build.yml` |
| `gh workflow run`  | Run workflow        | `gh workflow run build.yml`  |
| `gh run list`      | List runs           | `gh run list`                |
| `gh run watch`     | Watch run           | `gh run watch 123456789`     |
