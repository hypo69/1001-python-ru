# GitHub CLI

## Co to jest GitHub CLI?

**GitHub CLI** (w skrócie `gh`) to narzędzie wiersza poleceń, które pozwala pracować z GitHubem bezpośrednio z terminala.
Dzięki niemu możesz zarządzać repozytoriami, problemami (issues), żądaniami ściągnięcia (pull requests), wydaniami (releases) i innymi encjami, bez wchodzenia do interfejsu webowego GitHub.

CLI jest wygodne dla programistów, inżynierów DevOps i wszystkich, którzy automatyzują pracę z GitHubem lub preferują terminal zamiast przeglądarki.

---

## Instalacja

GitHub CLI jest obsługiwany na **Windows**, **macOS** i **Linux**.

*   **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

*   **macOS (przez Homebrew):**

```bash
brew install gh
```

*   **Windows (przez Winget):**

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

CLI zaproponuje:

*   wybór GitHub.com lub GitHub Enterprise
*   metodę autoryzacji (przeglądarka, token, SSH)
*   zapisanie danych do kolejnych uruchomień

Status można sprawdzić poleceniem:

```bash
gh auth status
```

---

## Główne funkcje

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

### Issues

Tworzenie issue:

```bash
gh issue create --title "Błąd: awaria przy uruchomieniu" --body "Kroki do odtworzenia..."
```

Lista issues:

```bash
gh issue list
```

Wyświetlanie konkretnego issue:

```bash
gh issue view 42
```

---

### Pull Requests

Tworzenie pull request:

```bash
gh pr create --base main --head feature-branch --title "Nowa funkcja" --body "Dodano nową funkcjonalność"
```

Wyświetlanie:

```bash
gh pr list
gh pr view 123
```

Łączenie (merge):

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Actions (CI/CD)

Uruchamianie workflow:

```bash
gh workflow run build.yml
```

Wyświetlanie statusu:

```bash
gh run list
```

---

## Przydatne polecenia

| Polecenie                       | Przeznaczenie                     |
| :------------------------------ | :-------------------------------- |
| `gh help`                       | lista wszystkich poleceń          |
| `gh alias set co "pr checkout"` | tworzenie aliasu dla szybkiego polecenia |
| `gh gist create file.txt`       | przesyłanie pliku jako gist       |
| `gh release create v1.0.0`      | tworzenie wydania                 |

---

## Zalety GitHub CLI

*   Oszczędność czasu: praca z GitHubem bez przeglądarki.
*   Skryptowanie: wygodne do automatyzacji w bash/PowerShell.
*   Integracja z CI/CD.
*   Jedno narzędzie do poleceń i API GitHub.

---

Świetnie 🚀 W takim razie stwórzmy **listę kontrolną "TOP-10 poleceń GitHub CLI do codziennego użytku"**. Można jej używać jako ściągawki.

---

# ✅ TOP-10 poleceń GitHub CLI do codziennego użytku

## 1. Autoryzacja

```bash
gh auth login
```

🔑 Autoryzacja w GitHub przez przeglądarkę lub token.
Przydatne przy pierwszej konfiguracji lub zmianie konta.

---

## 2. Sprawdzenie statusu autoryzacji

```bash
gh auth status
```

📌 Sprawdza, czy CLI jest połączone z GitHubem i w jaki sposób.

---

## 3. Klonowanie repozytorium

```bash
gh repo clone owner/repo
```

📥 Szybkie klonowanie repozytorium bez wyszukiwania linku w interfejsie webowym.

---

## 4. Tworzenie nowego repozytorium

```bash
gh repo create my-project
```

🆕 Tworzenie repozytorium bezpośrednio z terminala (lokalnie + na GitHubie).

---

## 5. Wyświetlanie informacji o repozytorium

```bash
gh repo view --web
```

📖 Pokazuje opis i ustawienia repozytorium.
Opcja `--web` natychmiast otwiera stronę w przeglądarce.

---

## 6. Lista issues

```bash
gh issue list
```

📋 Wygodne do przeglądania zadań i błędów bezpośrednio w terminalu.

---

## 7. Tworzenie issue

```bash
gh issue create --title "Błąd: logowanie nie powiodło się" --body "Kroki do odtworzenia..."
```

🐞 Tworzy nowe zadanie lub raport o błędzie.

---

## 8. Tworzenie Pull Request

```bash
gh pr create --base main --head feature-branch --title "Nowa funkcja" --body "Opis..."
```

🔀 Główne narzędzie pracy zespołowej: otwieranie Pull Requesta z własnej gałęzi.

---

## 9. Wyświetlanie i sprawdzanie PR

```bash
gh pr view 123
```

👀 Wyświetlanie Pull Requesta z komentarzami i statusami sprawdzeń.
Można dodać `--web`, aby otworzyć w przeglądarce.

---

## 10. Łączenie PR z usunięciem gałęzi

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Łączenie Pull Requesta + usuwanie gałęzi w jednym kroku.


---

# 📌 GitHub CLI — Ściągawka

## 🔑 Autoryzacja i ustawienia

| Polecenie                       | Przeznaczenie                     | Przykład                        |
| :------------------------------ | :-------------------------------- | :------------------------------ |
| `gh auth login`                 | Autoryzacja (przeglądarka, token, SSH) | `gh auth login`                 |
| `gh auth status`                | Sprawdzenie bieżącego połączenia  | `gh auth status`                |
| `gh alias set co "pr checkout"` | Tworzenie aliasu dla polecenia    | `gh alias set co "pr checkout"` |
| `gh config get`                 | Pobieranie ustawień CLI           | `gh config get editor`          |

---

## 📂 Repozytoria

| Polecenie        | Przeznaczenie                           | Przykład                       |
| :--------------- | :-------------------------------------- | :----------------------------- |
| `gh repo create` | Tworzenie repozytorium                  | `gh repo create my-project`    |
| `gh repo clone`  | Klonowanie repozytorium                 | `gh repo clone hypo69/hypotez` |
| `gh repo view`   | Informacje o repozytorium (lub otwarcie w web) | `gh repo view --web`           |
| `gh repo fork`   | Tworzenie forka repozytorium            | `gh repo fork owner/repo`      |

---

## 📝 Issues

| Polecenie         | Przeznaczenie    | Przykład                                          |
| :---------------- | :--------------- | :------------------------------------------------ |
| `gh issue list`   | Lista zadań      | `gh issue list`                                   |
| `gh issue create` | Tworzenie issue  | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Wyświetlanie issue | `gh issue view 42`                                |
| `gh issue close`  | Zamykanie issue  | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Polecenie        | Przeznaczenie            | Przykład                                    |
| :--------------- | :----------------------- | :------------------------------------------ |
| `gh pr list`     | Lista PR                 | `gh pr list`                                |
| `gh pr create`   | Tworzenie PR             | `gh pr create --base main --head feature-x` |
| `gh pr view`     | Wyświetlanie PR          | `gh pr view 123 --web`                      |
| `gh pr checkout` | Przełączanie na gałąź PR | `gh pr checkout 123`                        |
| `gh pr merge`    | Łączenie PR              | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Releases

| Polecenie          | Przeznaczenie           | Przykład                                           |
| :----------------- | :---------------------- | :------------------------------------------------- |
| `gh release list`  | Lista wydań             | `gh release list`                                  |
| `gh release create`| Tworzenie wydania       | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload`| Dodawanie pliku do wydania | `gh release upload v1.0.0 build.zip`               |
| `gh release view`  | Wyświetlanie wydania    | `gh release view v1.0.0`                           |

---

## 📜 Gisty

| Polecenie        | Przeznaczenie    | Przykład                  |
| :--------------- | :--------------- | :------------------------ |
| `gh gist create` | Tworzenie gista  | `gh gist create file.txt` |
| `gh gist list`   | Lista gistów     | `gh gist list`            |
| `gh gist view`   | Wyświetlanie gista | `gh gist view abc123`     |
| `gh gist edit`   | Edycja gista     | `gh gist edit abc123`     |

---

## ⚙️ Workflows (GitHub Actions)

| Polecenie         | Przeznaczenie      | Przykład                      |
| :---------------- | :----------------- | :---------------------------- |
| `gh workflow list`| Lista workflow     | `gh workflow list`            |
| `gh workflow view`| Wyświetlanie workflow | `gh workflow view build.yml`  |
| `gh workflow run` | Uruchamianie workflow | `gh workflow run build.yml`   |
| `gh run list`     | Lista uruchomień   | `gh run list`                 |
| `gh run watch`    | Obserwowanie uruchomienia | `gh run watch 123456789`      |
