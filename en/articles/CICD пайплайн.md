🚀 **CI/CD: From Basics to Production on GCP with GitHub Actions – A Complete Guide with Examples** 🚀

Hello, developers! In this article, I will talk about CI/CD – a concept.

### What is a CI/CD pipeline in the context of programming?

**CI/CD pipeline (Continuous Integration / Continuous Delivery or Continuous Deployment)** is an automated process that allows developers to quickly and reliably deliver code changes to a production environment.

Let's break down the key concepts:

🔧 **CI — Continuous Integration**
This is a practice where developers frequently integrate changes into a shared codebase. Each such change is automatically:
*   **Built**
*   **Tested** (unit tests, integration tests)
*   **Checked for compliance with standards** (linting, static analysis)

👉 **CI Goal:** To identify errors at the earliest stage, before they break something important or reach a release.

🚀 **CD — Continuous Delivery or Continuous Deployment**
There are two options here:

✅ **Continuous Delivery**
After successfully passing the CI stage, changes are automatically:
*   Undergo additional tests (e.g., E2E – end-to-end tests)
*   Are deployed to a staging (test) server
👉 **But deployment to production still requires manual confirmation.** This gives the team control over *when* exactly users will see the changes.

🤖 **Continuous Deployment**
This is the next step after Continuous Delivery. Here, deployment to production happens **fully automatically** if all previous pipeline stages (build, all tests) have passed successfully. This is the most advanced level of automation.

### 🔄 What does a CI/CD pipeline usually consist of?

A typical pipeline includes the following stages:
1.  **Checkout** — Cloning the latest version of the code from the repository.
2.  **Build** — Building the project (compilation, artifact assembly, Docker images).
3.  **Test** — Running various types of tests (unit, integration, E2E).
4.  **Lint/Code Quality** — Checking the code for style compliance and potential errors using static analyzers.
5.  **Deploy** — Deploying the application (to a staging or production server).
6.  **Notify** — Sending notifications about the pipeline status to the team (e.g., Slack, Email).

### 🛠 Popular CI/CD Tools:

*   **GitHub Actions** (our focus today!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 Why do we need CI/CD at all?

*   **Reduces human error:** Automation eliminates errors associated with manual operations.
*   **Fast bug detection:** Errors are found earlier, making them easier and cheaper to fix.
*   **Automation of routine tasks:** Developers spend less time on building and deploying, and more on coding.
*   **Improved code quality:** Continuous checks and tests raise the overall quality bar.
*   **Fast delivery of features to users:** New features reach the end-user faster and more frequently.

### 📦 Simple CI/CD Examples with GitHub Actions

Let's look at basic pipelines for popular technologies. All examples use GitHub Actions and are saved in the `.github/workflows/` directory of your project.

#### 🐍 CI/CD for Python (with `pytest` and `flake8`)

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
          python-version: '3.11' # Specify your version

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Make sure you have requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Check code in src and tests folders (adapt to your project)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD for Node.js (with `npm test` and `eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # Specify your Node.js version

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # or npm ci for more predictable installation

      - name: Lint with ESLint
        run: npx eslint . # Make sure ESLint is configured in the project

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD for Docker (build and push to Docker Hub)

For this example, you will need `DOCKER_USERNAME` and `DOCKER_PASSWORD` (or token) secrets in your GitHub repository settings (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # Run only for the main branch

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # Replace myapp with your application name
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Deploy to Popular Platforms

Now that we have built and tested artifacts (e.g., a Docker image), let's see how they can be deployed.

#### 🟣 Deploy to Heroku

**🔐 GitHub Secrets:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

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
          git push heroku main -f # Be careful with -f (force push)
```
If you are deploying a Docker image to Heroku:
```yaml
# ... (build and login to Docker Hub/GHCR steps from previous examples) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # Depends on the image build job
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # Assuming the image is built as ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 Deploy to AWS (e.g., static files to S3)

**🔐 GitHub Secrets:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

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
        # Replace ./public with the path to your static files
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
For deployment to **AWS Elastic Beanstalk**, the EB CLI is usually used, the pipeline will be similar, but with `eb deploy` commands.

#### 🔵 Deploy to Google Cloud Platform (GCP App Engine)

**🔐 GitHub Secrets:** `GCP_CREDENTIALS` (JSON service account key), `GCP_PROJECT_ID`.

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
        # Make sure you have app.yaml in the project root
        run: gcloud app deploy --quiet
```

#### 🟪 Deploy to Render.com

Render often automatically deploys on push to GitHub if the repository is connected. But for a manual trigger (or as part of a more complex pipeline), you can use a Deploy Hook.
**🔐 GitHub Secrets:** `RENDER_DEPLOY_HOOK` (URL obtained from Render service settings).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Manual trigger from GitHub UI

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 Advanced CI/CD: Build Docker → Push to GHCR → Staging/Production on GCP Cloud Run

And now for the icing on the cake! Let's build an advanced pipeline:
1.  Build Docker image.
2.  Publish image to GitHub Container Registry (ghcr.io).
3.  Automatic deployment to **staging** environment on GCP Cloud Run.
4.  Deployment to **production** environment on GCP Cloud Run **after manual confirmation**.

For this, we will need several workflow files.

**Required GitHub Secrets:**
*   `GCP_PROJECT_ID`: Your GCP project ID.
*   `GCP_CREDENTIALS`: JSON service account key for GCP with permissions to deploy to Cloud Run and access GHCR (if needed). Usually `GITHUB_TOKEN` is sufficient for GHCR access from Actions.
*   `GCP_REGION`: Region for Cloud Run (e.g., `europe-west1`).

#### 1. Build and publish Docker image to GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # Run on push to main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # For checkout
      packages: write     # For push to GHCR

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
          # You can add tagging by commit SHA for uniqueness:
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner`: Repository owner (your username or organization).
*   `github.event.repository.name`: Repository name.
*   `myapp`: Your application/image name.

#### 2. Automatic deployment to Staging (GCP Cloud Run)

This workflow will run automatically after `build.yml` completes successfully.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # Build workflow name
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Run only if the build workflow completed successfully
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Use GitHub Environments for staging (optional, but good practice)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # URL will be available after deployment

    steps:
      - uses: actions/checkout@v3 # Needed if you use configurations from the repository

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging' # Your staging Cloud Run service name
          region: '${{ secrets.GCP_REGION }}'
          # Use the image that was pushed in build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Allow unauthenticated access for example
```

#### 3. Deployment to Production with manual confirmation (GCP Cloud Run)

This workflow is triggered manually via the GitHub Actions UI.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Allows manual trigger

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
          service: 'myapp-production' # Your production service name
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Use the same 'latest' image
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # For production, you can add --no-traffic and then gradually shift traffic
          # traffic:
          #   latest: true
          #   percent: 100
```

**Important points of this advanced pipeline:**
*   **GitHub Container Registry (ghcr.io):** We use it to store Docker images. This is convenient as it is tightly integrated with GitHub Actions.
*   **`workflow_run`:** Allows one workflow (staging deployment) to be triggered upon completion of another (build).
*   **`workflow_dispatch`:** Provides the ability to manually trigger a workflow (production deployment), ensuring control.
*   **GitHub Environments:** Allow you to configure protection rules for production (e.g., requiring approval from specific reviewers) and store environment-specific secrets.
*   **GCP Cloud Run:** An excellent serverless option for running containerized applications.

### 🔐 Security – it's important!

*   **Use GitHub Secrets:** Never store tokens, passwords, API keys directly in YAML files. Use `Settings -> Secrets and variables -> Actions` in your repository.
*   **Minimum privileges:** For service accounts (e.g., GCP), grant only the permissions strictly necessary to perform CI/CD tasks.
*   **Isolate environments:** Staging and Production should be as isolated as possible. Different projects/accounts in cloud providers are good practice.
*   **Branch protection:** Configure protection for the `main` (or `master`) branch so that pushes to it are only possible via Pull Requests with mandatory CI checks.
