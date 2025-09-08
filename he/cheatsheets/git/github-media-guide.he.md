# מדריך מלא לעבודה עם קבצי מדיה ב-GitHub

## מבוא

GitHub תומך בסוגים שונים של קבצי מדיה ב-`README.md` ובמסמכי Markdown אחרים. הבנה כיצד לעבוד נכון עם מדיה תעזור ליצור תיעוד מושך ואינפורמטיבי יותר עבור הפרויקטים שלכם.

-----

## תמונות

### תחביר בסיסי

להוספת תמונות משתמשים בתחביר Markdown סטנדרטי.

```markdown
![טקסט אלטרנטיבי](נתיב/לתמונה.png)
![לוגו הפרויקט](assets/logo.png)
```

### תמונות עם קישורים

כדי להפוך תמונה ללחיצה, עטפו אותה בקישור Markdown.

```markdown
[![תיאור](image.png)](https://example.com)
```

### תמונות ממאגר

*   **נתיב יחסי:**
    זוהי הדרך האמינה ביותר אם הקובץ נמצא במאגר שלכם. הקישור יעבוד גם אם הפרויקט יועבר.
    ```markdown
    ![תרשים](docs/images/architecture.png)
    ```
*   **קישור ישיר:**
    להוספת תמונה באמצעות קישור ישיר לקובץ במאגר, השתמשו בדומיין `raw.githubusercontent.com`. זוהי השיטה המומלצת ביותר, מכיוון שהיא מספקת את הקובץ ישירות ללא ממשק GitHub.
    ```markdown
    # דרך raw.githubusercontent.com (מומלץ)
    ![תרשים](https://raw.githubusercontent.com/username/repo/main/docs/images/architecture.png)
    ```
    ניתן גם להשתמש בפרמטר `?raw=true` בכתובות URL של קבצים.
    ```markdown
    # קישור ישיר לקובץ במאגר
    ![תרשים](https://github.com/username/repo/blob/main/assets/images/architecture.png?raw=true)
    ```

### HTML לתמונות עם פרמטרים נוספים

אם אתם צריכים להתאים את הגודל, המרכוז או להוסיף כיתוב לתמונה, השתמשו בתג HTML `<img>`.

```html
<img src="image.png" alt="תיאור" width="300" height="200">

<div align="center">
  <img src="logo.png" alt="לוגו" width="200">
</div>

<figure>
  <img src="screenshot.png" alt="צילום מסך" width="600">
  <figcaption>איור 1: ממשק המשתמש הראשי של היישום</figcaption>
</figure>
```

-----

## וידאו

GitHub אינו תומך בהטמעה ישירה של וידאו בקבצי Markdown. עם זאת, קיימות שיטות מוכחות להצגתם.

### שיטה 1: העלאה דרך GitHub Issues/Releases (מומלץ)

שיטה זו היא האמינה ביותר, במיוחד עבור קבצים גדולים וקבצים עם שמות בקירילית, מכיוון ש-GitHub מייצר עבורם קישורים נכונים באופן אוטומטי.

**שלבים:**

1.  פתחו Issue חדש במאגר שלכם.
2.  גררו את קובץ הווידאו (.mp4, .mov, .webm, .avi) לשדה התגובה.
3.  GitHub יעלה את הקובץ וייצור קישור ישיר, שייראה בערך כך: `https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp4`.
4.  העתיקו קישור זה לשימוש בתג HTML `<video>`.

<!-- end list -->

```html
<video width="600" controls>
  <source src="https://user-images.githubusercontent.com/12345678/123456789-demo.mp4" type="video/mp4">
  הדפדפן שלך אינו תומך בהפעלת וידאו.
</video>
```

### שיטה 2: תצוגה מקדימה עם קישור לווידאו

אתם יכולים להשתמש בתמונה כתצוגה מקדימה, שתוביל להורדה או לצפייה בווידאו.

```markdown
[![הדגמת פעולה](assets/video-preview.jpg)](https://github.com/username/repo/raw/main/assets/demo.mp4)
*לחצו על התמונה לצפייה בווידאו*

**[⬇️ הורדת וידאו](https://github.com/username/repo/raw/main/assets/demo.mp4)** | **[🎬 צפייה בדפדפן](https://github.com/username/repo/blob/main/assets/demo.mp4)**
```

### שיטה 3: אינטגרציה עם YouTube

שיטה זו אידיאלית אם הווידאו שלכם כבר נמצא ב-YouTube.

```markdown
[![שם הווידאו](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

[![הווידאו שלי](custom-preview.png)](https://youtu.be/VIDEO_ID)
```

### שיטה 4: וידאו דרך GitHub Pages

צרו דף HTML עם וידאו בענף `gh-pages` וקשרו אליו מתוך קובץ ה-`README.md` שלכם.

```html
<!DOCTYPE html>
<html>
<head>
    <title>הדגמת וידאו</title>
</head>
<body>
    <video width="800" controls>
        <source src="demo.mp4" type="video/mp4">
    </video>
</body>
</html>
```

לאחר מכן ב-`README.md`:

```markdown
[📺 צפייה בווידאו](https://username.github.io/repo-name/video.html)
```

-----

## קבצי אודיו

GitHub אינו תומך בהטמעה ישירה של אודיו, אך אתם יכולים לספק קישורים להורדה או להשתמש בשירותים חיצוניים.

### קישור להורדה

```markdown
🎵 [הורדת קובץ אודיו](assets/audio/soundtrack.mp3)
```

### HTML5 audio (עובד באופן מוגבל)

שימוש ב-`<audio>` ב-Markdown עשוי לא לעבוד בכל הדפדפנים ובכל הפלטפורמות.

```html
<audio controls>
  <source src="https://user-images.githubusercontent.com/USER_ID/FILE_ID.mp3" type="audio/mpeg">
  הדפדפן שלך אינו תומך בהפעלת אודיו.
</audio>
```

### שירותים חיצוניים

השתמשו בתגים (badges) או בקישורים לשירותים חיצוניים כמו SoundCloud.

```markdown
[![SoundCloud](https://img.shields.io/badge/SoundCloud-Listen-orange)](https://soundcloud.com/your-track)
```

-----

## אנימציית GIF

קבצי GIF עובדים בדיוק כמו תמונות רגילות.

### יצירת GIF מווידאו

אתם יכולים להשתמש בכלי שורת פקודה, כגון **FFmpeg**, או בממירים מקוונים.

#### באמצעות FFmpeg:

```bash
# המרת וידאו ל-GIF
ffmpeg -i input.mp4 -vf "fps=10,scale=600:-1" -t 30 output.gif
```

#### ממירים מקוונים:

*   [EZGIF](https://ezgif.com/)
*   [CloudConvert](https://cloudconvert.com/)
*   [Convertio](https://convertio.co/)

### שימוש ב-GIF ב-README

```markdown
![הדגמה](demo.gif)

<div align="center">
  <img src="demo.gif" alt="הדגמת פעולה" width="600">
  <p><em>הדגמת הפונקציונליות העיקרית</em></p>
</div>
```

-----

## שיטות עבודה מומלצות

### ארגון קבצים

צרו תיקיות נפרדות למדיה כדי לשמור על סדר במאגר.

```
project/
├── README.md
├── assets/
│   ├── images/
│   │   ├── logo.png
│   │   └── screenshots/
│   ├── videos/
│   │   └── demo.mp4
│   └── gifs/
│       └── feature1.gif
```

### אופטימיזציית גדלים

*   **תמונות:** השתמשו בפורמטים עם דחיסה טובה (PNG, JPEG, WebP) ובכלים לאופטימיזציה (לדוגמה, TinyPNG).
*   **וידאו:** גודל מומלץ – עד **100 MB**. השתמשו ברזולוציה של 720p או 1080p.
*   **GIF:** גודל אופטימלי – עד **5 MB**.

### נגישות

*   ציינו תמיד `alt-text` עבור תמונות.
*   ספקו חלופות לקבצי מדיה. לדוגמה, קישור לווידאו עבור אלה שאינם יכולים לצפות ב-GIF.

-----

## טכניקות מתקדמות

### תמונות רספונסיביות

```html
<picture>
  <source media="(max-width: 600px)" srcset="mobile-image.png">
  <source media="(max-width: 1200px)" srcset="tablet-image.png">
  <img src="desktop-image.png" alt="תמונה רספונסיבית">
</picture>
```

### טעינה עצלה (Lazy Loading)

```html
<img src="image.png" alt="תיאור" loading="lazy" width="600">
```

### גלריית תמונות

```markdown
## צילומי מסך

<div align="center">
  <img src="screenshot1.png" width="250" alt="דף הבית">
  <img src="screenshot2.png" width="250" alt="הגדרות">
  <img src="screenshot3.png" width="250" alt="פרופיל">
</div>
```

### תגים (Badges) ואייקונים

```markdown
![GitHub stars](https://img.shields.io/github/stars/username/repo)
```

### אלמנטים אינטראקטיביים

השתמשו בתג `<details>` ליצירת בלוקים מתקפלים.

```markdown
<details>
<summary>📸 צפייה בצילומי מסך</summary>

![צילום מסך 1](screenshot1.png)
![צילום מסך 2](screenshot2.png)

</details>
```

-----

## פתרון בעיות

### וידאו לא מופעל

**בעיה:** תג הווידאו HTML אינו עובד עם קבצים מהמאגר.

**פתרון:** השתמשו בשיטת ההעלאה דרך GitHub Issues/Releases.

### תמונות לא מוצגות

**בעיה:** סוג קישור שגוי.
**פתרון:** ודאו שאתם משתמשים בקישור ישיר (`raw.githubusercontent.com`), ולא בקישור לדף הקובץ (`github.com/blob`).

```markdown
![שגוי](https://github.com/user/repo/blob/main/image.png)

![נכון](https://raw.githubusercontent.com/user/repo/main/image.png)
```

### קבצי מדיה גדולים מדי

**פתרונות:**

*   בצעו אופטימיזציה לתמונות ולווידאו.
*   השתמשו ב-**Git LFS** (Large File Storage) עבור קבצים גדולים.
*   אחסנו מדיה ב-CDN או השתמשו בשיטה עם Issues.

-----

### דוגמאות שימוש

### README עם סט מלא של מדיה

```markdown
# הפרויקט שלי

<div align="center">
  <img src="assets/logo.png" alt="לוגו" width="200">
  
  ![GitHub stars](https://img.shields.io/github/stars/username/repo)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
</div>

## 🎬 הדגמה

[![וידאו הדגמה](assets/video-preview.jpg)](https://user-images.githubusercontent.com/12345/demo.mp4)

## 📸 צילומי מסך

<details>
<summary>צפייה בצילומי מסך</summary>

![דף הבית](assets/screenshots/main.png)
![הגדרות](assets/screenshots/settings.png)

</details>

## 🎯 תכונות

![הדגמת תכונה](assets/gifs/feature-demo.gif)

- ✅ תכונה 1
- ✅ תכונה 2
- ✅ תכונה 3

## 🏗️ ארכיטקטורה

<div align="center">
  <img src="assets/diagrams/architecture.svg" alt="ארכיטקטורה" width="600">
</div>
```
