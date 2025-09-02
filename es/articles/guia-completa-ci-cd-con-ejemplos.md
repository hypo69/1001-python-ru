🚀 **CI/CD: De los conceptos básicos a la producción en GCP con GitHub Actions – Guía completa con ejemplos** 🚀

¡Hola, desarrolladores! En este artículo, hablaré sobre el concepto de CI/CD.

### ¿Qué es un pipeline de CI/CD en el contexto de la programación?

**Un pipeline de CI/CD (Integración Continua / Entrega Continua o Despliegue Continuo)** es un proceso automatizado que permite a los desarrolladores entregar cambios de código de forma rápida y fiable a un entorno de producción.

Desglosemos los conceptos clave:

🔧 **CI — Integración Continua**
Es la práctica en la que los desarrolladores fusionan con frecuencia sus cambios en una base de código compartida. Cada uno de estos cambios se somete automáticamente a:
*   **Construcción** (build)
*   **Pruebas** (pruebas unitarias, pruebas de integración)
*   **Comprobación del cumplimiento de los estándares** (linting, análisis estático)

👉 **El objetivo de la CI:** Identificar errores en la fase más temprana, antes de que rompan algo importante o lleguen a una versión.

🚀 **CD — Entrega Continua o Despliegue Continuo**
Aquí hay dos opciones:

✅ **Entrega Continua**
Después de pasar con éxito la fase de CI, los cambios se someten automáticamente a:
*   Pruebas adicionales (por ejemplo, pruebas E2E – de extremo a extremo)
*   Despliegue en un servidor de preproducción (staging)
👉 **Pero el despliegue a producción todavía requiere una aprobación manual.** Esto le da al equipo control sobre *cuándo* exactamente los usuarios verán los cambios.

🤖 **Despliegue Continuo**
Este es el siguiente paso después de la Entrega Continua. Aquí, el despliegue a producción se realiza **de forma totalmente automática** si todas las fases anteriores del pipeline (construcción, todas las pruebas) se han superado con éxito. Este es el nivel más avanzado de automatización.

### 🔄 ¿De qué se compone normalmente un pipeline de CI/CD?

Un pipeline típico incluye las siguientes fases:
1.  **Checkout** — Clonación de la última versión del código desde el repositorio.
2.  **Build** — Construcción del proyecto (compilación, creación de artefactos, imágenes de Docker).
3.  **Test** — Ejecución de varios tipos de pruebas (unitarias, de integración, E2E).
4.  **Lint/Calidad del código** — Comprobación del código para el cumplimiento del estilo y posibles errores mediante analizadores estáticos.
5.  **Deploy** — Despliegue de la aplicación (a un servidor de preproducción o producción).
6.  **Notify** — Envío de notificaciones sobre el estado del pipeline al equipo (por ejemplo, en Slack, correo electrónico).

### 🛠 Herramientas populares para CI/CD:

*   **GitHub Actions** (¡nuestro enfoque de hoy!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 ¿Por qué necesitamos CI/CD?

*   **Reduce el error humano:** La automatización elimina los errores asociados a las operaciones manuales.
*   **Detección rápida de errores:** Los errores se encuentran antes, lo que los hace más fáciles y baratos de corregir.
*   **Automatización de tareas rutinarias:** Los desarrolladores dedican menos tiempo a la construcción y el despliegue, y más al código.
*   **Mejora de la calidad del código:** Las comprobaciones y pruebas constantes elevan el listón de la calidad general.
*   **Entrega rápida de funciones a los usuarios:** Las nuevas funciones llegan al usuario final más rápido y con más frecuencia.

### 📦 Ejemplos sencillos de CI/CD con GitHub Actions

Veamos pipelines básicos para tecnologías populares. Todos los ejemplos utilizan GitHub Actions y se guardan en el directorio `.github/workflows/` de tu proyecto.

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
          python-version: '3.11' # Especifica tu versión

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # Asegúrate de tener requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # Comprueba el código en las carpetas src y tests (adáptalo a tu proyecto)
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
        node-version: [18.x] # Especifica tu versión de Node.js

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # o npm ci para una instalación más predecible

      - name: Lint with ESLint
        run: npx eslint . # Asegúrate de que ESLint esté configurado en el proyecto

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD para Docker (construcción y envío a Docker Hub)

Para este ejemplo, necesitarás los secretos `DOCKER_USERNAME` y `DOCKER_PASSWORD` (o un token) en la configuración de tu repositorio de GitHub (`Settings -> Secrets and variables -> Actions`).

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
        # Reemplaza myapp por el nombre de tu aplicación
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 Despliegue en plataformas populares

Ahora que tenemos artefactos construidos y probados (por ejemplo, una imagen de Docker), veamos cómo se pueden desplegar.

#### 🟣 Despliegue en Heroku

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
          git push heroku main -f # Ten cuidado con -f (force push)
```
Si estás desplegando una imagen de Docker en Heroku:
```yaml
# ... (pasos de construcción e inicio de sesión en Docker Hub/GHCR de los ejemplos anteriores) ...
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

#### 🟨 Despliegue en AWS (por ejemplo, archivos estáticos en S3)

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
        # Reemplaza ./public por la ruta a tus archivos estáticos
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
Para el despliegue en **AWS Elastic Beanstalk**, normalmente se utiliza la EB CLI, el pipeline será similar, pero con comandos `eb deploy`.

#### 🔵 Despliegue en Google Cloud Platform (GCP App Engine)

**🔐 Secretos de GitHub:** `GCP_CREDENTIALS` (clave de cuenta de servicio JSON), `GCP_PROJECT_ID`.

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
        # Asegúrate de tener app.yaml en la raíz de tu proyecto
        run: gcloud app deploy --quiet
```

#### 🟪 Despliegue en Render.com

Render a menudo se despliega automáticamente al hacer push en GitHub si el repositorio está conectado. Pero para un desencadenador manual (o como parte de un pipeline más complejo), puedes usar un Deploy Hook.
**🔐 Secretos de GitHub:** `RENDER_DEPLOY_HOOK` (URL, obtenida de la configuración del servicio en Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # Inicio manual desde la interfaz de usuario de GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD avanzado: Construir Docker → Enviar a GHCR → Preproducción/Producción en GCP Cloud Run

¡Y ahora la guinda del pastel! Construyamos un pipeline avanzado:
1.  Construcción de una imagen de Docker.
2.  Publicación de la imagen en el GitHub Container Registry (ghcr.io).
3.  Despliegue automático en un entorno de **preproducción** en GCP Cloud Run.
4.  Despliegue en un entorno de **producción** en GCP Cloud Run **previa aprobación manual**.

Para ello, necesitaremos varios archivos de workflow.

**Secretos de GitHub necesarios:**
*   `GCP_PROJECT_ID`: El ID de tu proyecto en GCP.
*   `GCP_CREDENTIALS`: Clave JSON de una cuenta de servicio de GCP con permisos para desplegar en Cloud Run y acceder a GHCR (si es necesario). Normalmente, `GITHUB_TOKEN` es suficiente para acceder a GHCR desde Actions.
*   `GCP_REGION`: La región para Cloud Run (por ejemplo, `europe-west1`).

#### 1. Construir y publicar una imagen de Docker en GHCR

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
      contents: read      # Para el checkout
      packages: write     # Para enviar a GHCR

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
          # También puedes añadir el etiquetado por el SHA del commit para la unicidad:
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner`: El propietario del repositorio (tu nombre de usuario u organización).
*   `github.event.repository.name`: El nombre del repositorio.
*   `myapp`: El nombre de tu aplicación/imagen.

#### 2. Despliegue automático en preproducción (GCP Cloud Run)

Este workflow se activará automáticamente después de la finalización con éxito de `build.yml`.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # El nombre del workflow de construcción
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # Ejecutar solo si el workflow de construcción se completó con éxito
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # Usar entornos de GitHub para preproducción (opcional, pero buena práctica)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # La URL estará disponible después del despliegue

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3 # Necesario si usas configuraciones del repositorio

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging' # El nombre de tu servicio de preproducción en Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # Usar la imagen que se envió en build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # Permitir el acceso no autenticado para el ejemplo

```

#### 3. Despliegue en producción con aprobación manual (GCP Cloud Run)

Este workflow se activa manualmente a través de la interfaz de usuario de GitHub Actions.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # Permite el inicio manual

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
          service: 'myapp-production' # El nombre de tu servicio de producción
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # Usar la misma imagen 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # Para producción, puedes añadir --no-traffic y luego cambiar gradualmente el tráfico
          # traffic:
          #   latest: true
          #   percent: 100
```

**Puntos importantes de este pipeline avanzado:**
*   **GitHub Container Registry (ghcr.io):** Lo usamos para almacenar imágenes de Docker. Es conveniente ya que está estrechamente integrado con GitHub Actions.
*   **`workflow_run`:** Permite ejecutar un workflow (despliegue en preproducción) al finalizar otro (construcción).
*   **`workflow_dispatch`:** Permite el inicio manual de un workflow (despliegue en producción), lo que proporciona control.
*   **Entornos de GitHub:** Permiten configurar reglas de protección para producción (por ejemplo, requerir la aprobación de revisores específicos) y almacenar secretos específicos del entorno.
*   **GCP Cloud Run:** Una excelente opción sin servidor para ejecutar aplicaciones en contenedores.

### 🔐 ¡La seguridad es importante!

*   **Usa los secretos de GitHub:** Nunca almacenes tokens, contraseñas, claves de API directamente en los archivos YAML. Usa `Settings -> Secrets and variables -> Actions` en tu repositorio.
*   **Privilegios mínimos:** Para las cuentas de servicio (por ejemplo, de GCP), concede solo los permisos que sean realmente necesarios para realizar las tareas de CI/CD.
*   **Aísla los entornos:** La preproducción y la producción deben estar lo más aisladas posible. Usar proyectos/cuentas diferentes en los proveedores de la nube es una buena práctica.
*   **Protección de ramas:** Configura la protección para la rama `main` (o `master`) para que solo se pueda enviar a ella a través de una Pull Request con comprobaciones de CI obligatorias.
