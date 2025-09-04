# GitHub CLI

## Qu'est-ce que GitHub CLI ?

**GitHub CLI** (en abrégé `gh`) est un outil en ligne de commande qui vous permet de travailler avec GitHub directement depuis le terminal.
Avec lui, vous pouvez gérer les dépôts, les issues, les pull requests, les releases et d'autres entités sans avoir à vous rendre sur l'interface web de GitHub.

CLI est pratique pour les développeurs, les ingénieurs DevOps et tous ceux qui automatisent le travail avec GitHub ou préfèrent le terminal au navigateur.

---

## Installation

GitHub CLI est pris en charge sur **Windows**, **macOS** et **Linux**.

* **Linux (Ubuntu/Debian) :**

```bash
sudo apt install gh
```

* **macOS (via Homebrew) :**

```bash
brew install gh
```

* **Windows (via Winget) :**

```powershell
winget install --id GitHub.cli
```

Après l'installation, vérifiez la version :

```bash
gh --version
```

---

## Autorisation

Pour accéder aux dépôts et actions privés, vous devez vous autoriser :

```bash
gh auth login
```

CLI proposera :

* choisir GitHub.com ou GitHub Enterprise
* méthode d'autorisation (navigateur, jeton, SSH)
* enregistrer les données pour les exécutions ultérieures

Vous pouvez vérifier le statut avec la commande :

```bash
gh auth status
```

---

## Fonctionnalités principales

### Travailler avec les dépôts

Création d'un nouveau dépôt :

```bash
gh repo create my-project
```

Clonage :

```bash
gh repo clone owner/repo
```

Affichage des informations :

```bash
gh repo view owner/repo
```

---

### Issues

Création d'une issue :

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

Liste des issues :

```bash
gh issue list
```

Affichage d'une issue spécifique :

```bash
gh issue view 42
```

---

### Pull Requests

Création d'une pull request :

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Affichage :

```bash
gh pr list
gh pr view 123
```

Fusion :

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Actions (CI/CD)

Exécution des workflows :

```bash
gh workflow run build.yml
```

Affichage du statut :

```bash
gh run list
```

---

## Commandes utiles

| Commande                         | Objectif                          |
| ------------------------------- | --------------------------------- |
| `gh help`                       | lister toutes les commandes       |
| `gh alias set co "pr checkout"` | créer un alias pour une commande rapide | 
| `gh gist create file.txt`       | télécharger un fichier en tant que gist | 
| `gh release create v1.0.0`      | créer une release                 |

---

## Avantages de GitHub CLI

* Gain de temps : travailler avec GitHub sans navigateur.
* Scripting : pratique pour automatiser en bash/PowerShell.
* Intégration avec CI/CD.
* Outil unique pour les commandes et l'API GitHub.

---

Excellent 🚀 Alors, créons une **liste de contrôle "TOP-10 des commandes GitHub CLI pour une utilisation quotidienne"**. Elle peut être utilisée comme aide-mémoire.

---

# ✅ TOP-10 des commandes GitHub CLI pour une utilisation quotidienne

## 1. Autorisation

```bash
gh auth login
```

🔑 Autorisation dans GitHub via le navigateur ou un jeton.
Utile pour la configuration initiale ou le changement de compte.

---

## 2. Vérifier le statut d'autorisation

```bash
gh auth status
```

📌 Vérifie si le CLI est connecté à GitHub et comment.

---

## 3. Cloner un dépôt

```bash
gh repo clone owner/repo
```

📥 Clonage rapide d'un dépôt sans rechercher le lien dans l'interface web.

---

## 4. Créer un nouveau dépôt

```bash
gh repo create my-project
```

🆕 Créer un dépôt directement depuis le terminal (local + sur GitHub).

---

## 5. Afficher les informations du dépôt

```bash
gh repo view --web
```

📖 Affiche la description et les paramètres du dépôt.
L'option `--web` ouvre immédiatement la page dans le navigateur.

---

## 6. Lister les issues

```bash
gh issue list
```

📋 Pratique pour afficher les tâches et les bugs directement dans le terminal.

---

## 7. Créer une issue

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Crée une nouvelle tâche ou un rapport de bug.

---

## 8. Créer une Pull Request

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Outil principal pour le travail d'équipe : ouvrir une Pull Request depuis votre branche.

---

## 9. Afficher et vérifier une PR

```bash
gh pr view 123
```

👀 Afficher une Pull Request avec les commentaires et les statuts de vérification.
Vous pouvez ajouter `--web` pour ouvrir dans le navigateur.

---

## 10. Fusionner une PR avec suppression de branche

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Fusionner une Pull Request + supprimer la branche en une seule étape.


---

# 📌 GitHub CLI — Aide-mémoire

## 🔑 Autorisation et paramètres

| Commande                         | Objectif                          | Exemple                         |
| ------------------------------- | --------------------------------- | ------------------------------- |
| `gh auth login`                 | Autorisation (navigateur, jeton, SSH) | `gh auth login`                 |
| `gh auth status`                | Vérifier la connexion actuelle    | `gh auth status`                |
| `gh alias set co "pr checkout"` | Créer un alias pour une commande rapide | `gh alias set co "pr checkout"` |
| `gh config get`                 | Obtenir les paramètres du CLI     | `gh config get editor`          |

---

## 📂 Dépôts

| Commande          | Objectif                                | Exemple                         |
| ---------------- | -------------------------------------- | ------------------------------- |
| `gh repo create` | Créer un dépôt                      | `gh repo create my-project`     |
| `gh repo clone`  | Cloner un dépôt                     | `gh repo clone hypo69/hypotez`  |
| `gh repo view`   | Infos sur le dépôt (ou ouvrir dans le web) | `gh repo view --web`            |
| `gh repo fork`   | Forker un dépôt                     | `gh repo fork owner/repo`       |

---

## 📝 Issues

| Commande           | Objectif         | Exemple                                           |
| ----------------- | ---------------- | ------------------------------------------------- |
| `gh issue list`   | Lister les tâches | `gh issue list`                                   |
| `gh issue create` | Créer une issue  | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Afficher une issue | `gh issue view 42`                                |
| `gh issue close`  | Fermer une issue | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Commande          | Objectif                   | Exemple                                     |
| ---------------- | ------------------------- | ------------------------------------------- |
| `gh pr list`     | Lister les PR             | `gh pr list`                                |
| `gh pr create`   | Créer une PR              | `gh pr create --base main --head feature-x` |
| `gh pr view`     | Afficher une PR           | `gh pr view 123 --web`                      |
| `gh pr checkout` | Basculer vers la branche de PR | `gh pr checkout 123`                        |
| `gh pr merge`    | Fusionner une PR          | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Releases

| Commande             | Objectif                 | Exemple                                            |
| ------------------- | ------------------------ | -------------------------------------------------- |
| `gh release list`   | Lister les releases      | `gh release list`                                  |
| `gh release create` | Créer une release        | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Ajouter un fichier à une release | `gh release upload v1.0.0 build.zip`               |
| `gh release view`   | Afficher une release     | `gh release view v1.0.0`                           |

---

## 📜 Gists

| Commande          | Objectif         | Exemple                    |
| ---------------- | ---------------- | -------------------------- |
| `gh gist create` | Créer un gist    | `gh gist create file.txt`  |
| `gh gist list`   | Lister les gists | `gh gist list`             |
| `gh gist view`   | Afficher un gist | `gh gist view abc123`      |
| `gh gist edit`   | Modifier un gist | `gh gist edit abc123`      |

---

## ⚙️ Workflows (GitHub Actions)

| Commande            | Objectif          | Exemple                       |
| ------------------ | ----------------- | ----------------------------- |
| `gh workflow list` | Lister les workflows | `gh workflow list`            |
| `gh workflow view` | Afficher un workflow | `gh workflow view build.yml`  |
| `gh workflow run`  | Exécuter un workflow | `gh workflow run build.yml`   |
| `gh run list`      | Lister les exécutions | `gh run list`                 |
| `gh run watch`     | Surveiller une exécution | `gh run watch 123456789`      |
