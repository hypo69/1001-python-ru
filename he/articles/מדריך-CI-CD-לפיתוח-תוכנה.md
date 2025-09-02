🚀 **CI/CD: מהיסודות ועד לפרודקשן ב-GCP עם GitHub Actions – מדריך מלא עם דוגמאות** 🚀

שלום, מפתחים! במאמר זה אסביר על CI/CD – הקונספט.

### מהו צינור CI/CD בהקשר של תכנות?

**צינור CI/CD (אינטגרציה רציפה / אספקה רציפה או פריסה רציפה)** הוא תהליך אוטומטי המאפשר למפתחים לספק שינויים בקוד במהירות ובאמינות לסביבת הייצור (פרודקשן).

בואו נפרט את מושגי המפתח:

🔧 **CI — אינטגרציה רציפה (Continuous Integration)**
זוהי פרקטיקה שבה מפתחים משלבים לעיתים קרובות שינויים בבסיס קוד משותף. כל שינוי כזה באופן אוטומטי:
*   **נבנה** (build)
*   **נבדק** (בדיקות יחידה, בדיקות אינטגרציה)
*   **נבדק להתאמה לתקנים** (לינטינג, ניתוח סטטי)

👉 **מטרת CI:** לזהות שגיאות בשלב מוקדם ככל האפשר, לפני שהן שוברות משהו חשוב או מגיעות לגרסה.

🚀 **CD — אספקה רציפה (Continuous Delivery) או פריסה רציפה (Continuous Deployment)**
יש כאן שתי אפשרויות:

✅ **אספקה רציפה (Continuous Delivery)**
לאחר מעבר מוצלח של שלב ה-CI, שינויים באופן אוטומטי:
*   עוברים בדיקות נוספות (לדוגמה, E2E – בדיקות מקצה לקצה)
*   מועברים לשרת Staging (בדיקה)
👉 **אך הפריסה לפרודקשן עדיין דורשת אישור ידני.** זה נותן לצוות שליטה על *מתי* בדיוק השינויים ייראו למשתמשים.

🤖 **פריסה רציפה (Continuous Deployment)**
זהו השלב הבא לאחר אספקה רציפה. כאן, הפריסה לפרודקשן מתבצעת **באופן אוטומטי לחלוטין**, אם כל שלבי הצינור הקודמים (בנייה, כל הבדיקות) עברו בהצלחה. זוהי רמת האוטומציה המתקדמת ביותר.

### 🔄 ממה מורכב בדרך כלל צינור CI/CD?

צינור טיפוסי כולל את השלבים הבאים:
1.  **Checkout** — שיבוט הגרסה האחרונה של הקוד מהמאגר.
2.  **Build** — בניית הפרויקט (קומפילציה, הרכבת ארטיפקטים, תמונות Docker).
3.  **Test** — הפעלת סוגי בדיקות שונים (יחידה, אינטגרציה, E2E).
4.  **Lint/Code Quality** — בדיקת הקוד להתאמה לסגנון ושגיאות פוטנציאליות באמצעות מנתחים סטטיים.
5.  **Deploy** — פריסת היישום (לשרת Staging או Production).
6.  **Notify** — שליחת התראות על סטטוס הצינור לצוות (לדוגמה, ל-Slack, אימייל).

### 🛠 כלים פופולריים ל-CI/CD:

*   **GitHub Actions** (המוקד שלנו היום!)
*   GitLab CI/CD
*   Jenkins
*   CircleCI
*   Bitbucket Pipelines
*   Azure DevOps
*   TeamCity

### 🧠 למה בכלל צריך CI/CD?

*   **מפחית טעויות אנוש:** אוטומציה מבטלת שגיאות הקשורות לפעולות ידניות.
*   **זיהוי מהיר של באגים:** שגיאות נמצאות מוקדם יותר, קל וזול יותר לתקן אותן.
*   **אוטומציה של משימות שגרתיות:** מפתחים מקדישים פחות זמן לבנייה ופריסה, ויותר – לקוד.
*   **שיפור איכות הקוד:** בדיקות ובחינות מתמשכות מעלות את רף האיכות הכללי.
*   **אספקה מהירה של פיצ'רים למשתמשים:** יכולות חדשות מגיעות למשתמש הקצה מהר יותר ולעיתים קרובות יותר.

### 📦 דוגמאות פשוטות ל-CI/CD עם GitHub Actions

בואו נסתכל על צינורות בסיסיים לטכנולוגיות פופולריות. כל הדוגמאות משתמשות ב-GitHub Actions ונשמרות בספריית `.github/workflows/` של הפרויקט שלכם.

#### 🐍 CI/CD עבור Python (עם `pytest` ו-`flake8`)

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
          python-version: '3.11' # ציין את הגרסה שלך

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt # ודא שיש לך requirements.txt
          pip install flake8 pytest

      - name: Lint with flake8
        run: |
          # בדוק קוד בתיקיות src ו-tests (התאם לפרויקט שלך)
          flake8 src tests

      - name: Run tests
        run: |
          pytest
```

#### 🌐 CI/CD עבור Node.js (עם `npm test` ו-`eslint`)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # ציין את גרסת ה-Node.js שלך

    steps:
      - uses: actions/checkout@v3

      - name: Use Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}

      - name: Install dependencies
        run: npm install # או npm ci להתקנה צפויה יותר

      - name: Lint with ESLint
        run: npx eslint . # ודא ש-ESLint מוגדר בפרויקט

      - name: Run tests
        run: npm test
```

#### 🐳 CI/CD עבור Docker (בנייה ודחיפה ל-Docker Hub)

לדוגמה זו תזדקק לסודות `DOCKER_USERNAME` ו-`DOCKER_PASSWORD` (או אסימון) בהגדרות מאגר GitHub שלך (`Settings -> Secrets and variables -> Actions`).

```yaml
# .github/workflows/docker-ci.yml
name: Docker CI/CD

on:
  push:
    branches: [ main ] # הפעל רק עבור ענף main

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

      - name: Build Docker image
        # החלף את myapp בשם היישום שלך
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
```

### 🚚 פריסה לפלטפורמות פופולריות

כעת, לאחר שיש לנו ארטיפקטים שנבנו ונבדקו (לדוגמה, תמונת Docker), בואו נראה כיצד ניתן לפרוס אותם.

#### 🟣 פריסה ל-Heroku

**🔐 סודות GitHub:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.

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
          git push heroku main -f # היזהר עם -f (force push)
```
אם אתה פורס תמונת Docker ל-Heroku:
```yaml
# ... (שלבי בנייה והתחברות ל-Docker Hub/GHCR מדוגמאות קודמות) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # תלוי במשימת בניית התמונה
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # בהנחה שהתמונה נבנתה כ-ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 פריסה ל-AWS (לדוגמה, קבצים סטטיים ל-S3)

**🔐 סודות GitHub:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.

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
        # החלף את ./public בנתיב לקבצים הסטטיים שלך
        run: aws s3 sync ./public s3://${{ secrets.S3_BUCKET_NAME }} --delete
```
לפריסה ל-**AWS Elastic Beanstalk** בדרך כלל משתמשים ב-EB CLI, הצינור יהיה דומה, אך עם פקודות `eb deploy`.

#### 🔵 פריסה ל-Google Cloud Platform (GCP App Engine)

**🔐 סודות GitHub:** `GCP_CREDENTIALS` (מפתח JSON של חשבון שירות), `GCP_PROJECT_ID`.

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
        # ודא שיש לך app.yaml בשורש הפרויקט
        run: gcloud app deploy --quiet
```

#### 🟪 פריסה ל-Render.com

Render לעיתים קרובות פורס אוטומטית בעת push ל-GitHub, אם המאגר מחובר. אך עבור טריגר ידני (או כחלק מצינור מורכב יותר), ניתן להשתמש ב-Deploy Hook.
**🔐 סודות GitHub:** `RENDER_DEPLOY_HOOK` (כתובת URL, שהתקבלה מהגדרות השירות ב-Render).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # מאפשר הפעלה ידנית מממשק המשתמש של GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD מתקדם: בניית Docker ← דחיפה ל-GHCR ← Staging/Production ב-GCP Cloud Run

ועכשיו, הדובדבן שבקצפת! בואו נבנה צינור מתקדם:
1.  בניית תמונת Docker.
2.  פרסום התמונה ב-GitHub Container Registry (ghcr.io).
3.  פריסה אוטומטית לסביבת **Staging** ב-GCP Cloud Run.
4.  פריסה לסביבת **Production** ב-GCP Cloud Run **לאחר אישור ידני**.

לשם כך, נזדקק למספר קבצי זרימת עבודה.

**סודות GitHub נדרשים:**
*   `GCP_PROJECT_ID`: מזהה הפרויקט שלך ב-GCP.
*   `GCP_CREDENTIALS`: מפתח JSON של חשבון שירות GCP עם הרשאות פריסה ל-Cloud Run וגישה ל-GHCR (אם נדרש). בדרך כלל `GITHUB_TOKEN` מספיק לגישה ל-GHCR מ-Actions.
*   `GCP_REGION`: אזור עבור Cloud Run (לדוגמה, `europe-west1`).

#### 1. בנייה ופרסום תמונת Docker ל-GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # הפעל בעת push ל-main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # עבור checkout
      packages: write     # עבור push ל-GHCR

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
          # ניתן להוסיף תיוג לפי SHA של הקומיט לייחודיות:
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   `github.repository_owner`: בעל המאגר (שם המשתמש או הארגון שלך).
*   `github.event.repository.name`: שם המאגר.
*   `myapp`: שם היישום/התמונה שלך.

#### 2. פריסה אוטומטית ל-Staging (GCP Cloud Run)

זרימת עבודה זו תופעל אוטומטית לאחר השלמה מוצלחת של `build.yml`.

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # שם זרימת העבודה של הבנייה
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # הפעל רק אם זרימת העבודה של הבנייה הסתיימה בהצלחה
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # השתמש בסביבות GitHub עבור Staging (אופציונלי, אך מומלץ)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # כתובת URL תהיה זמינה לאחר הפריסה

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3 # נדרש אם אתה משתמש בתצורות מהמאגר

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging' # שם שירות ה-Staging שלך ב-Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # השתמש בתמונה שנדחפה ב-build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # אפשר גישה לא מאומתת לדוגמה
```

#### 3. פריסה לפרודקשן עם אישור ידני (GCP Cloud Run)

זרימת עבודה זו מופעלת ידנית דרך ממשק המשתמש של GitHub Actions.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # מאפשר הפעלה ידנית

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
          service: 'myapp-production' # שם שירות הפרודקשן שלך
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # השתמש באותה תמונת 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # עבור פרודקשן, ניתן להוסיף --no-traffic ולאחר מכן להעביר את התעבורה בהדרגה
          # traffic:
          #   latest: true
          #   percent: 100
```

**היבטים חשובים של צינור מתקדם זה:**
*   **GitHub Container Registry (ghcr.io):** אנו משתמשים בו לאחסון תמונות Docker. זה נוח, מכיוון שהוא משולב היטב עם GitHub Actions.
*   **`workflow_run`:** מאפשר הפעלת זרימת עבודה אחת (פריסת Staging) עם השלמת אחרת (בנייה).
*   **`workflow_dispatch`:** מאפשר הפעלה ידנית של זרימת עבודה (פריסת Production), ומספק שליטה.
*   **סביבות GitHub:** מאפשרות הגדרת כללי הגנה עבור Production (לדוגמה, דרישת אישור ממבקרים ספציפיים) ואחסון סודות ספציפיים לסביבה.
*   **GCP Cloud Run:** אפשרות serverless מצוינת להפעלת יישומים מבוססי קונטיינרים.

### 🔐 אבטחה – זה חשוב!

*   **השתמש בסודות GitHub:** לעולם אל תשמור אסימונים, סיסמאות או מפתחות API ישירות בקבצי YAML. השתמש ב-`Settings -> Secrets and variables -> Actions` במאגר שלך.
*   **הרשאות מינימליות:** עבור חשבונות שירות (לדוגמה, GCP) הענק רק את ההרשאות הנחוצות באמת לביצוע משימות CI/CD.
*   **בידוד סביבות:** Staging ו-Production צריכים להיות מבודדים ככל האפשר. פרויקטים/חשבונות נפרדים בספקי ענן – זוהי פרקטיקה טובה.
*   **הגנת ענפים:** הגדר הגנה עבור ענף `main` (או `master`), כך שניתן יהיה לדחוף אליו רק באמצעות Pull Request עם בדיקות CI חובה.
