🚀 **CI/CD: Von den Grundlagen bis zur Produktion auf GCP mit GitHub Actions – Ein vollständiger Leitfaden mit Beispielen** 🚀

Hallo, Entwickler! In diesem Artikel werde ich über CI/CD sprechen – ein Konzept.

### Was ist eine CI/CD-Pipeline im Kontext der Programmierung?

**Eine CI/CD-Pipeline (Continuous Integration / Continuous Delivery oder Continuous Deployment)** ist ein automatisierter Prozess, der es Entwicklern ermöglicht, Codeänderungen schnell und zuverlässig in eine Produktionsumgebung zu liefern.

Lassen Sie uns die Schlüsselkonzepte aufschlüsseln:

🔧 **CI — Continuous Integration (Kontinuierliche Integration)**
Dies ist eine Praxis, bei der Entwickler häufig Änderungen in eine gemeinsame Codebasis integrieren. Jede solche Änderung wird automatisch:
*   **Gebaut** (build)
*   **Getestet** (Unit-Tests, Integrationstests)
*   **Auf Einhaltung von Standards überprüft** (Linting, statische Analyse)

👉 **Ziel von CI:** Fehler so früh wie möglich zu identifizieren, bevor sie etwas Wichtiges kaputt machen oder in ein Release gelangen.

🚀 **CD — Continuous Delivery (Kontinuierliche Bereitstellung) oder Continuous Deployment (Kontinuierliche Auslieferung)**
Hier gibt es zwei Optionen:

✅ **Continuous Delivery (Kontinuierliche Bereitstellung)**
Nach erfolgreichem Abschluss der CI-Phase werden Änderungen automatisch:
*   Zusätzlichen Tests unterzogen (z. B. E2E – End-to-End-Tests)
*   Auf einem Staging-Server (Testserver) bereitgestellt

👉 **Aber die Bereitstellung in die Produktion erfordert immer noch eine manuelle Bestätigung.** Dies gibt dem Team die Kontrolle darüber, *wann* genau die Benutzer die Änderungen sehen.

🤖 **Continuous Deployment (Kontinuierliche Auslieferung)**
Dies ist der nächste Schritt nach Continuous Delivery. Hier erfolgt die Bereitstellung in die Produktion **vollautomatisch**, wenn alle vorherigen Phasen der Pipeline (Build, alle Tests) erfolgreich waren. Dies ist die fortschrittlichste Stufe der Automatisierung.

### 🔄 Woraus besteht eine CI/CD-Pipeline normalerweise?

Eine typische Pipeline umfasst die folgenden Phasen:
1.  **Checkout** — Klonen der neuesten Codeversion aus dem Repository.
2.  **Build** — Erstellen des Projekts (Kompilierung, Erstellung von Artefakten, Docker-Images).
3.  **Test** — Ausführen verschiedener Arten von Tests (Unit-, Integrations-, E2E).
4.  **Lint/Code Quality** — Überprüfung des Codes auf Stilkonformität und potenzielle Fehler mithilfe statischer Analysetools.
5.  **Deploy** — Bereitstellen der Anwendung (auf einem Staging- oder Produktionsserver).
6.  **Notify** — Senden von Benachrichtigungen über den Pipeline-Status an das Team (z. B. in Slack, E-Mail).

### 🛠 Beliebte Tools für CI/CD:

*   **GitHub Actions** (unser heutiger Fokus!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 Warum brauchen wir CI/CD überhaupt?

*   **Reduziert menschliche Fehler:** Automatisierung eliminiert Fehler, die mit manuellen Operationen verbunden sind.
*   **Schnelle Fehlererkennung:** Fehler werden früher gefunden, was ihre Behebung einfacher und kostengünstiger macht.
*   **Automatisierung von Routineaufgaben:** Entwickler verbringen weniger Zeit mit dem Bauen und Bereitstellen und mehr Zeit mit dem Codieren.
*   **Verbesserung der Codequalität:** Kontinuierliche Überprüfungen und Tests erhöhen den allgemeinen Qualitätsstandard.
*   **Schnelle Bereitstellung von Funktionen für Benutzer:** Neue Funktionen erreichen den Endbenutzer schneller und häufiger.

### 📦 Einfache CI/CD-Beispiele mit GitHub Actions

Schauen wir uns grundlegende Pipelines für beliebte Technologien an. Alle Beispiele verwenden GitHub Actions und werden im Verzeichnis `.github/workflows/` Ihres Projekts gespeichert.

#### 🐍 CI/CD für Python (mit `pytest` und `flake8`)

```yaml
# .github/workflows/python-ci.yml
name: Python CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11' # Geben Sie Ihre Version an

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Stellen Sie sicher, dass Sie requirements.txt haben
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Überprüfen Sie den Code in den Ordnern src und tests (passen Sie ihn an Ihr Projekt an)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD für Node.js (mit `npm test` und `eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # Geben Sie Ihre Node.js-Version an

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # oder npm ci für eine vorhersehbarere Installation

      - name: Lint with ESLint
        run: npx eslint . # Stellen Sie sicher, dass ESLint im Projekt konfiguriert ist

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD für Docker (Build und Push zu Docker Hub)

Für dieses Beispiel benötigen Sie die Geheimnisse `DOCKER_USERNAME` und `DOCKER_PASSWORD` (oder ein Token) in den Einstellungen Ihres GitHub-Repositorys (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # Nur für den main-Branch ausführen

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # Ersetzen Sie myapp durch den Namen Ihrer Anwendung
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Bereitstellung auf beliebten Plattformen

Nachdem wir nun gebaute und getestete Artefakte (z. B. ein Docker-Image) haben, schauen wir uns an, wie sie bereitgestellt werden können.

#### 🟣 Bereitstellung auf Heroku

**🔐 GitHub-Geheimnisse:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

```yaml
# .github/workflows/deploy-heroku.yml
name: Deploy to Heroku

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Heroku CLI
        run: curl https://cli-assets.heroku.com/install.sh | sh
      - name: Login to Heroku
        env:
          HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
        run: heroku auth:token
      - name: Deploy to Heroku
        env:
          HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
        run: |
          heroku git:remote -a ${{ secrets.HEROKU_APP_NAME }}
          git push heroku main -f # Seien Sie vorsichtig mit -f (force push)
```
Wenn Sie ein Docker-Image auf Heroku bereitstellen:
```yaml
# ... (Build- und Login-Schritte für Docker Hub/GHCR aus früheren Beispielen) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # Abhängig vom Build-Job des Images
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # Angenommen, das Image wird als ghcr.io/username/repo/myapp:latest gebaut
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 Bereitstellung auf AWS (z. B. statische Dateien in S3)

**🔐 GitHub-Geheimnisse:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

```yaml
# .github/workflows/deploy-aws-s3.yml
name: Deploy Static Site to AWS S3

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}
      - name: Sync files to S3
        # Ersetzen Sie ./public durch den Pfad zu Ihren statischen Dateien
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Für die Bereitstellung auf **AWS Elastic Beanstalk** wird normalerweise die EB CLI verwendet, die Pipeline ist ähnlich, aber mit `eb deploy`-Befehlen.

#### 🔵 Bereitstellung auf Google Cloud Platform (GCP App Engine)

**🔐 GitHub-Geheimnisse:** `GCP_CREDENTIALS` (JSON-Schlüssel des Dienstkontos), `GCP_PROJECT_ID`..

```yaml
# .github/workflows/deploy-gcp-app-engine.yml
name: Deploy to GCP App Engine

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2
        with:
          project_id: ${{ secrets.GCP_PROJECT_ID }}
          service_account_key: ${{ secrets.GCP_CREDENTIALS }}
          export_default_credentials: true
      - name: Deploy to App Engine
        # Stellen Sie sicher, dass Sie app.yaml im Stammverzeichnis des Projekts haben
        run: gcloud app deploy --quiet
```

#### 🟪 Bereitstellung auf Render.com

Render stellt oft automatisch bei einem Push zu GitHub bereit, wenn das Repository verbunden ist. Aber für einen manuellen Trigger (oder als Teil einer komplexeren Pipeline) kann ein Deploy Hook verwendet werden.
**🔐 GitHub-Geheimnisse:** `RENDER_DEPLOY_HOOK` (URL, die aus den Render-Diensteinstellungen abgerufen wird).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Manueller Start über die GitHub-UI

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 Fortgeschrittenes CI/CD: Docker bauen → Push zu GHCR → Staging/Production auf GCP Cloud Run

Und jetzt das Sahnehäubchen! Lassen Sie uns eine fortgeschrittene Pipeline zusammenstellen:
1.  Build des Docker-Images.
2.  Veröffentlichung des Images im GitHub Container Registry (ghcr.io).
3.  Automatische Bereitstellung in die **Staging**-Umgebung auf GCP Cloud Run.
4.  Bereitstellung in die **Produktions**-Umgebung auf GCP Cloud Run **nach manueller Bestätigung**.

Dafür benötigen wir mehrere Workflow-Dateien.

**Erforderliche GitHub-Geheimnisse:**
*   `GCP_PROJECT_ID`: ID Ihres GCP-Projekts.
*   `GCP_CREDENTIALS`: JSON-Schlüssel des GCP-Dienstkontos mit Berechtigungen zur Bereitstellung in Cloud Run und Zugriff auf GHCR (falls erforderlich). Normalerweise reicht `GITHUB_TOKEN` für den Zugriff auf GHCR von Actions aus.
*   `GCP_REGION`: Region für Cloud Run (z. B. `europe-west1`).

#### 1. Build und Veröffentlichung des Docker-Images in GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # Bei Push zu main ausführen

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # Für Checkout
      packages: write     # Für Push zu GHCR

    steps:
      - uses: actions/checkout@v3

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          # Sie können eine Tagging nach Commit-SHA für Einzigartigkeit hinzufügen:
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner`: Besitzer des Repositorys (Ihr Benutzername oder Ihre Organisation).
*   `github.event.repository.name`: Name des Repositorys.
*   `myapp`: Name Ihrer Anwendung/Ihres Images.

#### 2. Automatische Bereitstellung in Staging (GCP Cloud Run)

Dieser Workflow wird automatisch nach erfolgreichem Abschluss von `build.yml` ausgeführt.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"]
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }}

    steps:
      - uses: actions/checkout@v3

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging'
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
```

#### 3. Bereitstellung in Produktion mit manueller Bestätigung (GCP Cloud Run)

Dieser Workflow wird manuell über die GitHub Actions-Benutzeroberfläche ausgelöst.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Ermöglicht manuellen Start

jobs:
  deploy-production:
    runs-on: ubuntu-latest

    environment:
      name: production
      url: ${{ steps.deploy.outputs.url }}

    steps:
      - uses: actions/checkout@v3

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Production)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-production'
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Für die Produktion können Sie --no-traffic hinzufügen und dann den Traffic schrittweise umschalten
          # traffic:
          #   latest: true
          #   percent: 100
```

**Wichtige Punkte dieser fortgeschrittenen Pipeline:**
*   **GitHub Container Registry (ghcr.io):** Wir verwenden es zum Speichern von Docker-Images. Dies ist praktisch, da es eng in GitHub Actions integriert ist.
*   **`workflow_run`:** Ermöglicht das Ausführen eines Workflows (Staging-Bereitstellung) nach Abschluss eines anderen (Build).
*   **`workflow_dispatch`:** Bietet die Möglichkeit, einen Workflow (Produktionsbereitstellung) manuell auszulösen, was die Kontrolle gewährleistet.
*   **GitHub Environments:** Ermöglichen es Ihnen, Schutzregeln für die Produktion zu konfigurieren (z. B. die Genehmigung durch bestimmte Prüfer zu verlangen) und umgebungsspezifische Geheimnisse zu speichern.
*   **GCP Cloud Run:** Eine ausgezeichnete Serverless-Option zum Ausführen von containerisierten Anwendungen.

### 🔐 Sicherheit – das ist wichtig!

*   **Verwenden Sie GitHub Secrets:** Speichern Sie niemals Token, Passwörter, API-Schlüssel direkt in YAML-Dateien. Verwenden Sie `Settings -> Secrets and variables -> Actions` in Ihrem Repository.
*   **Minimale Berechtigungen:** Gewähren Sie Dienstkonten (z. B. GCP) nur die Berechtigungen, die für die Ausführung von CI/CD-Aufgaben unbedingt erforderlich sind.
*   **Umgebungen isolieren:** Staging und Produktion sollten so weit wie möglich isoliert sein. Unterschiedliche Projekte/Konten bei Cloud-Anbietern sind eine gute Praxis.
*   **Branch-Schutz:** Konfigurieren Sie den Schutz für den `main`- (oder `master`)-Branch, sodass Pushs nur über Pull Requests mit obligatorischen CI-Prüfungen möglich sind.
