🚀 **CI/CD: De lo básico a la producción en GCP con GitHub Actions – Una guía completa con ejemplos** 🚀

¡Hola, desarrolladores! En este artículo, hablaré sobre CI/CD – el concepto.

### ¿Qué es un pipeline de CI/CD en el contexto de la programación?

**Un pipeline de CI/CD (Integración Continua / Entrega Continua o Despliegue Continuo)** es un proceso automatizado que permite a los desarrolladores entregar cambios de código de forma rápida y fiable a un entorno de producción.

Desglosemos los conceptos clave:

🔧 **CI — Integración Continua**
Esta es una práctica en la que los desarrolladores integran frecuentemente cambios en una base de código compartida. Cada cambio de este tipo es automáticamente:
*   **Construido** (build)
*   **Probado** (pruebas unitarias, pruebas de integración)
*   **Verificado para el cumplimiento de estándares** (linting, análisis estático)

👉 **Objetivo de CI:** Identificar errores en la etapa más temprana posible, antes de que rompan algo importante o lleguen a la versión.

🚀 **CD — Entrega Continua (Continuous Delivery) o Despliegue Continuo (Continuous Deployment)**
Aquí hay dos opciones:

✅ **Entrega Continua (Continuous Delivery)**
Después de pasar con éxito la etapa de CI, los cambios automáticamente:
*   Se someten a pruebas adicionales (por ejemplo, E2E – pruebas de extremo a extremo)
*   Se despliegan en un servidor de staging (prueba)
👉 **Sin embargo, el despliegue a producción todavía requiere aprobación manual.** Esto le da al equipo control sobre *cuándo* exactamente los usuarios verán los cambios.

🤖 **Despliegue Continuo (Continuous Deployment)**
Este es el siguiente paso después de la Entrega Continua. Aquí, el despliegue a producción se realiza **completamente de forma automática** si todas las etapas anteriores del pipeline (construcción, todas las pruebas) son exitosas. Este es el nivel más avanzado de automatización.

### 🔄 ¿De qué se compone típicamente un pipeline de CI/CD?

Un pipeline típico incluye las siguientes etapas:
1.  **Checkout** — Clonación de la última versión del código desde el repositorio.
2.  **Build** — Construcción del proyecto (compilación, ensamblaje de artefactos, imágenes Docker).
3.  **Test** — Ejecución de varios tipos de pruebas (unitarias, de integración, E2E).
4.  **Lint/Code Quality** — Verificación del código para el cumplimiento de estilo y posibles errores utilizando analizadores estáticos.
5.  **Deploy** — Despliegue de la aplicación (a un servidor de staging o producción).
6.  **Notify** — Envío de notificaciones sobre el estado del pipeline al equipo (por ejemplo, Slack, Email).

### 🛠 Herramientas populares para CI/CD:

*   **GitHub Actions** (¡nuestro enfoque hoy!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 ¿Por qué necesitamos CI/CD?

*   **Reduce el error humano:** La automatización elimina los errores asociados con las operaciones manuales.
*   **Detección rápida de errores:** Los errores se encuentran antes, lo que los hace más fáciles y económicos de corregir.
*   **Automatización de tareas rutinarias:** Los desarrolladores dedican menos tiempo a la construcción y el despliegue, y más tiempo al código.
*   **Mejora de la calidad del código:** Las comprobaciones y pruebas continuas elevan el nivel de calidad general.
*   **Entrega más rápida de características a los usuarios:** Las nuevas funcionalidades llegan al usuario final más rápida y frecuentemente.

### 📦 Ejemplos sencillos de CI/CD con GitHub Actions

Veamos pipelines básicos para tecnologías populares. Todos los ejemplos utilizan GitHub Actions y se guardan en el directorio `.github/workflows/` de su proyecto.

#### 🐍 CI/CD para Python (con `pytest` y `flake8`)

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
          python-version: '3.11' # Especifique su versión

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Asegúrese de tener requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Verifique el código en las carpetas src y tests (adapte a su proyecto)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD para Node.js (con `npm test` y `eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # Especifique su versión de Node.js

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # o npm ci para una instalación más predecible

      - name: Lint with ESLint
        run: npx eslint . # Asegúrese de que ESLint esté configurado en el proyecto

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD para Docker (construcción y push a Docker Hub)

Para este ejemplo, necesitará los secretos `DOCKER_USERNAME` y `DOCKER_PASSWORD` (o token) en la configuración de su repositorio de GitHub (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # Ejecutar solo para la rama main

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # Reemplace myapp con el nombre de su aplicación
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Despliegue a plataformas populares

Ahora que tenemos artefactos construidos y probados (por ejemplo, una imagen Docker), veamos cómo se pueden desplegar.

#### 🟣 Despliegue a Heroku

**🔐 Secretos de GitHub:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

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
          git push heroku main -f # Tenga cuidado con -f (force push)
```
Si está desplegando una imagen Docker en Heroku:
```yaml
# ... (pasos de construcción e inicio de sesión en Docker Hub/GHCR de ejemplos anteriores) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # Depende del trabajo de construcción de la imagen
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # Suponiendo que la imagen se construye como ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 Despliegue a AWS (por ejemplo, estático en S3)

**🔐 Secretos de GitHub:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

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
        # Reemplace ./public con la ruta a sus archivos estáticos
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Para el despliegue a **AWS Elastic Beanstalk**, normalmente se usa EB CLI, el pipeline será similar, pero con comandos `eb deploy`.

#### 🔵 Despliegue a Google Cloud Platform (GCP App Engine)

**🔐 Secretos de GitHub:** `GCP_CREDENTIALS` (clave JSON de la cuenta de servicio), `GCP_PROJECT_ID`.

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
        # Asegúrese de tener app.yaml en la raíz del proyecto
        run: gcloud app deploy --quiet
```

#### 🟪 Despliegue a Render.com

Render a menudo despliega automáticamente al hacer push a GitHub si el repositorio está conectado. Pero para un disparador manual (o como parte de un pipeline más complejo), puede usar un Deploy Hook.
**🔐 Secretos de GitHub:** `RENDER_DEPLOY_HOOK` (URL obtenida de la configuración del servicio en Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Permite el disparo manual desde la interfaz de usuario de GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD avanzado: Construir Docker → Push a GHCR → Staging/Production en GCP Cloud Run

¡Y ahora, la guinda del pastel! Construyamos un pipeline avanzado:
1.  Construcción de la imagen Docker.
2.  Publicación de la imagen en el GitHub Container Registry (ghcr.io).
3.  Despliegue automático al entorno de **staging** en GCP Cloud Run.
4.  Despliegue al entorno de **producción** en GCP Cloud Run **después de la aprobación manual**.

Para esto, necesitaremos varios archivos de flujo de trabajo.

**Secretos de GitHub requeridos:**
*   `GCP_PROJECT_ID`: ID de su proyecto de GCP.
*   `GCP_CREDENTIALS`: Clave JSON de una cuenta de servicio de GCP con permisos para desplegar en Cloud Run y acceder a GHCR (si es necesario). `GITHUB_TOKEN` suele ser suficiente para el acceso a GHCR desde Actions.
*   `GCP_REGION`: Región para Cloud Run (por ejemplo, `europe-west1`).

#### 1. Construir y publicar la imagen Docker en GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # Ejecutar en push a main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # Para checkout
      packages: write     # Para push a GHCR

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
          # Puede agregar etiquetado por SHA de commit para la unicidad:
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner`: Propietario del repositorio (su nombre de usuario u organización).
*   `github.event.repository.name`: Nombre del repositorio.
*   `myapp`: Nombre de su aplicación/imagen.

#### 2. Despliegue automático a Staging (GCP Cloud Run)

Este flujo de trabajo se ejecutará automáticamente después de que `build.yml` se complete con éxito.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # Nombre del flujo de trabajo de construcción
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Ejecutar solo si el flujo de trabajo de construcción se completó con éxito
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Usar entornos de GitHub para staging (opcional, pero buena práctica)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # La URL estará disponible después del despliegue

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3 # Necesario si usa configuraciones del repositorio

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging' # Nombre de su servicio de staging en Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # Usar la imagen que se subió en build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Permitir acceso no autenticado para el ejemplo
```

#### 3. Despliegue a Producción con aprobación manual (GCP Cloud Run)

Este flujo de trabajo se activa manualmente a través de la interfaz de usuario de GitHub Actions.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Permite el disparo manual

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
          service: 'myapp-production' # Nombre de su servicio de producción
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Usar la misma imagen 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Para producción, puede agregar --no-traffic y luego cambiar el tráfico gradualmente
          # traffic:
          #   latest: true
          #   percent: 100
```

**Aspectos importantes de este pipeline avanzado:**
*   **GitHub Container Registry (ghcr.io):** Lo usamos para almacenar imágenes Docker. Es conveniente ya que está estrechamente integrado con GitHub Actions.
*   **`workflow_run`:** Permite activar un flujo de trabajo (despliegue de staging) al finalizar otro (construcción).
*   **`workflow_dispatch`:** Permite la activación manual de un flujo de trabajo (despliegue de producción), lo que proporciona control.
*   **Entornos de GitHub:** Permiten configurar reglas de protección para producción (por ejemplo, requerir la aprobación de revisores específicos) y almacenar secretos específicos del entorno.
*   **GCP Cloud Run:** Una excelente opción sin servidor para ejecutar aplicaciones en contenedores.

### 🔐 Seguridad – ¡Es importante!

*   **Use Secretos de GitHub:** Nunca almacene tokens, contraseñas o claves de API directamente en archivos YAML. Use `Settings -> Secrets and variables -> Actions` en su repositorio.
*   **Privilegio mínimo:** Para las cuentas de servicio (por ejemplo, GCP), otorgue solo los permisos estrictamente necesarios para realizar las tareas de CI/CD.
*   **Aislar entornos:** Staging y Producción deben estar lo más aislados posible. Los proyectos/cuentas separados en los proveedores de la nube son una buena práctica.
*   **Protección de ramas:** Configure la protección para la rama `main` (o `master`) para permitir pushes solo a través de Pull Requests con comprobaciones de CI obligatorias.
