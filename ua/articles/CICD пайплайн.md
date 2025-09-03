🚀 **CI/CD: Від основ до Production на GCP з GitHub Actions – Повний посібник з прикладами** 🚀

Привіт, розробники! У цій статті я розповім про CI/CD – концепцію.

### Що таке CI/CD пайплайн у контексті програмування?

**CI/CD пайплайн (Continuous Integration / Continuous Delivery або Continuous Deployment)** — це автоматизований процес, який дозволяє розробникам швидко та надійно доставляти зміни в коді в робоче середовище (продакшн).

Давайте розберемо ключові поняття:

🔧 **CI — Continuous Integration (Безперервна інтеграція)**
Це практика, при якій розробники часто вносять зміни в загальну кодову базу. Кожна така зміна автоматично:
*   **Збирається** (build)
*   **Тестується** (юніт-тести, інтеграційні тести)
*   **Перевіряється на відповідність стандартам** (лінтинг, статичний аналіз)

👉 **Мета CI:** Виявляти помилки на найранішому етапі, до того як вони зламають щось важливе або потраплять у реліз.

🚀 **CD — Continuous Delivery (Безперервна доставка) або Continuous Deployment (Безперервне розгортання)**
Тут є два варіанти:

✅ **Continuous Delivery (Безперервна доставка)**
Після успішного проходження етапу CI, зміни автоматично:
*   Проходять додаткові тести (наприклад, E2E – end-to-end тести)
*   Потрапляють на staging (тестовий) сервер
👉 **Але деплой у продакшн все ще вимагає ручного підтвердження.** Це дає команді контроль над тим, *коли* саме зміни побачать користувачі.

🤖 **Continuous Deployment (Безперервний деплой)**
Це наступний крок після Continuous Delivery. Тут деплой у продакшн відбувається **повністю автоматично**, якщо всі попередні етапи пайплайну (збірка, всі тести) пройшли успішно. Це найпросунутіший рівень автоматизації.

### 🔄 З чого зазвичай складається CI/CD пайплайн?

Типовий пайплайн включає наступні етапи:
1.  **Checkout** — Клонування останньої версії коду з репозиторію.
2.  **Build** — Збірка проекту (компіляція, збірка артефактів, Docker-образів).
3.  **Test** — Запуск різних видів тестів (юніт, інтеграційні, E2E).
4.  **Lint/Code Quality** — Перевірка коду на відповідність стилю та потенційні помилки за допомогою статичних аналізаторів.
5.  **Deploy** — Розгортання програми (на staging або production сервер).
6.  **Notify** — Надсилання сповіщень про статус пайплайну команді (наприклад, у Slack, Email).

### 🛠 Популярні інструменти для CI/CD:

*   **GitHub Actions** (наш фокус сьогодні!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 Навіщо взагалі потрібен CI/CD?

*   **Зменшує людський фактор:** Автоматизація виключає помилки, пов'язані з ручними операціями.
*   **Швидке виявлення багів:** Помилки знаходяться раніше, їх простіше та дешевше виправити.
*   **Автоматизація рутинних завдань:** Розробники витрачають менше часу на збірку та деплой, більше – на код.
*   **Покращення якості коду:** Постійні перевірки та тести підвищують загальну планку якості.
*   **Швидка доставка фіч користувачам:** Нові можливості доходять до кінцевого користувача швидше та частіше.

### 📦 Прості приклади CI/CD з GitHub Actions

Давайте подивимося на базові пайплайни для популярних технологій. Всі приклади використовують GitHub Actions і зберігаються в директорії `.github/workflows/` вашого проекту.

#### 🐍 CI/CD для Python (з `pytest` та `flake8`)

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
          python-version: '3.11' # Вкажіть вашу версію

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Переконайтеся, що у вас є requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Перевіряємо код у папках src та tests (адаптуйте під свій проект)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD для Node.js (з `npm test` та `eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # Вкажіть вашу версію Node.js

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # або npm ci для більш передбачуваної установки

      - name: Lint with ESLint
        run: npx eslint . # Переконайтеся, що ESLint налаштований у проекті

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD для Docker (збірка та пуш у Docker Hub)

Для цього прикладу вам знадобляться секрети `DOCKER_USERNAME` та `DOCKER_PASSWORD` (або токен) у налаштуваннях вашого GitHub репозиторію (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # Запускаємо тільки для main гілки

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # Замініть myapp на назву вашої програми
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Деплой на популярні платформи

Тепер, коли у нас є зібрані та протестовані артефакти (наприклад, Docker-образ), давайте подивимося, як їх можна розгорнути.

#### 🟣 Деплой на Heroku

**🔐 Секрети GitHub:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

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
          git push heroku main -f # Будьте обережні з -f (force push)
```
Якщо ви деплоїте Docker-образ на Heroku:
```yaml
# ... (кроки build та login to Docker Hub/GHCR з попередніх прикладів) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # Залежить від джоба збірки образу
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # Припускаємо, що образ зібраний як ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 Деплой на AWS (наприклад, статика в S3)

**🔐 Секрети GitHub:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

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
        # Замініть ./public на шлях до ваших статичних файлів
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Для деплою на **AWS Elastic Beanstalk** зазвичай використовується EB CLI, пайплайн буде схожий, але з командами `eb deploy`.

#### 🔵 Деплой на Google Cloud Platform (GCP App Engine)

**🔐 Секрети GitHub:** `GCP_CREDENTIALS` (JSON ключ сервіс-акаунту), `GCP_PROJECT_ID`.

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
        # Переконайтеся, що у вас є app.yaml у корені проекту
        run: gcloud app deploy --quiet
```

#### 🟪 Деплой на Render.com

Render часто автоматично деплоїть при push у GitHub, якщо репозиторій підключений. Але для ручного тригера (або як частина більш складного пайплайну) можна використовувати Deploy Hook.
**🔐 Секрети GitHub:** `RENDER_DEPLOY_HOOK` (URL, отриманий з налаштувань сервісу в Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Ручний запуск з UI GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 Просунутий CI/CD: Build Docker → Push у GHCR → Staging/Production на GCP Cloud Run

А тепер вишенька на торті! Зберемо просунутий пайплайн:
1.  Збірка Docker-образу.
2.  Публікація образу в GitHub Container Registry (ghcr.io).
3.  Автоматичний деплой у **staging** середовище на GCP Cloud Run.
4.  Деплой у **production** середовище на GCP Cloud Run **після ручного підтвердження**.

Для цього нам знадобиться кілька файлів воркфлоу.

**Необхідні секрети GitHub:**
*   `GCP_PROJECT_ID`: ID вашого проекту в GCP.
*   `GCP_CREDENTIALS`: JSON-ключ сервіс-акаунту GCP з правами на деплой у Cloud Run та доступ до GHCR (якщо потрібно). Зазвичай `GITHUB_TOKEN` достатньо для доступу до GHCR з Actions.
*   `GCP_REGION`: Регіон для Cloud Run (наприклад, `europe-west1`).

#### 1. Збірка та публікація Docker-образу в GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # Запускаємо при пуші в main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # Для checkout
      packages: write     # Для пушу в GHCR

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
          # Можна додати тегування за SHA коміту для унікальності:
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner`: Власник репозиторію (ваш username або організації).
*   `github.event.repository.name`: Назва репозиторію.
*   `myapp`: Назва вашої програми/образу.

#### 2. Автоматичний деплой у Staging (GCP Cloud Run)

Цей воркфлоу буде запускатися автоматично після успішного завершення `build.yml`.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # Назва воркфлоу збірки
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Запускаємо тільки якщо воркфлоу збірки завершився успішно
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Використовуємо GitHub Environments для staging (опціонально, але хороша практика)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # URL буде доступний після деплою

    steps:
      - uses: actions/checkout@v3 # Потрібен, якщо використовуєте конфігурації з репозиторію

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging' # Назва вашого staging сервісу в Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # Використовуємо образ, який був запушений в build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Дозволяємо неаутентифікований доступ для прикладу
```

#### 3. Деплой у Production з ручним підтвердженням (GCP Cloud Run)

Цей воркфлоу запускається вручну через UI GitHub Actions.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Дозволяє ручний запуск

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
          service: 'myapp-production' # Назва вашого production сервісу
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Використовуємо той самий 'latest' образ
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Для production можна додати --no-traffic і потім поступово перемикати трафік
          # traffic:
          #   latest: true
          #   percent: 100
```

**Важливі моменти цього просунутого пайплайну:**
*   **GitHub Container Registry (ghcr.io):** Ми використовуємо його для зберігання Docker-образів. Це зручно, оскільки він тісно інтегрований з GitHub Actions.
*   **`workflow_run`:** Дозволяє запускати один воркфлоу (деплой на staging) по завершенні іншого (збірка).
*   **`workflow_dispatch`:** Дає можливість ручного запуску воркфлоу (деплой на production), що забезпечує контроль.
*   **GitHub Environments:** Дозволяють налаштувати правила захисту для production (наприклад, вимагати схвалення від певних рев'юерів) та зберігати специфічні для середовища секрети.
*   **GCP Cloud Run:** Відмінний serverless-варіант для запуску контейнеризованих програм.

### 🔐 Безпека – це важливо!

*   **Використовуйте GitHub Secrets:** Ніколи не зберігайте токени, паролі, ключі API безпосередньо в YAML-файлах. Використовуйте `Settings -> Secrets and variables -> Actions` у вашому репозиторії.
*   **Мінімальні привілеї:** Для сервіс-акаунтів (наприклад, GCP) надавайте лише ті права, які дійсно необхідні для виконання завдань CI/CD.
*   **Ізолюйте середовища:** Staging та Production повинні бути максимально ізольовані. Різні проекти/акаунти в хмарних провайдерах – хороша практика.
*   **Захист гілок:** Налаштуйте захист для `main` (або `master`) гілки, щоб пушити в неї можна було лише через Pull Request з обов'язковими перевірками CI.
