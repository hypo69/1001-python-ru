# GitHub CLI

## Cos'è GitHub CLI?

**GitHub CLI** (abbreviato `gh`) è uno strumento da riga di comando che ti consente di lavorare con GitHub direttamente dal terminale.
Con esso, puoi gestire repository, issue, pull request, release e altre entità senza dover accedere all'interfaccia web di GitHub.

CLI è conveniente per sviluppatori, ingegneri DevOps e chiunque automatizzi il lavoro con GitHub o preferisca il terminale al browser.

---

## Installazione

GitHub CLI è supportato su **Windows**, **macOS** e **Linux**.

* **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

* **macOS (tramite Homebrew):**

```bash
brew install gh
```

* **Windows (tramite Winget):**

```powershell
winget install --id GitHub.cli
```

Dopo l'installazione, controlla la versione:

```bash
gh --version
```

---

## Autorizzazione

Per accedere a repository e azioni privati, devi autorizzare:

```bash
gh auth login
```

CLI offrirà:

* scegliere GitHub.com o GitHub Enterprise
* metodo di autorizzazione (browser, token, SSH)
* salvare i dati per le esecuzioni successive

Puoi controllare lo stato con il comando:

```bash
gh auth status
```

---

## Funzionalità principali

### Lavorare con i repository

Creazione di un nuovo repository:

```bash
gh repo create my-project
```

Clonazione:

```bash
gh repo clone owner/repo
```

Visualizzazione delle informazioni:

```bash
gh repo view owner/repo
```

---

### Issue

Creazione di un'issue:

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

Elenco delle issue:

```bash
gh issue list
```

Visualizzazione di un'issue specifica:

```bash
gh issue view 42
```

---

### Pull Requests

Creazione di una pull request:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Visualizzazione:

```bash
gh pr list
gh pr view 123
```

Unione:

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Actions (CI/CD)

Esecuzione di workflow:

```bash
gh workflow run build.yml
```

Visualizzazione dello stato:

```bash
gh run list
```

---

## Comandi utili

| Comando                         | Scopo                               |
| ------------------------------- | ----------------------------------- |
| `gh help`                       | elenca tutti i comandi              |
| `gh alias set co "pr checkout"` | crea un alias per un comando rapido |
| `gh gist create file.txt`       | carica un file come gist            |
| `gh release create v1.0.0`      | crea una release                    |

---

## Vantaggi di GitHub CLI

* Risparmio di tempo: lavorare con GitHub senza browser.
* Scripting: comodo da automatizzare in bash/PowerShell.
* Integrazione con CI/CD.
* Strumento unico per comandi e API GitHub.

---

Eccellente 🚀 Allora creiamo una **checklist "TOP-10 comandi GitHub CLI per l'uso quotidiano"**. Può essere usata come cheat sheet.

---

# ✅ TOP-10 comandi GitHub CLI per l'uso quotidiano

## 1. Autorizzazione

```bash
gh auth login
```

🔑 Autorizza in GitHub tramite browser o token.
Utile per la configurazione iniziale o il cambio di account.

---

## 2. Controlla lo stato dell'autorizzazione

```bash
gh auth status
```

📌 Controlla se la CLI è connessa a GitHub e come.

---

## 3. Clona repository

```bash
gh repo clone owner/repo
```

📥 Clonazione rapida del repository senza cercare un link nell'interfaccia web.

---

## 4. Crea nuovo repository

```bash
gh repo create my-project
```

🆕 Crea repository direttamente dal terminale (locale + su GitHub).

---

## 5. Visualizza le informazioni del repository

```bash
gh repo view --web
```

📖 Mostra la descrizione e le impostazioni del repository.
L'opzione `--web` apre immediatamente la pagina nel browser.

---

## 6. Elenca le issue

```bash
gh issue list
```

📋 Comodo per visualizzare attività e bug direttamente nel terminale.

---

## 7. Crea issue

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Crea una nuova attività o un rapporto di bug.

---

## 8. Crea Pull Request

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Strumento principale per il lavoro di squadra: apertura di una Pull Request dal tuo branch.

---

## 9. Visualizza e controlla PR

```bash
gh pr view 123
```

👀 Visualizza Pull Request con commenti e stati di controllo.
Puoi aggiungere `--web` per aprire nel browser.

---

## 10. Unisci PR con eliminazione del branch

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Unisci Pull Request + elimina branch in un solo passaggio.


---

# 📌 GitHub CLI — Cheat Sheet

## 🔑 Autorizzazione e impostazioni

| Comando                         | Scopo                               |
| ------------------------------- | ----------------------------------- |
| `gh auth login`                 | Autorizzazione (browser, token, SSH) | `gh auth login`                     |
| `gh auth status`                | Controlla la connessione corrente   | `gh auth status`                    |
| `gh alias set co "pr checkout"` | Crea un alias per un comando rapido | `gh alias set co "pr checkout"`     |
| `gh config get`                 | Ottieni le impostazioni della CLI   | `gh config get editor`              |

---

## 📂 Repository

| Comando          | Scopo                                   | Esempio                             |
| ---------------- | --------------------------------------- | ----------------------------------- |
| `gh repo create` | Crea repository                         | `gh repo create my-project`         |
| `gh repo clone`  | Clona repository                        | `gh repo clone hypo69/hypotez`      |
| `gh repo view`   | Info repository (o apri nel web)        | `gh repo view --web`                |
| `gh repo fork`   | Fork repository                         | `gh repo fork owner/repo`           |

---

## 📝 Issue

| Comando           | Scopo           | Esempio                                           |
| ----------------- | --------------- | ------------------------------------------------- |
| `gh issue list`   | Elenca attività | `gh issue list`                                   |
| `gh issue create` | Crea issue      | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Visualizza issue | `gh issue view 42`                                |
| `gh issue close`  | Chiudi issue    | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Comando          | Scopo                     | Esempio                                     |
| ---------------- | ------------------------- | --------------------------------------------- |
| `gh pr list`     | Elenca PR                 | `gh pr list`                                  |
| `gh pr create`   | Crea PR                   | `gh pr create --base main --head feature-x`   |
| `gh pr view`     | Visualizza PR             | `gh pr view 123 --web`                        |
| `gh pr checkout` | Passa al branch PR        | `gh pr checkout 123`                          |
| `gh pr merge`    | Unisci PR                 | `gh pr merge 123 --squash --delete-branch`    |

---

## 📦 Release

| Comando             | Scopo                   | Esempio                                             |
| ------------------- | ----------------------- | --------------------------------------------------- |
| `gh release list`   | Elenca release          | `gh release list`                                   |
| `gh release create` | Crea release            | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Aggiungi file a release | `gh release upload v1.0.0 build.zip`                |
| `gh release view`   | Visualizza release      | `gh release view v1.0.0`                            |

---

## 📜 Gist

| Comando          | Scopo           | Esempio                   |
| ---------------- | --------------- | ------------------------- |
| `gh gist create` | Crea gist       | `gh gist create file.txt` |
| `gh gist list`   | Elenca gist     | `gh gist list`            |
| `gh gist view`   | Visualizza gist | `gh gist view abc123`     |
| `gh gist edit`   | Modifica gist   | `gh gist edit abc123`     |

---

## ⚙️ Workflow (GitHub Actions)

| Comando            | Scopo                   | Esempio                       |
| ------------------ | --------------------- | ----------------------------- |
| `gh workflow list` | Elenca workflow         | `gh workflow list`            |
| `gh workflow view` | Visualizza workflow     | `gh workflow view build.yml`  |
| `gh workflow run`  | Esegui workflow         | `gh workflow run build.yml`   |
| `gh run list`      | Elenca esecuzioni       | `gh run list`                 |
| `gh run watch`     | Osserva esecuzione      | `gh run watch 123456789`      |
