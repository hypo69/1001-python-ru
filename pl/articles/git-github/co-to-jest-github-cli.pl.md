# GitHub CLI

## Co to jest GitHub CLI?

**GitHub CLI** (w skrócie `gh`) to narzędzie wiersza poleceń, które umożliwia pracę z GitHubem bezpośrednio z terminala.
Za jego pomocą można zarządzać repozytoriami, problemami, żądaniami ściągnięcia, wydaniami i innymi encjami, bez wchodzenia do interfejsu internetowego GitHub.

CLI jest wygodne dla programistów, inżynierów DevOps i wszystkich, którzy automatyzują pracę z GitHubem lub preferują terminal zamiast przeglądarki.

---

## Instalacja

GitHub CLI jest obsługiwany w systemach **Windows**, **macOS** i **Linux**.

* **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

* **macOS (przez Homebrew):**

```bash
brew install gh
```

* **Windows (przez Winget):**

```powershell
winget install --id GitHub.cli
```

Po instalacji sprawdź wersję:

```bash
gh --version
```

---

## Autoryzacja

Aby uzyskać dostęp do prywatnych repozytoriów i akcji, musisz się autoryzować:

```bash
gh auth login
```

CLI zaoferuje:

* wybór GitHub.com lub GitHub Enterprise
* metodę autoryzacji (przeglądarka, token, SSH)
* zapisanie danych do kolejnych uruchomień

Możesz sprawdzić status za pomocą polecenia:

```bash
gh auth status
```

---

## Kluczowe funkcje

### Praca z repozytoriami

Tworzenie nowego repozytorium:

```bash
gh repo create my-project
```

Klonowanie:

```bash
gh repo clone owner/repo
```

Wyświetlanie informacji:

```bash
gh repo view owner/repo
```

---

### Problemy

Tworzenie problemu:

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

Lista problemów:

```bash
gh issue list
```

Wyświetlanie konkretnego problemu:

```bash
gh issue view 42
```

---

### Żądania ściągnięcia

Tworzenie żądania ściągnięcia:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Wyświetlanie:

```bash
gh pr list
gh pr view 123
```

Scalanie:

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Akcje (CI/CD)

Uruchamianie przepływów pracy:

```bash
gh workflow run build.yml
```

Wyświetlanie statusu:

```bash
gh run list
```

---

## Przydatne polecenia

| Polecenie                         | Cel                               |
| ------------------------------- | --------------------------------- |
| `gh help`                       | lista wszystkich poleceń          |
| `gh alias set co "pr checkout"` | utwórz alias dla szybkiego polecenia |
| `gh gist create file.txt`       | prześlij plik jako gist           |
| `gh release create v1.0.0`      | utwórz wydanie                    |

---

## Zalety GitHub CLI

* Oszczędność czasu: praca z GitHubem bez przeglądarki.
* Skryptowanie: wygodne do automatyzacji w bash/PowerShell.
* Integracja z CI/CD.
* Jedno narzędzie do poleceń i API GitHub.

---

Doskonale 🚀 W takim razie stwórzmy **listę kontrolną "TOP-10 poleceń GitHub CLI do codziennego użytku"**. Można jej używać jako ściągawki.

---

# ✅ TOP-10 poleceń GitHub CLI do codziennego użytku

## 1. Autoryzacja

```bash
gh auth login
```

🔑 Autoryzacja w GitHub przez przeglądarkę lub token.
Przydatne przy początkowej konfiguracji lub zmianie konta.

---

## 2. Sprawdź status autoryzacji

```bash
gh auth status
```

📌 Sprawdza, czy CLI jest połączone z GitHubem i w jaki sposób.

---

## 3. Klonowanie repozytorium

```bash
gh repo clone owner/repo
```

📥 Szybkie klonowanie repozytorium bez wyszukiwania linku w interfejsie internetowym.

---

## 4. Utwórz nowe repozytorium

```bash
gh repo create my-project
```

🆕 Utwórz repozytorium bezpośrednio z terminala (lokalnie + na GitHub).

---

## 5. Wyświetl informacje o repozytorium

```bash
gh repo view --web
```

📖 Wyświetla opis i ustawienia repozytorium.
Opcja `--web` natychmiast otwiera stronę w przeglądarce.

---

## 6. Lista problemów

```bash
gh issue list
```

📋 Wygodne do przeglądania zadań i błędów bezpośrednio w terminalu.

---

## 7. Utwórz problem

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Tworzy nowe zadanie lub raport o błędzie.

---

## 8. Utwórz żądanie ściągnięcia

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Główne narzędzie do pracy zespołowej: otwieranie żądania ściągnięcia z Twojej gałęzi.

---

## 9. Wyświetl i sprawdź żądanie ściągnięcia

```bash
gh pr view 123
```

👀 Wyświetl żądanie ściągnięcia z komentarzami i statusami sprawdzeń.
Możesz dodać `--web`, aby otworzyć w przeglądarce.

---

## 10. Scal żądanie ściągnięcia z usunięciem gałęzi

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Scal żądanie ściągnięcia + usuń gałąź w jednym kroku.


---

# 📌 GitHub CLI — Ściągawka

## 🔑 Autoryzacja i ustawienia

| Polecenie                         | Cel                               |
| ------------------------------- | --------------------------------- |
| `gh auth login`                 | Autoryzacja (przeglądarka, token, SSH) | `gh auth login`                 |
| `gh auth status`                | Sprawdź bieżące połączenie        | `gh auth status`                |
| `gh alias set co "pr checkout"` | Utwórz alias dla szybkiego polecenia | `gh alias set co "pr checkout"` |
| `gh config get`                 | Pobierz ustawienia CLI            | `gh config get editor`          |

---

## 📂 Repozytoria

| Polecenie          | Cel                                    | Przykład                        |
| ---------------- | -------------------------------------- | ------------------------------- |
| `gh repo create` | Utwórz repozytorium                    | `gh repo create my-project`     |
| `gh repo clone`  | Sklonuj repozytorium                   | `gh repo clone hypo69/hypotez`  |
| `gh repo view`   | Informacje o repozytorium (lub otwórz w sieci) | `gh repo view --web`            |
| `gh repo fork`   | Utwórz fork repozytorium               | `gh repo fork owner/repo`       |

---

## 📝 Problemy

| Polecenie           | Cel            | Przykład                                          |
| ----------------- | -------------- | ------------------------------------------------- |
| `gh issue list`   | Lista zadań    | `gh issue list`                                   |
| `gh issue create` | Utwórz problem | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Wyświetl problem | `gh issue view 42`                                |
| `gh issue close`  | Zamknij problem | `gh issue close 42`                               |

---

## 🔀 Żądania ściągnięcia

| Polecenie          | Cel                       | Przykład                                      |
| ---------------- | ------------------------- | ------------------------------------------- |
| `gh pr list`     | Lista żądań ściągnięcia   | `gh pr list`                                |
| `gh pr create`   | Utwórz żądanie ściągnięcia | `gh pr create --base main --head feature-x` |
| `gh pr view`     | Wyświetl żądanie ściągnięcia | `gh pr view 123 --web`                      |
| `gh pr checkout` | Przełącz na gałąź żądania ściągnięcia | `gh pr checkout 123`                        |
| `gh pr merge`    | Scal żądanie ściągnięcia | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Wydania

| Polecenie             | Cel                    | Przykład                                           |
| ------------------- | ---------------------- | -------------------------------------------------- |
| `gh release list`   | Lista wydań            | `gh release list`                                  |
| `gh release create` | Utwórz wydanie         | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Dodaj plik do wydania  | `gh release upload v1.0.0 build.zip`               |
| `gh release view`   | Wyświetl wydanie       | `gh release view v1.0.0`                           |

---

## 📜 Gisty

| Polecenie          | Cel            | Przykład                   |
| ---------------- | -------------- | -------------------------- |
| `gh gist create` | Utwórz gist    | `gh gist create file.txt`  |
| `gh gist list`   | Lista gistów   | `gh gist list`             |
| `gh gist view`   | Wyświetl gist  | `gh gist view abc123`      |
| `gh gist edit`   | Edytuj gist    | `gh gist edit abc123`      |

---

## ⚙️ Przepływy pracy (GitHub Actions)

| Polecenie            | Cel                   | Przykład                      |
| ------------------ | --------------------- | ----------------------------- |
| `gh workflow list` | Lista przepływów pracy | `gh workflow list`            |
| `gh workflow view` | Wyświetl przepływ pracy | `gh workflow view build.yml`  |
| `gh workflow run`  | Uruchom przepływ pracy | `gh workflow run build.yml`   |
| `gh run list`      | Lista uruchomień      | `gh run list`                 |
| `gh run watch`     | Obserwuj uruchomienie | `gh run watch 123456789`      |
