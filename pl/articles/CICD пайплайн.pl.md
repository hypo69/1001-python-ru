🚀 **CI/CD: Od podstaw do produkcji w GCP z GitHub Actions – Kompletny przewodnik z przykładami** 🚀

Witajcie, deweloperzy! W tym artykule opowiem o CI/CD – koncepcji.

### Czym jest potok CI/CD w kontekście programowania?

**Potok CI/CD (Continuous Integration / Continuous Delivery lub Continuous Deployment)** to zautomatyzowany proces, który pozwala deweloperom szybko i niezawodnie dostarczać zmiany w kodzie do środowiska produkcyjnego.

Rozłóżmy kluczowe pojęcia:

🔧 **CI — Continuous Integration (Ciągła Integracja)**
Jest to praktyka, w której deweloperzy często wprowadzają zmiany do wspólnej bazy kodu. Każda taka zmiana automatycznie:
*   **Jest budowana** (build)
*   **Jest testowana** (testy jednostkowe, testy integracyjne)
*   **Jest sprawdzana pod kątem zgodności ze standardami** (linting, analiza statyczna)

👉 **Cel CI:** Wykrywanie błędów na najwcześniejszym etapie, zanim zepsują coś ważnego lub trafią do wydania.

🚀 **CD — Continuous Delivery (Ciągłe Dostarczanie) lub Continuous Deployment (Ciągłe Wdrażanie)**
Tutaj są dwie opcje:

✅ **Continuous Delivery (Ciągłe Dostarczanie)**
Po pomyślnym przejściu etapu CI, zmiany automatycznie:
*   Przechodzą dodatkowe testy (np. E2E – testy end-to-end)
*   Trafiają na serwer stagingowy (testowy)
👉 **Ale wdrożenie na produkcję nadal wymaga ręcznego potwierdzenia.** Daje to zespołowi kontrolę nad tym, *kiedy* dokładnie użytkownicy zobaczą zmiany.

🤖 **Continuous Deployment (Ciągłe Wdrażanie)**
Jest to kolejny krok po Continuous Delivery. Tutaj wdrożenie na produkcję odbywa się **całkowicie automatycznie**, jeśli wszystkie poprzednie etapy potoku (kompilacja, wszystkie testy) zakończyły się pomyślnie. Jest to najbardziej zaawansowany poziom automatyzacji.

### 🔄 Z czego zazwyczaj składa się potok CI/CD?

Typowy potok obejmuje następujące etapy:
1.  **Checkout** — Klonowanie najnowszej wersji kodu z repozytorium.
2.  **Build** — Budowanie projektu (kompilacja, montaż artefaktów, obrazów Docker).
3.  **Test** — Uruchamianie różnych rodzajów testów (jednostkowych, integracyjnych, E2E).
4.  **Lint/Code Quality** — Sprawdzanie kodu pod kątem zgodności stylu i potencjalnych błędów za pomocą analizatorów statycznych.
5.  **Deploy** — Wdrażanie aplikacji (na serwer stagingowy lub produkcyjny).
6.  **Notify** — Wysyłanie powiadomień o statusie potoku do zespołu (np. w Slacku, e-mailu).

### 🛠 Popularne narzędzia do CI/CD:

*   **GitHub Actions** (nasz dzisiejszy fokus!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 Dlaczego w ogóle potrzebujemy CI/CD?

*   **Zmniejsza czynnik ludzki:** Automatyzacja eliminuje błędy związane z ręcznymi operacjami.
*   **Szybkie wykrywanie błędów:** Błędy są znajdowane wcześniej, co sprawia, że są łatwiejsze i tańsze w naprawie.
*   **Automatyzacja rutynowych zadań:** Deweloperzy spędzają mniej czasu na budowaniu i wdrażaniu, a więcej – na kodzie.
*   **Poprawa jakości kodu:** Ciągłe sprawdzanie i testowanie podnosi ogólny poziom jakości.
*   **Szybkie dostarczanie funkcji użytkownikom:** Nowe funkcje docierają do użytkownika końcowego szybciej i częściej.

### 📦 Proste przykłady CI/CD z GitHub Actions

Przyjrzyjmy się podstawowym potokom dla popularnych technologii. Wszystkie przykłady używają GitHub Actions i są zapisywane w katalogu `.github/workflows/` Twojego projektu.

#### 🐍 CI/CD dla Pythona (z `pytest` i `flake8`)

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
          python-version: '3.11' # Określ swoją wersję

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Upewnij się, że masz requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Sprawdź kod w folderach src i tests (dostosuj do swojego projektu)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD dla Node.js (z `npm test` i `eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # Określ swoją wersję Node.js

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # lub npm ci dla bardziej przewidywalnej instalacji

      - name: Lint with ESLint
        run: npx eslint . # Upewnij się, że ESLint jest skonfigurowany w projekcie

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD dla Docker (budowanie i push do Docker Hub)

Do tego przykładu potrzebne będą sekrety `DOCKER_USERNAME` i `DOCKER_PASSWORD` (lub token) w ustawieniach repozytorium GitHub (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # Uruchom tylko dla gałęzi main

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # Zastąp myapp nazwą swojej aplikacji
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Wdrażanie na popularne platformy

Teraz, gdy mamy zbudowane i przetestowane artefakty (np. obraz Docker), zobaczmy, jak można je wdrożyć.

#### 🟣 Wdrażanie na Heroku

**🔐 Sekrety GitHub:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

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
          git push heroku main -f # Zachowaj ostrożność z -f (force push)
```
Jeśli wdrażasz obraz Docker na Heroku:
```yaml
# ... (kroki budowania i logowania do Docker Hub/GHCR z poprzednich przykładów) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # Zależy od zadania budowania obrazu
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # Zakładając, że obraz jest zbudowany jako ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 Wdrażanie na AWS (np. statyczne do S3)

**🔐 Sekrety GitHub:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

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
        # Zastąp ./public ścieżką do swoich plików statycznych
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Do wdrożenia na **AWS Elastic Beanstalk** zazwyczaj używa się EB CLI, potok będzie podobny, ale z poleceniami `eb deploy`.

#### 🔵 Wdrażanie na Google Cloud Platform (GCP App Engine)

**🔐 Sekrety GitHub:** `GCP_CREDENTIALS` (klucz JSON konta serwisowego), `GCP_PROJECT_ID`.

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
        # Upewnij się, że masz app.yaml w katalogu głównym projektu
        run: gcloud app deploy --quiet
```

#### 🟪 Wdrażanie na Render.com

Render często automatycznie wdraża po pushu do GitHub, jeśli repozytorium jest połączone. Ale dla ręcznego wyzwalacza (lub jako część bardziej złożonego potoku) można użyć Deploy Hook.
**🔐 Sekrety GitHub:** `RENDER_DEPLOY_HOOK` (URL uzyskany z ustawień usługi w Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Ręczne uruchamianie z UI GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 Zaawansowane CI/CD: Budowanie Docker → Push do GHCR → Staging/Produkcja w GCP Cloud Run

A teraz wisienka na torcie! Zbudujmy zaawansowany potok:
1.  Budowanie obrazu Docker.
2.  Publikowanie obrazu w GitHub Container Registry (ghcr.io).
3.  Automatyczne wdrożenie w środowisku **stagingowym** w GCP Cloud Run.
4.  Wdrożenie w środowisku **produkcyjnym** w GCP Cloud Run **po ręcznym potwierdzeniu**.

Do tego potrzebne będą nam pliki workflow.

**Wymagane sekrety GitHub:**
*   `GCP_PROJECT_ID`: ID Twojego projektu w GCP.
*   `GCP_CREDENTIALS`: Klucz JSON konta serwisowego GCP z uprawnieniami do wdrażania w Cloud Run i dostępu do GHCR (jeśli potrzebne). Zazwyczaj `GITHUB_TOKEN` wystarcza do dostępu do GHCR z Actions.
*   `GCP_REGION`: Region dla Cloud Run (np. `europe-west1`).

#### 1. Budowanie i publikowanie obrazu Docker w GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # Uruchom po pushu do main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # Do checkout
      packages: write     # Do pushu do GHCR

    steps:
      - uses: actions/checkout@v3

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build Docker image
        # Zastąp myapp nazwą swojej aplikacji
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
</code></pre>
*   `github.repository_owner`: Właściciel repozytorium (Twoja nazwa użytkownika lub organizacji).
*   `github.event.repository.name`: Nazwa repozytorium.
*   `myapp`: Nazwa Twojej aplikacji/obrazu.

#### 2. Automatyczne wdrożenie do Staging (GCP Cloud Run)

Ten workflow zostanie uruchomiony automatycznie po pomyślnym zakończeniu `build.yml`.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # Nazwa workflow budowania
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Uruchom tylko, jeśli workflow budowania zakończył się pomyślnie
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Użyj środowisk GitHub dla staging (opcjonalnie, ale dobra praktyka)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # URL będzie dostępny po wdrożeniu

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
          service: 'myapp-staging' # Nazwa Twojej usługi stagingowej w Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # Użyj obrazu, który został wypchnięty w build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Zezwól na nieautoryzowany dostęp dla przykładu
</code></pre>
<h4>3. Wdrażanie na produkcję z ręcznym potwierdzeniem (GCP Cloud Run)</h4>
<p>Ten workflow jest uruchamiany ręcznie za pośrednictwem interfejsu użytkownika GitHub Actions.</p>
<pre class="line-numbers"><code class="language-yaml">
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Pozwala na ręczne uruchomienie

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
          service: 'myapp-production' # Nazwa Twojej usługi produkcyjnej
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Użyj tego samego obrazu 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Dla produkcji możesz dodać --no-traffic, a następnie stopniowo przełączać ruch
          # traffic:
          #   latest: true
          #   percent: 100
</code></pre>
<p>**Ważne punkty tego zaawansowanego potoku:**</p>
<li>**GitHub Container Registry (ghcr.io):** Używamy go do przechowywania obrazów Docker. Jest to wygodne, ponieważ jest ściśle zintegrowane z GitHub Actions.</li>
<li>**`workflow_run`:** Pozwala na uruchomienie jednego workflow (wdrożenie stagingowe) po zakończeniu drugiego (budowanie).</li>
<li>**`workflow_dispatch`:** Daje możliwość ręcznego uruchomienia workflow (wdrożenie produkcyjne), co zapewnia kontrolę.</li>
<li>**Środowiska GitHub:** Pozwalają na konfigurację reguł ochrony dla produkcji (np. wymaganie zatwierdzenia od określonych recenzentów) i przechowywanie sekretów specyficznych dla środowiska.</li>
<li>**GCP Cloud Run:** Doskonała opcja serverless do uruchamiania aplikacji kontenerowych.</li>
<h3>🔐 Bezpieczeństwo – to ważne!</h3>
<li>**Używaj sekretów GitHub:** Nigdy nie przechowuj tokenów, haseł, kluczy API bezpośrednio w plikach YAML. Użyj `Settings -> Secrets and variables -> Actions` w swoim repozytorium.</li>
<li>**Minimalne uprawnienia:** Dla kont serwisowych (np. GCP) przyznawaj tylko te uprawnienia, które są naprawdę niezbędne do wykonywania zadań CI/CD.</li>
<li>**Izoluj środowiska:** Staging i Produkcja powinny być jak najbardziej izolowane. Różne projekty/konta u dostawców chmury to dobra praktyka.</li>
<li>**Ochrona gałęzi:** Skonfiguruj ochronę dla gałęzi `main` (lub `master`), aby pushowanie do niej było możliwe tylko poprzez Pull Request z obowiązkowymi kontrolami CI.</li>
