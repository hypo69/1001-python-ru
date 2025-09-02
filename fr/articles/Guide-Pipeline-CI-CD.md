🚀 **CI/CD : Des bases à la production sur GCP avec GitHub Actions – Un guide complet avec des exemples** 🚀

Bonjour, développeurs ! Dans cet article, je vais aborder le CI/CD – le concept.

### Qu'est-ce qu'un pipeline CI/CD dans le contexte de la programmation ?

**Un pipeline CI/CD (Intégration Continue / Livraison Continue ou Déploiement Continu)** est un processus automatisé qui permet aux développeurs de livrer rapidement et de manière fiable les modifications de code dans un environnement de production.

Décomposons les concepts clés :

🔧 **CI — Intégration Continue**
C'est une pratique où les développeurs intègrent fréquemment des modifications dans une base de code partagée. Chaque modification de ce type est automatiquement :
*   **Construite** (build)
*   **Testée** (tests unitaires, tests d'intégration)
*   **Vérifiée pour la conformité aux normes** (linting, analyse statique)

👉 **Objectif du CI :** Identifier les erreurs le plus tôt possible, avant qu'elles ne cassent quelque chose d'important ou n'atteignent la version.

🚀 **CD — Livraison Continue (Continuous Delivery) ou Déploiement Continu (Continuous Deployment)**
Il y a deux options ici :

✅ **Livraison Continue (Continuous Delivery)**
Après avoir réussi l'étape CI, les modifications automatiquement :
*   Subissent des tests supplémentaires (par exemple, E2E – tests de bout en bout)
*   Sont déployées sur un serveur de staging (test)
👉 **Cependant, le déploiement en production nécessite toujours une approbation manuelle.** Cela donne à l'équipe le contrôle sur *quand* exactement les utilisateurs verront les modifications.

🤖 **Déploiement Continu (Continuous Deployment)**
C'est l'étape suivante après la Livraison Continue. Ici, le déploiement en production se fait **entièrement automatiquement** si toutes les étapes précédentes du pipeline (construction, tous les tests) sont réussies. C'est le niveau d'automatisation le plus avancé.

### 🔄 De quoi se compose généralement un pipeline CI/CD ?

Un pipeline typique comprend les étapes suivantes :
1.  **Checkout** — Clonage de la dernière version du code depuis le dépôt.
2.  **Build** — Construction du projet (compilation, assemblage d'artefacts, images Docker).
3.  **Test** — Exécution de différents types de tests (unitaires, d'intégration, E2E).
4.  **Lint/Code Quality** — Vérification du code pour la conformité au style et les erreurs potentielles à l'aide d'analyseurs statiques.
5.  **Deploy** — Déploiement de l'application (vers un serveur de staging ou de production).
6.  **Notify** — Envoi de notifications sur l'état du pipeline à l'équipe (par exemple, Slack, Email).

### 🛠 Outils CI/CD populaires :

*   **GitHub Actions** (notre objectif aujourd'hui !)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 Pourquoi avons-nous besoin du CI/CD ?

*   **Réduit l'erreur humaine :** L'automatisation élimine les erreurs liées aux opérations manuelles.
*   **Détection rapide des bugs :** Les erreurs sont trouvées plus tôt, ce qui les rend plus faciles et moins coûteuses à corriger.
*   **Automatisation des tâches routinières :** Les développeurs passent moins de temps à la construction et au déploiement, et plus de temps au code.
*   **Amélioration de la qualité du code :** Les vérifications et les tests continus augmentent le niveau de qualité global.
*   **Livraison plus rapide des fonctionnalités aux utilisateurs :** Les nouvelles fonctionnalités atteignent l'utilisateur final plus rapidement et plus fréquemment.

### 📦 Exemples simples de CI/CD avec GitHub Actions

Examinons des pipelines de base pour les technologies populaires. Tous les exemples utilisent GitHub Actions et sont enregistrés dans le répertoire `.github/workflows/` de votre projet.

#### 🐍 CI/CD pour Python (avec `pytest` et `flake8`)

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
          python-version: '3.11' # Spécifiez votre version

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Assurez-vous d'avoir requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Vérifiez le code dans les dossiers src et tests (adaptez à votre projet)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD pour Node.js (avec `npm test` et `eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # Spécifiez votre version de Node.js

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # ou npm ci pour une installation plus prévisible

      - name: Lint with ESLint
        run: npx eslint . # Assurez-vous que ESLint est configuré dans le projet

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD pour Docker (construction et push vers Docker Hub)

Pour cet exemple, vous aurez besoin des secrets `DOCKER_USERNAME` et `DOCKER_PASSWORD` (ou d'un jeton) dans les paramètres de votre dépôt GitHub (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # Exécuter uniquement pour la branche main

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # Remplacez myapp par le nom de votre application
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Déploiement vers des plateformes populaires

Maintenant que nous avons des artefacts construits et testés (par exemple, une image Docker), voyons comment les déployer.

#### 🟣 Déploiement vers Heroku

**🔐 Secrets GitHub :** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

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
          git push heroku main -f # Soyez prudent avec -f (force push)
```
Si vous déployez une image Docker sur Heroku :
```yaml
# ... (étapes de construction et de connexion à Docker Hub/GHCR des exemples précédents) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # Dépend du job de construction de l'image
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # En supposant que l'image est construite comme ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 Déploiement vers AWS (par exemple, statique dans S3)

**🔐 Secrets GitHub :** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

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
        # Remplacez ./public par le chemin de vos fichiers statiques
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Pour le déploiement vers **AWS Elastic Beanstalk**, EB CLI est généralement utilisé, le pipeline sera similaire, mais avec les commandes `eb deploy`.

#### 🔵 Déploiement vers Google Cloud Platform (GCP App Engine)

**🔐 Secrets GitHub :** `GCP_CREDENTIALS` (clé JSON du compte de service), `GCP_PROJECT_ID`.

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
        # Assurez-vous d'avoir app.yaml à la racine du projet
        run: gcloud app deploy --quiet
```

#### 🟪 Déploiement vers Render.com

Render déploie souvent automatiquement lors d'un push vers GitHub si le dépôt est connecté. Mais pour un déclencheur manuel (ou dans le cadre d'un pipeline plus complexe), vous pouvez utiliser un Deploy Hook.
**🔐 Secrets GitHub :** `RENDER_DEPLOY_HOOK` (URL obtenue à partir des paramètres du service dans Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Permet le déclenchement manuel depuis l'interface utilisateur de GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD avancé : Construire Docker → Pousser vers GHCR → Staging/Production sur GCP Cloud Run

Et maintenant, la cerise sur le gâteau ! Construisons un pipeline avancé :
1.  Construction de l'image Docker.
2.  Publication de l'image dans le GitHub Container Registry (ghcr.io).
3.  Déploiement automatique vers l'environnement de **staging** sur GCP Cloud Run.
4.  Déploiement vers l'environnement de **production** sur GCP Cloud Run **après approbation manuelle**.

Pour cela, nous aurons besoin de plusieurs fichiers de workflow.

**Secrets GitHub requis :**
*   `GCP_PROJECT_ID` : ID de votre projet GCP.
*   `GCP_CREDENTIALS` : Clé JSON du compte de service GCP avec les autorisations de déploiement vers Cloud Run et d'accès à GHCR (si nécessaire). `GITHUB_TOKEN` est généralement suffisant pour l'accès à GHCR depuis Actions.
*   `GCP_REGION` : Région pour Cloud Run (par exemple, `europe-west1`).

#### 1. Construire et publier l'image Docker dans GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # Exécuter lors d'un push vers main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # Pour le checkout
      packages: write     # Pour le push vers GHCR

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

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
          # Vous pouvez ajouter un tag par SHA de commit pour l'unicité :
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner` : Propriétaire du dépôt (votre nom d'utilisateur ou organisation).
*   `github.event.repository.name` : Nom du dépôt.
*   `myapp` : Nom de votre application/image.

#### 2. Déploiement automatique vers Staging (GCP Cloud Run)

Ce workflow s'exécutera automatiquement après la réussite de `build.yml`.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # Nom du workflow de construction
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Exécuter uniquement si le workflow de construction s'est terminé avec succès
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Utiliser les environnements GitHub pour le staging (facultatif, mais bonne pratique)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # L'URL sera disponible après le déploiement

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3 # Nécessaire si vous utilisez des configurations du dépôt

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging' # Nom de votre service de staging dans Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # Utiliser l'image qui a été poussée dans build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Autoriser l'accès non authentifié pour l'exemple
```

#### 3. Déploiement en Production avec approbation manuelle (GCP Cloud Run)

Ce workflow est déclenché manuellement via l'interface utilisateur de GitHub Actions.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Permet le déclenchement manuel

jobs:
  deploy-production:
    runs-on: ubuntu-latest

    environment:
      name: production
      url: ${{ steps.deploy.outputs.url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Production)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-production' # Nom de votre service de production
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Utiliser la même image 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Pour la production, vous pouvez ajouter --no-traffic et ensuite basculer progressivement le trafic
          # traffic:
          #   latest: true
          #   percent: 100
```

**Aspects importants de ce pipeline avancé :**
*   **GitHub Container Registry (ghcr.io) :** Nous l'utilisons pour stocker les images Docker. C'est pratique car il est étroitement intégré à GitHub Actions.
*   **`workflow_run` :** Permet de déclencher un workflow (déploiement de staging) à la fin d'un autre (construction).
*   **`workflow_dispatch` :** Permet le déclenchement manuel d'un workflow (déploiement de production), offrant un contrôle.
*   **Environnements GitHub :** Permettent de configurer des règles de protection pour la production (par exemple, exiger l'approbation de relecteurs spécifiques) et de stocker des secrets spécifiques à l'environnement.
*   **GCP Cloud Run :** Une excellente option serverless pour exécuter des applications conteneurisées.

### 🔐 Sécurité – C'est important !

*   **Utilisez les secrets GitHub :** Ne stockez jamais les jetons, mots de passe ou clés API directement dans les fichiers YAML. Utilisez `Settings -> Secrets and variables -> Actions` dans votre dépôt.
*   **Moins de privilèges :** Pour les comptes de service (par exemple, GCP), n'accordez que les autorisations strictement nécessaires à l'exécution des tâches CI/CD.
*   **Isoler les environnements :** Le staging et la production doivent être aussi isolés que possible. Des projets/comptes séparés chez les fournisseurs de cloud sont une bonne pratique.
*   **Protection des branches :** Configurez la protection pour la branche `main` (ou `master`) afin d'autoriser les pushes uniquement via les Pull Requests avec des vérifications CI obligatoires.
