🚀 **CI/CD: Dalle basi alla produzione su GCP con GitHub Actions – Una guida completa con esempi** 🚀

Ciao, sviluppatori! In questo articolo parlerò di CI/CD – il concetto.

### Cos'è una pipeline CI/CD nel contesto della programmazione?

Una **pipeline CI/CD (Continuous Integration / Continuous Delivery o Continuous Deployment)** è un processo automatizzato che consente agli sviluppatori di consegnare rapidamente e in modo affidabile le modifiche al codice in un ambiente di lavoro (produzione).

Analizziamo i concetti chiave:

🔧 **CI — Continuous Integration (Integrazione Continua)**
Questa è una pratica in cui gli sviluppatori apportano frequentemente modifiche a una codebase condivisa. Ogni modifica di questo tipo automaticamente:
*   **Viene costruita** (build)
*   **Viene testata** (test unitari, test di integrazione)
*   **Viene verificata la conformità agli standard** (linting, analisi statica)

👉 **Obiettivo della CI:** Identificare gli errori nella fase più precoce, prima che danneggino qualcosa di importante o finiscano in una release.

🚀 **CD — Continuous Delivery (Consegna Continua) o Continuous Deployment (Distribuzione Continua)**
Qui ci sono due opzioni:

✅ **Continuous Delivery (Consegna Continua)**
Dopo aver completato con successo la fase di CI, le modifiche automaticamente:
*   Superano test aggiuntivi (ad esempio, E2E – test end-to-end)
*   Vanno su un server di staging (test)
👉 **Ma la distribuzione in produzione richiede ancora una conferma manuale.** Questo dà al team il controllo su *quando* esattamente gli utenti vedranno le modifiche.

🤖 **Continuous Deployment (Distribuzione Continua)**
Questo è il passo successivo dopo la Continuous Delivery. Qui la distribuzione in produzione avviene **in modo completamente automatico**, se tutte le fasi precedenti della pipeline (build, tutti i test) sono state completate con successo. Questo è il livello più avanzato di automazione.

### 🔄 Di cosa è composta di solito una pipeline CI/CD?

Una pipeline tipica include le seguenti fasi:
1.  **Checkout** — Clonazione dell'ultima versione del codice dal repository.
2.  **Build** — Costruzione del progetto (compilazione, assemblaggio di artefatti, immagini Docker).
3.  **Test** — Esecuzione di vari tipi di test (unitari, di integrazione, E2E).
4.  **Lint/Code Quality** — Verifica del codice per la conformità dello stile e potenziali errori utilizzando analizzatori statici.
5.  **Deploy** — Distribuzione dell'applicazione (su un server di staging o di produzione).
6.  **Notify** — Invio di notifiche sullo stato della pipeline al team (ad esempio, in Slack, Email).

### 🛠 Strumenti popolari per CI/CD:

*   **GitHub Actions** (il nostro focus oggi!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 Perché abbiamo bisogno di CI/CD?

*   **Riduce l'errore umano:** L'automazione elimina gli errori associati alle operazioni manuali.
*   **Rilevamento rapido dei bug:** Gli errori vengono trovati prima, rendendoli più facili ed economici da correggere.
*   **Automazione delle attività di routine:** Gli sviluppatori dedicano meno tempo alla costruzione e alla distribuzione, e più al codice.
*   **Miglioramento della qualità del codice:** Controlli e test costanti elevano il livello di qualità generale.
*   **Consegna rapida delle funzionalità agli utenti:** Nuove funzionalità raggiungono l'utente finale più velocemente e più frequentemente.

### 📦 Esempi semplici di CI/CD con GitHub Actions

Vediamo le pipeline di base per le tecnologie più diffuse. Tutti gli esempi utilizzano GitHub Actions e vengono salvati nella directory `.github/workflows/` del tuo progetto.

#### 🐍 CI/CD per Python (con `pytest` e `flake8`)

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
          python-version: '3.11' # Specifica la tua versione

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Assicurati di avere requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Controlla il codice nelle cartelle src e tests (adatta al tuo progetto)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD per Node.js (con `npm test` e `eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # Specifica la tua versione di Node.js

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # o npm ci per un'installazione più prevedibile

      - name: Lint with ESLint
        run: npx eslint . # Assicurati che ESLint sia configurato nel progetto

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD per Docker (costruzione e push su Docker Hub)

Per questo esempio, avrai bisogno dei secret `DOCKER_USERNAME` e `DOCKER_PASSWORD` (o token) nelle impostazioni del tuo repository GitHub (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # Esegui solo per il branch main

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # Sostituisci myapp con il nome della tua applicazione
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Distribuzione su piattaforme popolari

Ora che abbiamo costruito e testato gli artefatti (ad esempio, un'immagine Docker), vediamo come possono essere distribuiti.

#### 🟣 Distribuzione su Heroku

**🔐 Secret GitHub:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

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
          git push heroku main -f # Fai attenzione con -f (force push)
```
Se stai distribuendo un'immagine Docker su Heroku:
```yaml
# ... (fasi di build e login a Docker Hub/GHCR dagli esempi precedenti) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # Dipende dal job di build dell'immagine
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # Supponendo che l'immagine sia costruita come ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 Distribuzione su AWS (ad esempio, statico su S3)

**🔐 Secret GitHub:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

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
        # Sostituisci ./public con il percorso dei tuoi file statici
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Per la distribuzione su **AWS Elastic Beanstalk**, di solito si usa la CLI di EB, la pipeline sarà simile, ma con i comandi `eb deploy`.

#### 🔵 Distribuzione su Google Cloud Platform (GCP App Engine)

**🔐 Secret GitHub:** `GCP_CREDENTIALS` (chiave JSON dell'account di servizio), `GCP_PROJECT_ID`.

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
        # Assicurati di avere app.yaml nella root del progetto
        run: gcloud app deploy --quiet
```

#### 🟪 Distribuzione su Render.com

Render spesso distribuisce automaticamente al push su GitHub, se il repository è connesso. Ma per un trigger manuale (o come parte di una pipeline più complessa) puoi usare un Deploy Hook.
**🔐 Secret GitHub:** `RENDER_DEPLOY_HOOK` (URL ottenuto dalle impostazioni del servizio Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Trigger manuale dall'UI di GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD Avanzato: Build Docker → Push su GHCR → Staging/Produzione su GCP Cloud Run

E ora la ciliegina sulla torta! Costruiamo una pipeline avanzata:
1.  Costruzione dell'immagine Docker.
2.  Pubblicazione dell'immagine su GitHub Container Registry (ghcr.io).
3.  Distribuzione automatica nell'ambiente di **staging** su GCP Cloud Run.
4.  Distribuzione nell'ambiente di **produzione** su GCP Cloud Run **dopo conferma manuale**.

Per questo, avremo bisogno di diversi file di workflow.

**Secret GitHub richiesti:**
*   `GCP_PROJECT_ID`: Il tuo ID progetto GCP.
*   `GCP_CREDENTIALS`: Chiave JSON di un account di servizio GCP con permessi per la distribuzione su Cloud Run e l'accesso a GHCR (se necessario). Di solito `GITHUB_TOKEN` è sufficiente per l'accesso a GHCR da Actions.
*   `GCP_REGION`: Regione per Cloud Run (ad esempio, `europe-west1`).

#### 1. Costruzione e pubblicazione dell'immagine Docker su GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main]

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # Per checkout
      packages: write     # Per push su GHCR

    steps:
      - uses: actions/checkout@v3

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build Docker image
        # Sostituisci myapp con il nome della tua applicazione
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```
*   `github.repository_owner`: Proprietario del repository (il tuo username o organizzazione).
*   `github.event.repository.name`: Nome del repository.
*   `myapp`: Nome della tua applicazione/immagine.

#### 2. Distribuzione automatica su Staging (GCP Cloud Run)

Questo workflow verrà eseguito automaticamente dopo il completamento con successo di `build.yml`.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # Nome del workflow di build
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Esegui solo se il workflow di build è stato completato con successo
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Usa gli ambienti GitHub per lo staging (opzionale, ma buona pratica)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # L'URL sarà disponibile dopo la distribuzione

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
          service: 'myapp-staging' # Nome del tuo servizio di staging in Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # Usa l'immagine che è stata pushata in build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Consenti l'accesso non autenticato per esempio
```

#### 3. Distribuzione in Produzione con conferma manuale (GCP Cloud Run)

Questo workflow viene attivato manualmente tramite l'interfaccia utente di GitHub Actions.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Consente il trigger manuale

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
          service: 'myapp-production' # Nome del tuo servizio di produzione
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Usa la stessa immagine 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Per la produzione, puoi aggiungere --no-traffic e poi passare gradualmente il traffico
          # traffic:
          #   latest: true
          #   percent: 100
```

**Punti importanti di questa pipeline avanzata:**
*   **GitHub Container Registry (ghcr.io):** Lo usiamo per archiviare le immagini Docker. Questo è comodo in quanto è strettamente integrato con GitHub Actions.
*   **`workflow_run`:** Consente di attivare un workflow (distribuzione di staging) al completamento di un altro (build).
*   **`workflow_dispatch`:** Offre la possibilità di attivare manualmente un workflow (distribuzione di produzione), fornendo controllo.
*   **Ambienti GitHub:** Ti consentono di configurare regole di protezione per la produzione (ad esempio, richiedendo l'approvazione di revisori specifici) e di archiviare secret specifici dell'ambiente.
*   **GCP Cloud Run:** Un'ottima opzione serverless per l'esecuzione di applicazioni containerizzate.

### 🔐 Sicurezza – è importante!

*   **Usa i secret di GitHub:** Non archiviare mai token, password, chiavi API direttamente nei file YAML. Usa `Settings -> Secrets and variables -> Actions` nel tuo repository.
*   **Privilegio minimo:** Per gli account di servizio (ad esempio, GCP), concedi solo i permessi strettamente necessari per eseguire le attività CI/CD.
*   **Isola gli ambienti:** Staging e Produzione dovrebbero essere il più isolati possibile. Progetti/account diversi nei provider cloud sono una buona pratica.
*   **Protezione dei branch:** Configura la protezione per il branch `main` (o `master`) in modo che i push siano possibili solo tramite Pull Request con controlli CI obbligatori.
