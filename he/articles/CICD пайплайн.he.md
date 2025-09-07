🚀 **CI/CD: מיסודות לייצור ב-<span dir="ltr">GCP</span> עם <span dir="ltr">GitHub</span> <span dir="ltr">Actions</span> – מדריך מלא עם דוגמאות** 🚀

שלום, מפתחים! במאמר זה אדבר על <span dir="ltr">CI</span>/<span dir="ltr">CD</span> – הקונספט.

### מהו <span dir="ltr">CI</span>/<span dir="ltr">CD</span> <span dir="ltr">pipeline</span> בהקשר של תכנות?

**<span dir="ltr">CI</span>/<span dir="ltr">CD</span> <span dir="ltr">pipeline</span> (<span dir="ltr">Continuous</span> <span dir="ltr">Integration</span> / <span dir="ltr">Continuous</span> <span dir="ltr">Delivery</span> או <span dir="ltr">Continuous</span> <span dir="ltr">Deployment</span>)** הוא תהליך אוטומטי, המאפשר למפתחים לספק שינויי קוד במהירות ובאמינות לסביבת עבודה (פרודקשן).

בואו נפרק את מושגי המפתח:

🔧 **<span dir="ltr">CI</span> — <span dir="ltr">Continuous</span> <span dir="ltr">Integration</span> (אינטגרציה מתמשכת)**
זוהי פרקטיקה שבה מפתחים מבצעים שינויים תכופים בבסיס קוד משותף. כל שינוי כזה באופן אוטומטי:
*   **נבנה** (<span dir="ltr">build</span>)
*   **נבדק** (בדיקות יחידה, בדיקות אינטגרציה)
*   **נבדק להתאמה לתקנים** (<span dir="ltr">linting</span>, ניתוח סטטי)

👉 **מטרת <span dir="ltr">CI</span>:** לזהות שגיאות בשלב מוקדם ככל האפשר, לפני שהן שוברות משהו חשוב או מגיעות לגרסה.

🚀 **<span dir="ltr">CD</span> — <span dir="ltr">Continuous</span> <span dir="ltr">Delivery</span> (אספקה מתמשכת) או <span dir="ltr">Continuous</span> <span dir="ltr">Deployment</span> (פריסה מתמשכת)**
כאן יש שתי אפשרויות:

✅ **<span dir="ltr">Continuous</span> <span dir="ltr">Delivery</span> (אספקה מתמשכת)**
לאחר השלמה מוצלחת של שלב ה-<span dir="ltr">CI</span>, השינויים באופן אוטומטי:
*   עוברים בדיקות נוספות (לדוגמה, <span dir="ltr">E2E</span> – בדיקות מקצה לקצה)
*   מגיעים לשרת <span dir="ltr">staging</span> (בדיקה)
👉 **אך פריסה לפרודקשן עדיין דורשת אישור ידני.** זה נותן לצוות שליטה על *מתי* בדיוק המשתמשים יראו את השינויים.

🤖 **<span dir="ltr">Continuous</span> <span dir="ltr">Deployment</span> (פריסה מתמשכת)**
זהו השלב הבא לאחר <span dir="ltr">Continuous</span> <span dir="ltr">Delivery</span>. כאן הפריסה לפרודקשן מתרחשת **באופן אוטומטי לחלוטין**, אם כל שלבי ה-<span dir="ltr">pipeline</span> הקודמים (בנייה, כל הבדיקות) עברו בהצלחה. זוהי הרמה המתקדמת ביותר של אוטומציה.

### 🔄 ממה מורכב בדרך כלל <span dir="ltr">CI</span>/<span dir="ltr">CD</span> <span dir="ltr">pipeline</span>?

<span dir="ltr">Pipeline</span> טיפוסי כולל את השלבים הבאים:
1.  **<span dir="ltr">Checkout</span>** — שיבוט הגרסה האחרונה של הקוד מהמאגר.
2.  **<span dir="ltr">Build</span>** — בניית הפרויקט (קומפילציה, הרכבת ארטיפקטים, תמונות <span dir="ltr">Docker</span>).
3.  **<span dir="ltr">Test</span>** — הפעלת סוגים שונים של בדיקות (יחידה, אינטגרציה, <span dir="ltr">E2E</span>).
4.  **<span dir="ltr">Lint</span>/<span dir="ltr">Code</span> <span dir="ltr">Quality</span>** — בדיקת קוד להתאמה לסגנון ושגיאות פוטנציאליות באמצעות מנתחים סטטיים.
5.  **<span dir="ltr">Deploy</span>** — פריסת היישום (לשרת <span dir="ltr">staging</span> או <span dir="ltr">production</span>).
6.  **<span dir="ltr">Notify</span>** — שליחת התראות על סטטוס ה-<span dir="ltr">pipeline</span> לצוות (לדוגמה, ב-<span dir="ltr">Slack</span>, <span dir="ltr">Email</span>).

### 🛠 כלים פופולריים ל-<span dir="ltr">CI</span>/<span dir="ltr">CD</span>:

*   **<span dir="ltr">GitHub</span> <span dir="ltr">Actions</span>** (המוקד שלנו היום!)
*   <span dir="ltr">GitLab</span> <span dir="ltr">CI</span>/<span dir="ltr">CD</span>
*   <span dir="ltr">Jenkins</span>
*   <span dir="ltr">CircleCI</span>
*   <span dir="ltr">Bitbucket</span> <span dir="ltr">Pipelines</span>
*   <span dir="ltr">Azure</span> <span dir="ltr">DevOps</span>
*   <span dir="ltr">TeamCity</span>

### 🧠 למה בכלל צריך <span dir="ltr">CI</span>/<span dir="ltr">CD</span>?

*   **מפחית טעויות אנוש:** אוטומציה מבטלת שגיאות הקשורות לפעולות ידניות.
*   **זיהוי מהיר של באגים:** שגיאות נמצאות מוקדם יותר, קל וזול יותר לתקן אותן.
*   **אוטומציה של משימות שגרתיות:** מפתחים מקדישים פחות זמן לבנייה ופריסה, ויותר – לקוד.
*   **שיפור איכות הקוד:** בדיקות ומבחנים מתמידים מעלים את רף האיכות הכללי.
*   **אספקה מהירה של פיצ'רים למשתמשים:** יכולות חדשות מגיעות למשתמש הקצה מהר יותר ובתדירות גבוהה יותר.

### 📦 דוגמאות פשוטות ל-<span dir="ltr">CI</span>/<span dir="ltr">CD</span> עם <span dir="ltr">GitHub</span> <span dir="ltr">Actions</span>

בואו נסתכל על <span dir="ltr">pipelines</span> בסיסיים לטכנולוגיות פופולריות. כל הדוגמאות משתמשות ב-<span dir="ltr">GitHub</span> <span dir="ltr">Actions</span> ונשמרות בספריית <<span dir="ltr">span</span> <span dir="ltr">dir</span>="<span dir="ltr">ltr</span>"><<span dir="ltr">code</span>>.<span dir="ltr">github</span>/<span dir="ltr">workflows</span>/</<span dir="ltr">code</span>></<span dir="ltr">span</span>> של הפרויקט שלכם.

#### 🐍 <span dir="ltr">CI</span>/<span dir="ltr">CD</span> עבור <span dir="ltr">Python</span> (עם <<span dir="ltr">span</span> <span dir="ltr">dir</span>="<span dir="ltr">ltr</span>"><<span dir="ltr">code</span>><span dir="ltr">pytest</span></<span dir="ltr">code</span>></<span dir="ltr">span</span>> ו-<span dir="ltr">flake8</span>)

<pre class="line-numbers"><code class="language-yaml">
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
</code></pre>
<h4>🌐 <span dir="ltr">CI</span>/<span dir="ltr">CD</span> עבור <span dir="ltr">Node.js</span> (עם <<span dir="ltr">span</span> <span dir="ltr">dir</span>="<span dir="ltr">ltr</span>"><<span dir="ltr">code</span>><span dir="ltr">npm</span> <span dir="ltr">test</span></<span dir="ltr">code</span>></<span dir="ltr">span</span>> ו-<span dir="ltr">eslint</span>)

<pre class="line-numbers"><code class="language-yaml">
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
</code></pre>
<h4>🐳 <span dir="ltr">CI</span>/<span dir="ltr">CD</span> עבור <span dir="ltr">Docker</span> (בנייה ו-<span dir="ltr">push</span> ל-<span dir="ltr">Docker</span> <span dir="ltr">Hub</span>)</h4>
<p>לדוגמה זו, תצטרך סודות `DOCKER_USERNAME` ו-`DOCKER_PASSWORD` (או אסימון) בהגדרות מאגר ה-<span dir="ltr">GitHub</span> שלך (`Settings -> Secrets and variables -> Actions`).</p>
<pre class="line-numbers"><code class="language-yaml">
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
</code></pre>
<h3>🚚 פריסה לפלטפורמות פופולריות</h3>
<p>כעת, כשיש לנו ארטיפקטים בנויים ונבדקים (לדוגמה, תמונת <span dir="ltr">Docker</span>), בואו נראה כיצד ניתן לפרוס אותם.</p>
<h4>🟣 פריסה ל-<span dir="ltr">Heroku</span></h4>
<p>**🔐 סודות <span dir="ltr">GitHub</span>:** `HEROKU_API_KEY`, `HEROKU_APP_NAME`.</p>
<pre class="line-numbers"><code class="language-yaml">
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
</code></pre>
<p>אם אתה פורס תמונת <span dir="ltr">Docker</span> ל-<span dir="ltr">Heroku</span>:</p>
<pre class="line-numbers"><code class="language-yaml">
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
#       # בהנחה שהתמונה נבנית כ-ghcr.io/username/repo/myapp:latest
#       run: docker tag ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Push image to Heroku
#       run: docker push registry.heroku.com/${{ secrets.HEROKU_APP_NAME }}/web
#     - name: Release Heroku App
#       env:
#         HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
#       run: heroku container:release web --app ${{ secrets.HEROKU_APP_NAME }}
</code></pre>
<h4>🟨 פריסה ל-<span dir="ltr">AWS</span> (לדוגמה, סטטי ל-<span dir="ltr">S3</span>)</h4>
<p>**🔐 סודות <span dir="ltr">GitHub</span>:** `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `S3_BUCKET_NAME`.</p>
<pre class="line-numbers"><code class="language-yaml">
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
</code></pre>
<p>לפריסה ל-<span dir="ltr">**AWS**</span> <span dir="ltr">**Elastic**</span> <span dir="ltr">**Beanstalk**</span> בדרך כלל משתמשים ב-<span dir="ltr">EB</span> <span dir="ltr">CLI</span>, ה-<span dir="ltr">pipeline</span> יהיה דומה, אך עם פקודות <<span dir="ltr">span</span> <span dir="ltr">dir</span>="<span dir="ltr">ltr</span>"><<span dir="ltr">code</span>><span dir="ltr">eb</span> <span dir="ltr">deploy</span></<span dir="ltr">code</span>></<span dir="ltr">span</span>>.</p>
<h4>🔵 פריסה ל-<span dir="ltr">Google</span> <span dir="ltr">Cloud</span> <span dir="ltr">Platform</span> (<span dir="ltr">GCP</span> <span dir="ltr">App</span> <span dir="ltr">Engine</span>)</h4>
<p>**🔐 סודות <span dir="ltr">GitHub</span>:** `GCP_CREDENTIALS` (מפתח <span dir="ltr">JSON</span> של חשבון שירות), `GCP_PROJECT_ID`.</p>
<pre class="line-numbers"><code class="language-yaml">
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
</code></pre>
<h4>🟪 פריסה ל-<span dir="ltr">Render.com</span></h4>
<p><span dir="ltr">Render</span> לעיתים קרובות פורס אוטומטית ב-<span dir="ltr">push</span> ל-<span dir="ltr">GitHub</span>, אם המאגר מחובר. אבל עבור טריגר ידני (או כחלק מ-<span dir="ltr">pipeline</span> מורכב יותר) ניתן להשתמש ב-<span dir="ltr">Deploy</span> <span dir="ltr">Hook</span>.</p>
<p>**🔐 סודות <span dir="ltr">GitHub</span>:** `RENDER_DEPLOY_HOOK` (<span dir="ltr">URL</span>, שהתקבל מהגדרות השירות ב-<span dir="ltr">Render</span>).</p>
<pre class="line-numbers"><code class="language-yaml">
# .github/workflows/deploy-render.yml
name: Trigger Render Deploy

on:
  workflow_dispatch: # הפעלה ידנית מ-UI GitHub

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Render Deploy Hook
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
</code></pre>
<h3>🌟 <span dir="ltr">CI</span>/<span dir="ltr">CD</span> מתקדם: בניית <span dir="ltr">Docker</span> ← <span dir="ltr">Push</span> ל-<span dir="ltr">GHCR</span> ← <span dir="ltr">Staging</span>/<span dir="ltr">Production</span> ב-<span dir="ltr">GCP</span> <span dir="ltr">Cloud</span> <span dir="ltr">Run</span></h3>
<p>ועכשיו הדובדבן שבקצפת! נבנה <span dir="ltr">pipeline</span> מתקדם:</p>
<li>בניית תמונת <span dir="ltr">Docker</span>.</li>
<li>פרסום התמונה ב-<span dir="ltr">GitHub</span> <span dir="ltr">Container</span> <span dir="ltr">Registry</span> (<span dir="ltr">ghcr.io</span>).</li>
<li>פריסה אוטומטית לסביבת **<span dir="ltr">staging</span>** ב-<span dir="ltr">GCP</span> <span dir="ltr">Cloud</span> <span dir="ltr">Run</span>.</li>
<li>פריסה לסביבת **<span dir="ltr">production</span>** ב-<span dir="ltr">GCP</span> <span dir="ltr">Cloud</span> <span dir="ltr">Run</span> **לאחר אישור ידני**.</p>
<p>לשם כך נצטרך מספר קבצי <span dir="ltr">workflow</span>.</p>
<p>**סודות <span dir="ltr">GitHub</span> נדרשים:**</p>
<li>`GCP_PROJECT_ID`: מזהה הפרויקט שלך ב-<span dir="ltr">GCP</span>.</li>
<li>`GCP_CREDENTIALS`: מפתח <span dir="ltr">JSON</span> של חשבון שירות <span dir="ltr">GCP</span> עם הרשאות פריסה ל-<span dir="ltr">Cloud</span> <span dir="ltr">Run</span> וגישה ל-<span dir="ltr">GHCR</span> (אם נדרש). בדרך כלל `GITHUB_TOKEN` מספיק לגישה ל-<span dir="ltr">GHCR</span> מ-<span dir="ltr">Actions</span>.</li>
<li>`GCP_REGION`: אזור עבור <span dir="ltr">Cloud</span> <span dir="ltr">Run</span> (לדוגמה, `europe-west1`).</li>
<h4>1. בנייה ופרסום תמונת <span dir="ltr">Docker</span> ב-<span dir="ltr">GHCR</span></h4>
<pre class="line-numbers"><code class="language-yaml">
# .github/workflows/build.yml
name: Build & Push to GHCR

on:
  push:
    branches: [main] # הפעל ב-push ל-main

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

      - name: Build Docker image
        # החלף את myapp בשם היישום שלך
        run: docker build -t ${{ secrets.DOCKER_USERNAME }}/myapp:latest .

      - name: Push Docker image
        run: docker push ${{ secrets.DOCKER_USERNAME }}/myapp:latest
</code></pre>
<li>`github.repository_owner`: בעל המאגר (שם המשתמש או הארגון שלך).</li>
<li>`github.event.repository.name`: שם המאגר.</li>
<li>`myapp`: שם היישום/התמונה שלך.</li>
<h4>2. פריסה אוטומטית ל-<span dir="ltr">Staging</span> (<span dir="ltr">GCP</span> <span dir="ltr">Cloud</span> <span dir="ltr">Run</span>)</h4>
<p>ה-<span dir="ltr">workflow</span> הזה יופעל אוטומטית לאחר השלמה מוצלחת של `build.yml`.</p>
<pre class="line-numbers"><code class="language-yaml">
# .github/workflows/deploy-staging.yml
name: Deploy to GCP Cloud Run (Staging)

on:
  workflow_run:
    workflows: ["Build & Push to GHCR"] # שם ה-workflow של הבנייה
    types:
      - completed

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    # הפעל רק אם ה-workflow של הבנייה הסתיים בהצלחה
    if: ${{ github.event.workflow_run.conclusion == 'success' }}

    # השתמש בסביבות GitHub עבור staging (אופציונלי, אך פרקטיקה טובה)
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }} # ה-URL יהיה זמין לאחר הפריסה

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
          service: 'myapp-staging' # שם שירות ה-staging שלך ב-Cloud Run
          region: '${{ secrets.GCP_REGION }}'
          # השתמש בתמונה שנשלחה ב-build.yml
          image: 'ghcr.io/${{ github.repository_owner }}/${{ github.event.repository.name }}/myapp:latest'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          flags: '--allow-unauthenticated --platform=managed' # אפשר גישה לא מאומתת לדוגמה
</code></pre>
<h4>3. פריסה ל-<span dir="ltr">Production</span> עם אישור ידני (<span dir="ltr">GCP</span> <span dir="ltr">Cloud</span> <span dir="ltr">Run</span>)</h4>
<p>ה-<span dir="ltr">workflow</span> הזה מופעל ידנית דרך <span dir="ltr">UI</span> ה-<span dir="ltr">GitHub</span> <span dir="ltr">Actions</span>.</p>
<pre class="line-numbers"><code class="language-yaml">
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
          # עבור production ניתן להוסיף --no-traffic ולאחר מכן להחליף תנועה בהדרגה
          # traffic:
          #   latest: true
          #   percent: 100
</code></pre>
<p>**נקודות חשובות ב-<span dir="ltr">pipeline</span> מתקדם זה:**</p>
<li>**<span dir="ltr">GitHub</span> <span dir="ltr">Container</span> <span dir="ltr">Registry</span> (<span dir="ltr">ghcr.io</span>):** אנו משתמשים בו לאחסון תמונות <span dir="ltr">Docker</span>. זה נוח מכיוון שהוא משולב היטב עם <span dir="ltr">GitHub</span> <span dir="ltr">Actions</span>.</li>
<li>**`workflow_run`:** מאפשר להפעיל <span dir="ltr">workflow</span> אחד (פריסת <span dir="ltr">staging</span>) עם השלמת <span dir="ltr">workflow</span> אחר (בנייה).</li>
<li>**`workflow_dispatch`:** מאפשר הפעלה ידנית של <span dir="ltr">workflow</span> (פריסת <span dir="ltr">production</span>), המספקת שליטה.</li>
<li>**<span dir="ltr">GitHub</span> <span dir="ltr">Environments</span>:** מאפשרים לך להגדיר כללי הגנה עבור <span dir="ltr">production</span> (לדוגמה, דרישת אישור ממבקרים ספציפיים) ולאחסן סודות ספציפיים לסביבה.</li>
<li>**<span dir="ltr">GCP</span> <span dir="ltr">Cloud</span> <span dir="ltr">Run</span>:** אפשרות <span dir="ltr">serverless</span> מצוינת להפעלת יישומים מבוססי קונטיינרים.</li>
<h3>🔐 אבטחה – זה חשוב!</h3>
<li>**השתמש בסודות <span dir="ltr">GitHub</span>:** לעולם אל תשמור אסימונים, סיסמאות, מפתחות <span dir="ltr">API</span> ישירות בקבצי <span dir="ltr">YAML</span>. השתמש ב-<span dir="ltr">Settings</span> -> <span dir="ltr">Secrets</span> <span dir="ltr">and</span> <span dir="ltr">variables</span> -> <span dir="ltr">Actions</span> במאגר שלך.</li>
<li>**הרשאות מינימליות:** עבור חשבונות שירות (לדוגמה, <span dir="ltr">GCP</span>), הענק רק את ההרשאות הנחוצות באמת לביצוע משימות <span dir="ltr">CI</span>/<span dir="ltr">CD</span>.</li>
<li>**בידוד סביבות:** <span dir="ltr">Staging</span> ו-<span dir="ltr">Production</span> צריכים להיות מבודדים ככל האפשר. פרויקטים/חשבונות שונים בספקי ענן – זו פרקטיקה טובה.</li>
<li>**הגנת ענפים:** הגדר הגנה עבור ענף `main` (או `master`) כך ש-<span dir="ltr">push</span> אליו יתאפשר רק באמצעות <span dir="ltr">Pull</span> <span dir="ltr">Request</span> עם בדיקות <span dir="ltr">CI</span> חובה.</li>
