🚀 **CI/CD : Des bases à la production sur GCP avec GitHub Actions – Guide complet avec exemples** 🚀

Bonjour, les développeurs ! Dans cet article, je vais vous parler du concept de CI/CD.

### Qu'est-ce qu'un pipeline CI/CD dans le contexte de la programmation ?

**Un pipeline CI/CD (Intégration Continue / Livraison Continue ou Déploiement Continu)** est un processus automatisé qui permet aux développeurs de livrer rapidement et de manière fiable les modifications de code dans un environnement de production.

Examinons les concepts clés :

🔧 **CI — Intégration Continue**
C'est la pratique par laquelle les développeurs fusionnent fréquemment leurs modifications dans une base de code partagée. Chaque modification de ce type est automatiquement :
*   **Construite** (build)
*   **Testée** (tests unitaires, tests d'intégration)
*   **Vérifiée pour la conformité aux normes** (linting, analyse statique)

👉 **L'objectif de la CI :** Identifier les erreurs au stade le plus précoce, avant qu'elles ne cassent quelque chose d'important ou n'arrivent en production.

🚀 **CD — Livraison Continue ou Déploiement Continu**
Il y a deux options ici :

✅ **Livraison Continue**
Après avoir passé avec succès l'étape de la CI, les modifications sont automatiquement :
*   Soumises à des tests supplémentaires (par exemple, des tests E2E – de bout en bout)
*   Déployées sur un serveur de pré-production (staging)
👉 **Mais le déploiement en production nécessite toujours une approbation manuelle.** Cela donne à l'équipe le contrôle sur *quand* exactement les modifications seront vues par les utilisateurs.

🤖 **Déploiement Continu**
C'est l'étape suivante après la Livraison Continue. Ici, le déploiement en production se fait **entièrement automatiquement** si toutes les étapes précédentes du pipeline (construction, tous les tests) ont réussi. C'est le niveau d'automatisation le plus avancé.

### 🔄 De quoi se compose généralement un pipeline CI/CD ?

Un pipeline typique comprend les étapes suivantes :
1.  **Checkout** — Clonage de la dernière version du code depuis le dépôt.
2.  **Build** — Construction du projet (compilation, création d'artefacts, images Docker).
3.  **Test** — Exécution de différents types de tests (unitaires, d'intégration, E2E).
4.  **Lint/Qualité du code** — Vérification du code pour la conformité au style et les erreurs potentielles à l'aide d'analyseurs statiques.
5.  **Deploy** — Déploiement de l'application (sur un serveur de pré-production ou de production).
6.  **Notify** — Envoi de notifications sur l'état du pipeline à l'équipe (par exemple, dans Slack, par e-mail).

### 🛠 Outils populaires pour le CI/CD :

*   **GitHub Actions** (notre centre d'intérêt aujourd'hui !)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 Pourquoi avons-nous besoin du CI/CD ?

*   **Réduit les erreurs humaines :** L'automatisation élimine les erreurs liées aux opérations manuelles.
*   **Détection rapide des bogues :** Les erreurs sont trouvées plus tôt, ce qui les rend plus faciles et moins chères à corriger.
*   **Automatisation des tâches de routine :** Les développeurs passent moins de temps à construire et à déployer, et plus de temps à coder.
*   **Amélioration de la qualité du code :** Des vérifications et des tests constants élèvent le niveau de qualité général.
*   **Livraison rapide des fonctionnalités aux utilisateurs :** Les nouvelles fonctionnalités parviennent à l'utilisateur final plus rapidement et plus fréquemment.

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
        run: npx eslint . # Assurez-vous qu'ESLint est configuré dans le projet

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD pour Docker (construction et envoi vers Docker Hub)

Pour cet exemple, vous aurez besoin des secrets `DOCKER_USERNAME` et `DOCKER_PASSWORD` (ou un jeton) dans les paramètres de votre dépôt GitHub (`Settings -> Secrets and variables -> Actions`).

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

### 🚚 Déploiement sur des plateformes populaires

Maintenant que nous avons des artefacts construits et testés (par exemple, une image Docker), voyons comment ils peuvent être déployés.

#### 🟣 Déploiement sur Heroku

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
#   needs: build # Dépend du travail de construction de l'image
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

#### 🟨 Déploiement sur AWS (par exemple, des fichiers statiques sur S3)

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
        # Remplacez ./public par le chemin d'accès à vos fichiers statiques
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Pour le déploiement sur **AWS Elastic Beanstalk**, on utilise généralement l'EB CLI, le pipeline sera similaire, mais avec des commandes `eb deploy`.

#### 🔵 Déploiement sur Google Cloud Platform (GCP App Engine)

**🔐 Secrets GitHub :** `GCP_CREDENTIALS` (clé de compte de service JSON), `GCP_PROJECT_ID`.

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
        # Assurez-vous d'avoir app.yaml à la racine de votre projet
        run: gcloud app deploy --quiet
```

#### 🟪 Déploiement sur Render.com

Render se déploie souvent automatiquement lors d'un push sur GitHub si le dépôt est connecté. Mais pour un déclenchement manuel (ou dans le cadre d'un pipeline plus complexe), vous pouvez utiliser un Deploy Hook.
**🔐 Secrets GitHub :** `RENDER_DEPLOY_HOOK` (URL, obtenue à partir des paramètres du service dans Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Démarrage manuel depuis l'interface utilisateur de GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD avancé : Construire Docker → Pousser vers GHCR → Pré-production/Production sur GCP Cloud Run

Et maintenant, la cerise sur le gâteau ! Construisons un pipeline avancé :
1.  Construction d'une image Docker.
2.  Publication de l'image dans le GitHub Container Registry (ghcr.io).
3.  Déploiement automatique dans un environnement de **pré-production** sur GCP Cloud Run.
4.  Déploiement dans un environnement de **production** sur GCP Cloud Run **après approbation manuelle**.

Pour cela, nous aurons besoin de plusieurs fichiers de workflow.

**Secrets GitHub requis :**
*   `GCP_PROJECT_ID` : L'ID de votre projet dans GCP.
*   `GCP_CREDENTIALS` : Clé JSON d'un compte de service GCP avec les autorisations de déploiement sur Cloud Run et d'accès à GHCR (si nécessaire). Habituellement, `GITHUB_TOKEN` est suffisant pour accéder à GHCR depuis les Actions.
*   `GCP_REGION` : La région pour Cloud Run (par exemple, `europe-west1`).

#### 1. Construire et publier une image Docker sur GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # Exécuter lors d'un push sur main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # Pour le checkout
      packages: write     # Pour pousser vers GHCR

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
          # Vous pouvez également ajouter un balisage par SHA de commit pour l'unicité :
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner` : Le propriétaire du dépôt (votre nom d'utilisateur ou votre organisation).
*   `github.event.repository.name` : Le nom du dépôt.
*   `myapp` : Le nom de votre application/image.

#### 2. Déploiement automatique en pré-production (GCP Cloud Run)

Ce workflow sera déclenché automatiquement après la réussite de `build.yml`.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # Le nom du workflow de construction
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Exécuter uniquement si le workflow de construction s'est terminé avec succès
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Utiliser les environnements GitHub pour la pré-production (facultatif, mais bonne pratique)
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
          service: 'myapp-staging' # Le nom de votre service de pré-production dans Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # Utiliser l'image qui a été poussée dans build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Autoriser l'accès non authentifié pour l'exemple

```

#### 3. Déploiement en production avec approbation manuelle (GCP Cloud Run)

Ce workflow est déclenché manuellement via l'interface utilisateur de GitHub Actions.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Permet un démarrage manuel

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
          service: 'myapp-production' # Le nom de votre service de production
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Utiliser la même image 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Pour la production, vous pouvez ajouter --no-traffic, puis basculer progressivement le trafic
          # traffic:
          #   latest: true
          #   percent: 100
```

**Points importants de ce pipeline avancé :**
*   **GitHub Container Registry (ghcr.io) :** Nous l'utilisons pour stocker les images Docker. C'est pratique car il est étroitement intégré à GitHub Actions.
*   **`workflow_run` :** Permet d'exécuter un workflow (déploiement en pré-production) à la fin d'un autre (construction).
*   **`workflow_dispatch` :** Permet le démarrage manuel d'un workflow (déploiement en production), ce qui assure le contrôle.
*   **Environnements GitHub :** Permettent de configurer des règles de protection pour la production (par exemple, exiger l'approbation de réviseurs spécifiques) et de stocker des secrets spécifiques à l'environnement.
*   **GCP Cloud Run :** Une excellente option sans serveur pour exécuter des applications conteneurisées.

### 🔐 La sécurité est importante !

*   **Utilisez les secrets GitHub :** Ne stockez jamais de jetons, de mots de passe, de clés API directement dans les fichiers YAML. Utilisez `Settings -> Secrets and variables -> Actions` dans votre dépôt.
*   **Privilèges minimums :** Pour les comptes de service (par exemple, GCP), n'accordez que les autorisations réellement nécessaires pour effectuer les tâches de CI/CD.
*   **Isolez les environnements :** La pré-production et la production doivent être aussi isolées que possible. Des projets/comptes différents chez les fournisseurs de cloud sont une bonne pratique.
*   **Protection des branches :** Configurez la protection pour la branche `main` (ou `master`) afin de ne pouvoir y pousser que via une Pull Request avec des vérifications de CI obligatoires.
