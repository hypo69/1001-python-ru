# GitHub CLI

## ¿Qué es GitHub CLI?

**GitHub CLI** (abreviado `gh`) es una herramienta de línea de comandos que le permite trabajar con GitHub directamente desde la terminal.
Con ella, puede administrar repositorios, issues, pull requests, lanzamientos y otras entidades sin necesidad de acceder a la interfaz web de GitHub.

CLI es conveniente para desarrolladores, ingenieros de DevOps y cualquiera que automatice el trabajo con GitHub o prefiera la terminal en lugar del navegador.

---

## Instalación

GitHub CLI es compatible con **Windows**, **macOS** y **Linux**.

* **Linux (Ubuntu/Debian):**

```bash
sudo apt install gh
```

* **macOS (a través de Homebrew):**

```bash
brew install gh
```

* **Windows (a través de Winget):**

```powershell
winget install --id GitHub.cli
```

Después de la instalación, compruebe la versión:

```bash
gh --version
```

---

## Autorización

Para acceder a repositorios y acciones privados, debe autorizar:

```bash
gh auth login
```

CLI ofrecerá:

* elegir GitHub.com o GitHub Enterprise
* método de autorización (navegador, token, SSH)
* guardar datos para ejecuciones posteriores

Puede verificar el estado con el comando:

```bash
gh auth status
```

---

## Características principales

### Trabajar con repositorios

Crear un nuevo repositorio:

```bash
gh repo create my-project
```

Clonación:

```bash
gh repo clone owner/repo
```

Ver información:

```bash
gh repo view owner/repo
```

---

### Issues

Crear un issue:

```bash
gh issue create --title "Bug: crash on startup" --body "Steps to reproduce..."
```

Lista de issues:

```bash
gh issue list
```

Ver un issue específico:

```bash
gh issue view 42
```

---

### Pull Requests

Crear un pull request:

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Added new functionality"
```

Ver:

```bash
gh pr list
gh pr view 123
```

Fusionar:

```bash
gh pr merge 123 --squash --delete-branch
```

---

### Acciones (CI/CD)

Ejecutar flujos de trabajo:

```bash
gh workflow run build.yml
```

Ver estado:

```bash
gh run list
```

---

## Comandos útiles

| Comando                         | Propósito                         |
| ------------------------------- | --------------------------------- |
| `gh help`                       | listar todos los comandos         |
| `gh alias set co "pr checkout"` | crear alias para comando rápido   |
| `gh gist create file.txt`       | subir archivo como gist           |
| `gh release create v1.0.0`      | crear lanzamiento                 |

---

## Ventajas de GitHub CLI

* Ahorro de tiempo: trabajar con GitHub sin navegador.
* Scripting: conveniente para automatizar en bash/PowerShell.
* Integración con CI/CD.
* Herramienta única para comandos y API de GitHub.

---

Excelente 🚀 Entonces hagamos una **lista de verificación "TOP-10 comandos de GitHub CLI para uso diario"**. Se puede usar como hoja de trucos.

---

# ✅ TOP-10 comandos de GitHub CLI para uso diario

## 1. Autorización

```bash
gh auth login
```

🔑 Autorizar en GitHub a través del navegador o token.
Útil para la configuración inicial o el cambio de cuenta.

---

## 2. Comprobar estado de autorización

```bash
gh auth status
```

📌 Comprueba si el CLI está conectado a GitHub y cómo.

---

## 3. Clonar repositorio

```bash
gh repo clone owner/repo
```

📥 Clonación rápida de repositorios sin buscar un enlace en la interfaz web.

---

## 4. Crear nuevo repositorio

```bash
gh repo create my-project
```

🆕 Crear repositorio directamente desde la terminal (local + en GitHub).

---

## 5. Ver información del repositorio

```bash
gh repo view --web
```

📖 Muestra la descripción y la configuración del repositorio.
La opción `--web` abre inmediatamente la página en el navegador.

---

## 6. Listar issues

```bash
gh issue list
```

📋 Conveniente para ver tareas y errores directamente en la terminal.

---

## 7. Crear issue

```bash
gh issue create --title "Bug: login failed" --body "Steps to reproduce..."
```

🐞 Crea una nueva tarea o informe de errores.

---

## 8. Crear Pull Request

```bash
gh pr create --base main --head feature-branch --title "New feature" --body "Description..."
```

🔀 Herramienta principal para el trabajo en equipo: abrir un Pull Request desde su rama.

---

## 9. Ver y comprobar PR

```bash
gh pr view 123
```

👀 Ver Pull Request con comentarios y estados de verificación.
Puede añadir `--web` para abrir en el navegador.

---

## 10. Fusionar PR con eliminación de rama

```bash
gh pr merge 123 --squash --delete-branch
```

✅ Fusionar Pull Request + eliminar rama en un solo paso.


---

# 📌 GitHub CLI — Hoja de trucos

## 🔑 Autorización y configuración

| Comando                         | Propósito                         | Ejemplo                         |
| ------------------------------- | --------------------------------- | ------------------------------- |
| `gh auth login`                 | Autorización (navegador, token, SSH) | `gh auth login`                 |
| `gh auth status`                | Comprobar conexión actual         | `gh auth status`                |
| `gh alias set co "pr checkout"` | Crear alias para comando rápido   | `gh alias set co "pr checkout"` |
| `gh config get`                 | Obtener configuración de CLI      | `gh config get editor`          |

---

## 📂 Repositorios

| Comando          | Propósito                              | Ejemplo                         |
| ---------------- | -------------------------------------- | ------------------------------- |
| `gh repo create` | Crear repositorio                      | `gh repo create my-project`     |
| `gh repo clone`  | Clonar repositorio                     | `gh repo clone hypo69/hypotez`  |
| `gh repo view`   | Información del repositorio (o abrir en web) | `gh repo view --web`            |
| `gh repo fork`   | Bifurcar repositorio                   | `gh repo fork owner/repo`       |

---

## 📝 Issues

| Comando           | Propósito        | Ejemplo                                           |
| ----------------- | -------------- | ------------------------------------------------- |
| `gh issue list`   | Listar tareas    | `gh issue list`                                   |
| `gh issue create` | Crear issue      | `gh issue create --title "Bug" --body "Steps..."` |
| `gh issue view`   | Ver issue        | `gh issue view 42`                                |
| `gh issue close`  | Cerrar issue     | `gh issue close 42`                               |

---

## 🔀 Pull Requests

| Comando          | Propósito                   | Ejemplo                                     |
| ---------------- | ------------------------- | ------------------------------------------- |
| `gh pr list`     | Listar PRs                  | `gh pr list`                                |
| `gh pr create`   | Crear PR                    | `gh pr create --base main --head feature-x` |
| `gh pr view`     | Ver PR                      | `gh pr view 123 --web`                      |
| `gh pr checkout` | Cambiar a rama de PR        | `gh pr checkout 123`                        |
| `gh pr merge`    | Fusionar PR                 | `gh pr merge 123 --squash --delete-branch`  |

---

## 📦 Lanzamientos

| Comando             | Propósito                 | Ejemplo                                            |
| ------------------- | ------------------------- | -------------------------------------------------- |
| `gh release list`   | Listar lanzamientos       | `gh release list`                                  |
| `gh release create` | Crear lanzamiento         | `gh release create v1.0.0 --notes "First release"` |
| `gh release upload` | Añadir archivo a lanzamiento | `gh release upload v1.0.0 build.zip`               |
| `gh release view`   | Ver lanzamiento           | `gh release view v1.0.0`                           |

---

## 📜 Gists

| Comando          | Propósito        | Ejemplo                   |
| ---------------- | ---------------- | ------------------------- |
| `gh gist create` | Crear gist       | `gh gist create file.txt` |
| `gh gist list`   | Listar gists     | `gh gist list`            |
| `gh gist view`   | Ver gist         | `gh gist view abc123`     |
| `gh gist edit`   | Editar gist      | `gh gist edit abc123`     |

---

## ⚙️ Flujos de trabajo (GitHub Actions)

| Comando            | Propósito           | Ejemplo                       |
| ------------------ | ------------------- | ----------------------------- |
| `gh workflow list` | Listar flujos de trabajo | `gh workflow list`            |
| `gh workflow view` | Ver flujo de trabajo | `gh workflow view build.yml`  |
| `gh workflow run`  | Ejecutar flujo de trabajo | `gh workflow run build.yml`   |
| `gh run list`      | Listar ejecuciones  | `gh run list`                 |
| `gh run watch`     | Observar ejecución  | `gh run watch 123456789`      |
