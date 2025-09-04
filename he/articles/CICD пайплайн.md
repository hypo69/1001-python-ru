🚀 **CI/CD: מיסודות ועד Production ב-GCP עם GitHub Actions – מדריך מלא עם דוגמאות** 🚀

שלום, מפתחים! במאמר זה אדבר על CI/CD – קונספט.

### מהו צינור CI/CD בהקשר של תכנות?

**צינור CI/CD (אינטגרציה רציפה / אספקה רציפה או פריסה רציפה)** הוא תהליך אוטומטי המאפשר למפתחים לספק שינויים בקוד במהירות ובאמינות לסביבת ייצור.

בואו נפרק את מושגי המפתח:

🔧 **CI — אינטגרציה רציפה**
זוהי פרקטיקה שבה מפתחים משלבים לעיתים קרובות שינויים בבסיס קוד משותף. כל שינוי כזה באופן אוטומטי:
*   **נבנה** (<span dir="ltr">build</span>)
*   **נבדק** (בדיקות יחידה, בדיקות אינטגרציה)
*   **נבדק להתאמה לתקנים** (לינטינג, ניתוח סטטי)

👉 **מטרת CI:** לזהות שגיאות בשלב מוקדם ככל האפשר, לפני שהן שוברות משהו חשוב או מגיעות לגרסה.

🚀 **CD — אספקה רציפה או פריסה רציפה**
יש כאן שתי אפשרויות:

✅ **אספקה רציפה**
לאחר מעבר מוצלח של שלב ה-<span dir="ltr">CI</span>, השינויים באופן אוטומטי:
*   עוברים בדיקות נוספות (לדוגמה, בדיקות <span dir="ltr">E2E</span> – מקצה לקצה)
*   נפרסים לשרת <span dir="ltr">staging</span> (בדיקה)
👉 **אך פריסה לייצור עדיין דורשת אישור ידני.** זה נותן לצוות שליטה על *מתי* בדיוק המשתמשים יראו את השינויים.

🤖 **פריסה רציפה**
זהו השלב הבא לאחר אספקה רציפה. כאן, הפריסה לייצור מתרחשת **באופן אוטומטי לחלוטין**, אם כל שלבי הצינור הקודמים (בנייה, כל הבדיקות) עברו בהצלחה. זוהי הרמה המתקדמת ביותר של אוטומציה.

### 🔄 ממה מורכב בדרך כלל צינור CI/CD?

צינור טיפוסי כולל את השלבים הבאים:
1.  **<span dir="ltr">Checkout</span>** — שיבוט הגרסה האחרונה של הקוד מהמאגר.
2.  **<span dir="ltr">Build</span>** — בניית הפרויקט (קומפילציה, הרכבת ארטיפקטים, תמונות <span dir="ltr">Docker</span>).
3.  **<span dir="ltr">Test</span>** — הפעלת סוגים שונים של בדיקות (יחידה, אינטגרציה, <span dir="ltr">E2E</span>).
4.  **<span dir="ltr">Lint/Code Quality</span>** — בדיקת הקוד להתאמה לסגנון ושגיאות פוטנציאליות באמצעות מנתחים סטטיים.
5.  **<span dir="ltr">Deploy</span>** — פריסת היישום (לשרת <span dir="ltr">staging</span> או <span dir="ltr">production</span>).
6.  **<span dir="ltr">Notify</span>** — שליחת התראות על מצב הצינור לצוות (לדוגמה, ב-<span dir="ltr">Slack</span>, דוא"ל).

### 🛠 כלי CI/CD פופולריים:

*   **<span dir="ltr">GitHub Actions</span>** (המוקד שלנו היום!)
*   <span dir="ltr">GitLab CI/CD</span>
*   <span dir="ltr">Jenkins</span>
*   <span dir="ltr">CircleCI</span>
*   <span dir="ltr">Bitbucket Pipelines</span>
*   <span dir="ltr">Azure DevOps</span>
*   <span dir="ltr">TeamCity</span>

### 🧠 למה בכלל צריך CI/CD?

*   **מפחית טעויות אנוש:** אוטומציה מבטלת שגיאות הקשורות לפעולות ידניות.
*   **זיהוי מהיר של באגים:** שגיאות נמצאות מוקדם יותר, מה שהופך אותן לקלות וזולות יותר לתיקון.
*   **אוטומציה של משימות שגרתיות:** מפתחים מבלים פחות זמן בבנייה ופריסה, ויותר זמן בקידוד.
*   **שיפור איכות הקוד:** בדיקות ובדיקות רציפות מעלות את רף האיכות הכולל.
*   **אספקה מהירה של תכונות למשתמשים:** תכונות חדשות מגיעות למשתמש הקצה מהר יותר ולעיתים קרובות יותר.

### 📦 דוגמאות פשוטות ל-CI/CD עם GitHub Actions

בואו נסתכל על צינורות בסיסיים לטכנולוגיות פופולריות. כל הדוגמאות משתמשות ב-<span dir="ltr">GitHub Actions</span> ונשמרות בספריית <span dir="ltr">.github/workflows/</span> של הפרויקט שלכם.

#### 🐍 CI/CD עבור Python (עם <span dir="ltr">pytest</span> ו-<span dir="ltr">flake8</span>)

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

#### 🌐 CI/CD עבור Node.js (עם <span dir="ltr">npm test</span> ו-<span dir="ltr">eslint</span>)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # ציין את גרסת Node.js שלך

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

לדוגמה זו, תזדקקו לסודות <span dir="ltr">DOCKER_USERNAME</span> ו-<span dir="ltr">DOCKER_PASSWORD</span> (או אסימון) בהגדרות מאגר ה-<span dir="ltr">GitHub</span> שלכם (<span dir="ltr">Settings -> Secrets and variables -> Actions</span>).

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

כעת, כשיש לנו ארטיפקטים בנויים ונבדקים (לדוגמה, תמונת <span dir="ltr">Docker</span>), בואו נראה כיצד ניתן לפרוס אותם.

#### 🟣 פריסה ל-Heroku

**🔐 סודות GitHub:** <span dir="ltr">HEROKU_API_KEY</span>, <span dir="ltr">HEROKU_APP_NAME</span>.

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
אם אתם פורסים תמונת <span dir="ltr">Docker</span> ל-<span dir="ltr">Heroku</span>:
```yaml
# ... (שלבי build ו-login ל-Docker Hub/GHCR מדוגמאות קודמות) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # תלוי במשימת בניית התמונה
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # בהנחה שהתמונה נבנית כ-ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 פריסה ל-AWS (לדוגמה, קבצים סטטיים ל-S3)

**🔐 סודות GitHub:** <span dir="ltr">AWS_ACCESS_KEY_ID</span>, <span dir="ltr">AWS_SECRET_ACCESS_KEY</span>, <span dir="ltr">AWS_REGION</span>, <span dir="ltr">S3_BUCKET_NAME</span>.

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
לפריסה ל-<span dir="ltr">**AWS Elastic Beanstalk**</span> משתמשים בדרך כלל ב-<span dir="ltr">EB CLI</span>, הצינור יהיה דומה, אך עם פקודות <span dir="ltr">eb deploy</span>.

#### 🔵 פריסה ל-Google Cloud Platform (GCP App Engine)

**🔐 סודות GitHub:** <span dir="ltr">GCP_CREDENTIALS</span> (מפתח <span dir="ltr">JSON</span> של חשבון שירות), <span dir="ltr">GCP_PROJECT_ID</span>.

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

<span dir="ltr">Render</span> לעיתים קרובות פורס אוטומטית בדחיפה ל-<span dir="ltr">GitHub</span> אם המאגר מחובר. אך עבור טריגר ידני (או כחלק מצינור מורכב יותר), ניתן להשתמש ב-<span dir="ltr">Deploy Hook</span>.
**🔐 סודות GitHub:** <span dir="ltr">RENDER_DEPLOY_HOOK</span> (<span dir="ltr">URL</span> שהתקבל מהגדרות שירות <span dir="ltr">Render</span>).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # טריגר ידני מ-UI של GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD מתקדם: בניית Docker ← דחיפה ל-GHCR ← Staging/Production ב-GCP Cloud Run

ועכשיו הדובדבן שבקצפת! בואו נבנה צינור מתקדם:
1.  בניית תמונת <span dir="ltr">Docker</span>.
2.  פרסום תמונה ב-<span dir="ltr">GitHub Container Registry (ghcr.io)</span>.
3.  פריסה אוטומטית לסביבת <span dir="ltr">**staging**</span> ב-<span dir="ltr">GCP Cloud Run</span>.
4.  פריסה לסביבת <span dir="ltr">**production**</span> ב-<span dir="ltr">GCP Cloud Run</span> **לאחר אישור ידני**.

לשם כך, נזדקק למספר קבצי זרימת עבודה.

**סודות GitHub נדרשים:**
*   <span dir="ltr">GCP_PROJECT_ID</span>: מזהה הפרויקט שלכם ב-<span dir="ltr">GCP</span>.
*   <span dir="ltr">GCP_CREDENTIALS</span>: מפתח <span dir="ltr">JSON</span> של חשבון שירות <span dir="ltr">GCP</span> עם הרשאות לפריסה ל-<span dir="ltr">Cloud Run</span> וגישה ל-<span dir="ltr">GHCR</span> (אם נדרש). בדרך כלל <span dir="ltr">GITHUB_TOKEN</span> מספיק לגישה ל-<span dir="ltr">GHCR</span> מ-<span dir="ltr">Actions</span>.
*   <span dir="ltr">GCP_REGION</span>: אזור עבור <span dir="ltr">Cloud Run</span> (לדוגמה, <span dir="ltr">europe-west1</span>).

#### 1. בנייה ופרסום תמונת Docker ב-GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # הפעל בדחיפה ל-main

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

#### 🌐 CI/CD עבור Node.js (עם <span dir="ltr">npm test</span> ו-<span dir="ltr">eslint</span>)

```yaml
# .github/workflows/node-ci.yml
name: Node.js CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [18.x] # ציין את גרסת Node.js שלך

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

לדוגמה זו, תזדקקו לסודות <span dir="ltr">DOCKER_USERNAME</span> ו-<span dir="ltr">DOCKER_PASSWORD</span> (או אסימון) בהגדרות מאגר ה-<span dir="ltr">GitHub</span> שלכם (<span dir="ltr">Settings -> Secrets and variables -> Actions</span>).

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

כעת, כשיש לנו ארטיפקטים בנויים ונבדקים (לדוגמה, תמונת <span dir="ltr">Docker</span>), בואו נראה כיצד ניתן לפרוס אותם.

#### 🟣 פריסה ל-Heroku

**🔐 סודות GitHub:** <span dir="ltr">HEROKU_API_KEY</span>, <span dir="ltr">HEROKU_APP_NAME</span>.

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
אם אתם פורסים תמונת <span dir="ltr">Docker</span> ל-<span dir="ltr">Heroku</span>:
```yaml
# ... (שלבי build ו-login ל-Docker Hub/GHCR מדוגמאות קודמות) ...
# deploy:
#   name: Deploy to Heroku
#   needs: build # תלוי במשימת בניית התמונה
#   runs-on: ubuntu-latest
#   steps:
#     # ...
#     - name: Login to Heroku container registry
#       run: echo "${{ secrets.HEROKU_API_KEY }}" | docker login --username=_ --password-stdin registry.heroku.com
#     - name: Tag image for Heroku
#       # בהנחה שהתמונה נבנית כ-ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
```

#### 🟨 פריסה ל-AWS (לדוגמה, קבצים סטטיים ל-S3)

**🔐 סודות GitHub:** <span dir="ltr">AWS_ACCESS_KEY_ID</span>, <span dir="ltr">AWS_SECRET_ACCESS_KEY</span>, <span dir="ltr">AWS_REGION</span>, <span dir="ltr">S3_BUCKET_NAME</span>.

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
לפריסה ל-<span dir="ltr">**AWS Elastic Beanstalk**</span> משתמשים בדרך כלל ב-<span dir="ltr">EB CLI</span>, הצינור יהיה דומה, אך עם פקודות <span dir="ltr">eb deploy</span>.

#### 🔵 פריסה ל-Google Cloud Platform (GCP App Engine)

**🔐 סודות GitHub:** <span dir="ltr">GCP_CREDENTIALS</span> (מפתח <span dir="ltr">JSON</span> של חשבון שירות), <span dir="ltr">GCP_PROJECT_ID</span>.

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

<span dir="ltr">Render</span> לעיתים קרובות פורס אוטומטית בדחיפה ל-<span dir="ltr">GitHub</span> אם המאגר מחובר. אך עבור טריגר ידני (או כחלק מצינור מורכב יותר), ניתן להשתמש ב-<span dir="ltr">Deploy Hook</span>.
**🔐 סודות GitHub:** <span dir="ltr">RENDER_DEPLOY_HOOK</span> (<span dir="ltr">URL</span> שהתקבל מהגדרות שירות <span dir="ltr">Render</span>).

```yaml
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # טריגר ידני מ-UI של GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

### 🌟 CI/CD מתקדם: בניית Docker ← דחיפה ל-GHCR ← Staging/Production ב-GCP Cloud Run

ועכשיו הדובדבן שבקצפת! בואו נבנה צינור מתקדם:
1.  בניית תמונת <span dir="ltr">Docker</span>.
2.  פרסום תמונה ב-<span dir="ltr">GitHub Container Registry (ghcr.io)</span>.
3.  פריסה אוטומטית לסביבת <span dir="ltr">**staging**</span> ב-<span dir="ltr">GCP Cloud Run</span>.
4.  פריסה לסביבת <span dir="ltr">**production**</span> ב-<span dir="ltr">GCP Cloud Run</span> **לאחר אישור ידני**.

לשם כך, נזדקק למספר קבצי זרימת עבודה.

**סודות GitHub נדרשים:**
*   <span dir="ltr">GCP_PROJECT_ID</span>: מזהה הפרויקט שלכם ב-<span dir="ltr">GCP</span>.
*   <span dir="ltr">GCP_CREDENTIALS</span>: מפתח <span dir="ltr">JSON</span> של חשבון שירות <span dir="ltr">GCP</span> עם הרשאות לפריסה ל-<span dir="ltr">Cloud Run</span> וגישה ל-<span dir="ltr">GHCR</span> (אם נדרש). בדרך כלל <span dir="ltr">GITHUB_TOKEN</span> מספיק לגישה ל-<span dir="ltr">GHCR</span> מ-<span dir="ltr">Actions</span>.
*   <span dir="ltr">GCP_REGION</span>: אזור עבור <span dir="ltr">Cloud Run</span> (לדוגמה, <span dir="ltr">europe-west1</span>).

#### 1. בנייה ופרסום תמונת Docker ב-GHCR

```yaml
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # הפעל בדחיפה ל-main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read      # עבור checkout
      packages: write     # עבור push ל-GHCR

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
          # ניתן להוסיף תיוג לפי SHA של קומיט לייחודיות:
          # tags: |
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest
          #   ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:${{ github.sha }}
```
*   <span dir="ltr">github.repository_owner</span>: בעל המאגר (שם המשתמש או הארגון שלכם).
*   <span dir="ltr">github.event.repository.name</span>: שם המאגר.
*   <span dir="ltr">myapp</span>: שם היישום/תמונה שלכם.

#### 2. פריסה אוטומטית ל-Staging (GCP Cloud Run)

זרימת עבודה זו תופעל אוטומטית לאחר ש-<span dir="ltr">build.yml</span> יסתיים בהצלחה.

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

    # השתמש בסביבות GitHub עבור staging (אופציונלי, אך פרקטיקה טובה)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # ה-URL יהיה זמין לאחר הפריסה

    steps:
      - uses: actions/checkout@v3 # נדרש אם אתה משתמש בתצורות מהמאגר

      - id: 'auth'
        uses: 'google-github-actions/auth@v2'
        with:
          credentials_json: '${{ secrets.GCP_CREDENTIALS }}'

      - name: 'Deploy to Cloud Run (Staging)'
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'
        with:
          service: 'myapp-staging' # שם שירות ה-staging שלך ב-Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # השתמש בתמונה שנדחפה ב-build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # אפשר גישה לא מאומתת לדוגמה
```

#### 3. פריסה ל-Production עם אישור ידני (GCP Cloud Run)

זרימת עבודה זו מופעלת ידנית דרך ממשק המשתמש של <span dir="ltr">GitHub Actions</span>.

```yaml
# .github/workflows/deploy-prod.yml
name: Deploy to GCP Cloud Run (Production)

on:
  workflow_dispatch: # מאפשר טריגר ידני

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
          service: 'myapp-production' # שם שירות ה-production שלך
          region: '${{ secrets.GCP_REGION }}'
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest' # השתמש באותה תמונת 'latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed'
          # עבור production, ניתן להוסיף --no-traffic ולאחר מכן להעביר תנועה בהדרגה
          # traffic:
          #   latest: true
          #   percent: 100
```

**נקודות חשובות בצינור מתקדם זה:**
*   <span dir="ltr">**GitHub Container Registry (ghcr.io):**</span> אנו משתמשים בו לאחסון תמונות <span dir="ltr">Docker</span>. זה נוח מכיוון שהוא משולב היטב עם <span dir="ltr">GitHub Actions</span>.
*   <span dir="ltr">**workflow_run:**</span> מאפשר להפעיל זרימת עבודה אחת (פריסת <span dir="ltr">staging</span>) עם השלמת אחרת (בנייה).
*   <span dir="ltr">**workflow_dispatch:**</span> מספק את היכולת להפעיל ידנית זרימת עבודה (פריסת <span dir="ltr">production</span>), מה שמבטיח שליטה.
*   <span dir="ltr">**GitHub Environments:**</span> מאפשרים לכם להגדיר כללי הגנה עבור <span dir="ltr">production</span> (לדוגמה, דרישת אישור ממבקרים ספציפיים) ולאחסן סודות ספציפיים לסביבה.
*   <span dir="ltr">**GCP Cloud Run:**</span> אפשרות <span dir="ltr">serverless</span> מצוינת להפעלת יישומים מבוססי קונטיינרים.

### 🔐 אבטחה – זה חשוב!

*   <span dir="ltr">**השתמשו בסודות GitHub:**</span> לעולם אל תשמרו אסימונים, סיסמאות, מפתחות <span dir="ltr">API</span> ישירות בקבצי <span dir="ltr">YAML</span>. השתמשו ב-<span dir="ltr">Settings -> Secrets and variables -> Actions</span> במאגר שלכם.
*   <span dir="ltr">**הרשאות מינימליות:**</span> עבור חשבונות שירות (לדוגמה, <span dir="ltr">GCP</span>), העניקו רק את ההרשאות הנחוצות ביותר לביצוע משימות <span dir="ltr">CI/CD</span>.
*   <span dir="ltr">**בודדו סביבות:**</span> <span dir="ltr">Staging</span> ו-<span dir="ltr">Production</span> צריכים להיות מבודדים ככל האפשר. פרויקטים/חשבונות שונים בספקי ענן הם פרקטיקה טובה.
*   <span dir="ltr">**הגנת ענפים:**</span> הגדירו הגנה עבור ענף <span dir="ltr">main</span> (או <span dir="ltr">master</span>) כך שדחיפות אליו יהיו אפשריות רק באמצעות <span dir="ltr">Pull Requests</span> עם בדיקות <span dir="ltr">CI</span> חובה.
