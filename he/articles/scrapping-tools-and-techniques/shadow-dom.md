### Shadow DOM - «DOM בתוך DOM»

DOM הוא ממשק תכנות יישומים (API) לקוד דף המייצג את הדף כמבנה דמוי עץ של אובייקטים.

כל אלמנט HTML (לדוגמה, `<p>`, `<div>`, `<img>`), כל תכונה וכל קטע טקסט הוא «צומת» נפרד
(node) בעץ זה. באמצעות JavaScript, אנו יכולים לגשת לצמתים אלה כדי לשנות את הדף באופן דינמי: לשנות טקסט, להוסיף סגנונות, ליצור אלמנטים חדשים או למחוק קיימים. במהותו, DOM הוא מודל «חי» של המסמך שאיתו הקוד מקיים אינטראקציה.

אבל לפתיחות זו יש גם צד שלילי. כאשר אנו יוצרים רכיב מורכב וניתן לשימוש חוזר (לדוגמה, נגן וידאו מותאם אישית או ווידג'ט לוח שנה), המבנה הפנימי והסגנונות שלו הופכים לפגיעים. סגנונות CSS מהדף הראשי יכולים בטעות «לזלוג» לתוך הרכיב ולשבור את המראה שלו. באופן דומה, קוד JavaScript של הדף יכול לשנות בטעות אלמנטים פנימיים של הרכיב, ובכך לשבש את הלוגיקה שלו.

כדי לפתור בעיה זו, קיים **Shadow DOM (DOM צללים)**.

בבסיסו, Shadow DOM הוא **«DOM בתוך DOM»**. זהו עץ נסתר של אלמנטים המחובר לאלמנט רגיל בדף (הנקרא «מארח»), אך הוא מבודד מה-DOM הראשי. הוא מאפשר למפתח ליצור גבול אטום סביב המבנה הפנימי של רכיב, ובכך להגן עליו מפני העולם החיצון.

Shadow DOM מאפשר לחבר עצי DOM נסתרים לאלמנטים בעץ ה-DOM הרגיל. עץ צללים זה מתחיל ב**שורש צללים** (shadow root), שתחתיו ניתן לחבר כל אלמנט בדיוק כמו ב-DOM הרגיל.

ישנם מספר מונחים הקשורים ל-Shadow DOM שכדאי להכיר:
![DOM](../../assets/shadow_dom/file.png)
*   **מארח צללים (Shadow host):** צומת DOM רגיל שאליו מחובר ה-DOM צללים.
*   **עץ צללים (Shadow tree):** עץ ה-DOM בתוך ה-DOM צללים.
*   **גבול צללים (Shadow boundary):** המקום שבו מסתיים ה-DOM צללים ומתחיל ה-DOM הרגיל.
*   **שורש צללים (Shadow root):** צומת השורש של עץ הצללים.

אתה יכול להשפיע על צמתים ב-DOM צללים בדיוק כמו על צמתים רגילים. ההבדל הוא שאף קוד בתוך ה-DOM צללים אינו יכול להשפיע על שום דבר מחוצה לו, מה שמספק אנקפסולציה אמינה.

לפני ש-Shadow DOM הפך זמין למפתחי אתרים, דפדפנים כבר השתמשו בו כדי לאגד את המבנה הפנימי של אלמנטים סטנדרטיים. לדוגמה, אלמנט `<video>` עם פקדים. כל מה שאתה רואה ב-DOM הוא תג `<video>`, אך הוא מכיל מספר כפתורים ופקדים אחרים בתוך ה-DOM צללים שלו.

#### יצירת Shadow DOM

ניתן ליצור Shadow DOM בשתי דרכים: באופן אימפרטיבי באמצעות JavaScript או באופן דקלרטיבי ישירות ב-HTML.

##### באופן אימפרטיבי באמצעות JavaScript

שיטה זו מצוינת עבור יישומים המרונדרים בצד הלקוח. אנו בוחרים אלמנט מארח וקוראים לו את המתודה `attachShadow()`.

```html
<!-- סימון HTML -->
<div id="host"></div>
<span>אני לא ב-DOM צללים</span>
```

```javascript
// מצא את המארח וצרף אליו את ה-DOM צללים
const host = document.querySelector("#host");
const shadow = host.attachShadow({ mode: "open" });

// צור והוסף אלמנטים לעץ הצללים
const span = document.createElement("span");
span.textContent = "אני נמצא ב-DOM צללים";
shadow.appendChild(span);
```

התוצאה בדף תיראה כך:
> אני נמצא ב-DOM צללים
> אני לא נמצא ב-DOM צללים

##### באופן דקלרטיבי באמצעות HTML

עבור יישומים שבהם רינדור בצד השרת חשוב, ניתן להגדיר את ה-DOM צללים באופן דקלרטיבי, באמצעות אלמנט `<template>` עם התכונה `shadowrootmode`.



```html
<div id="host">
  <template shadowrootmode="open">
    <p>פסקה זו נמצאת בתוך ה-DOM צללים.</p>
    <style>
      p { color: red; } /* סגנונות אלה יהיו מבודדים */
    </style>
  </template>
</div>
```

כאשר הדפדפן יעבד קוד זה, הוא ייצור אוטומטית שורש צללים עבור ה-`<div>` וימקם בתוכו את תוכן תגית `<template>`. תגית `<template>` עצמה תיעלם מעץ ה-DOM הראשי.

#### אנקפסולציה: הגנה מפני JavaScript ו-CSS

היתרון העיקרי של Shadow DOM הוא בידוד. בואו נראה איך זה עובד.

##### אנקפסולציה מ-JavaScript

נוסיף כפתור שינסה לשנות את כל אלמנטי ה-`<span>` בדף.

```javascript
// ... קוד יצירת ה-DOM צללים ...

const upper = document.querySelector("#upper-button");
upper.addEventListener("click", () => {
  // סלקטור זה מחפש בכל המסמך
  const spans = document.querySelectorAll("span");
  for (const span of spans) {
    span.textContent = span.textContent.toUpperCase();
  }
});
```

בלחיצה על הכפתור, הטקסט ישתנה רק ב-`<span>` שנמצא במסמך הראשי. האלמנט בתוך ה-DOM צללים יישאר ללא שינוי, מכיוון ש-`document.querySelectorAll()` אינו יכול «להציץ» מעבר לגבול הצללים.

##### גישה ל-DOM צללים: מאפיין `shadowRoot` ועבודה עם קינון

כאשר אנו קוראים ל-`host.attachShadow({ mode: "open" })`, אנו יוצרים DOM צללים במצב "פתוח". המשמעות היא שנוכל לגשת לתוכן שלו מבחוץ באמצעות המאפיין `host.shadowRoot`.

```javascript
// מצא spans רק בתוך עץ הצללים של מארח ספציפי
const spansInShadow = host.shadowRoot.querySelectorAll("span");
```

אם תציין `mode: "closed"`, המאפיין `host.shadowRoot` יחזיר `null`, והגישה לעץ הצללים מבחוץ תיחסם. זהו אינו מנגנון אבטחה קפדני, אלא יותר הסכם למפתחים שאין לגעת בחלקים הפנימיים של הרכיב.

**עבודה עם עצי צללים מקוננים**

בארכיטקטורות רכיבים מורכבות, אלמנט משתמש אחד יכול להכיל בתוכו אלמנטים משתמשים אחרים, שלכל אחד מהם Shadow DOM משלו. כדי להגיע לאלמנט בעץ צללים מקונן עמוק, יהיה צורך «לעבור» ברצף דרך כל `shadowRoot`.

נציג מבנה כזה:
*   רכיב `<nmbrs-form>` (טופס ראשי).
*   בתוכו נמצא `<div>`, ובו — רכיב `<nmbrs-button>` (כפתור מותאם אישית).
*   בתוך `<nmbrs-button>` נמצא כפתור HTML אמיתי `<button>`.

כדי לגשת לכפתור זה מהקשר הגלובלי, הנתיב ייראה כך:

```javascript
// 1. מצא את רכיב השורש במסמך הראשי
const formComponent = document.querySelector('nmbrs-form');

// 2. «היכנס» לעץ הצללים שלו
const shadowRoot1 = formComponent.shadowRoot;

// 3. מצא את רכיב הכפתור המקונן
const buttonComponent = shadowRoot1.querySelector('div div.btn-container nmbrs-button');

// 4. «היכנס» לעץ הצללים של רכיב זה
const shadowRoot2 = buttonComponent.shadowRoot;

// 5. ורק עכשיו מצא את האלמנט הסופי
const finalButton = shadowRoot2.querySelector('button#button');
```

בצורה של שרשרת קריאות אחת, זה נראה כך:

```javascript
const button = document.querySelector('nmbrs-form').shadowRoot
                      .querySelector('div div.btn-container nmbrs-button').shadowRoot
                      .querySelector('button#button');
```

שרשרת כה ארוכה מדגימה בבירור את עוצמת האנקפסולציה: כדי להגיע לפרטים פנימיים, יש לעבור במפורש דרך כל «גבול». זה הופך את הקוד לצפוי יותר ומגן על רכיבים מפני שינויים מקריים.

##### אנקפסולציה מ-CSS

סגנונות המוגדרים בדף הראשי אינם משפיעים על אלמנטים בתוך ה-DOM צללים.

```css
/* סגנון זה יחול רק על spans במסמך הראשי */
span {
  color: blue;
  border: 1px solid black;
}
```

האלמנט `<span>` בתוך עץ הצללים לא יקבל סגנונות אלה. זה פותר בעיה ענקית של חפיפות מקריות וקונפליקטים ב-CSS.

#### החלת סגנונות בתוך ה-DOM צללים

סגנונות המוגדרים בתוך עץ הצללים, בתורם, אינם משפיעים על הדף הראשי. ישנן שתי דרכים עיקריות להוסיף אותם.

##### 1. גיליונות סגנונות ניתנים לבנייה (Constructable Stylesheets)

שיטה זו מאפשרת ליצור אובייקט `CSSStyleSheet` ב-JavaScript ולהחיל אותו על עץ צללים אחד או יותר. זה יעיל אם יש לך סגנונות משותפים למספר רכיבים.

```javascript
const sheet = new CSSStyleSheet();
sheet.replaceSync("span { color: red; border: 2px dotted black; }");

const shadow = host.attachShadow({ mode: "open" });
// החל את גיליון הסגנונות על שורש הצללים
shadow.adoptedStyleSheets = [sheet];
```

##### 2. הוספת אלמנט `<style>`

דרך פשוטה ודקלרטיבית — למקם את תגית `<style>` ישירות בתוך עץ הצללים (לרוב בתוך `<template>`).

```html
<template id="my-element">
  <style>
    span {
      color: red;
      border: 2px dotted black;
    }
  </style>
  <span>אני ב-DOM צללים</span>
</template>
```

#### Shadow DOM ואלמנטים מותאמים אישית: שילוב מושלם

כל עוצמתו של ה-DOM צללים מתגלה בעת יצירת **אלמנטים מותאמים אישית (Custom Elements)**. ללא אנקפסולציה, הם היו שבירים להפליא.

אלמנט מותאם אישית הוא מחלקה היורשת מ-`HTMLElement`. ככלל, האלמנט עצמו משמש כמארח צללים, וכל המבנה הפנימי שלו נוצר בתוך עץ הצללים.

הנה דוגמה לרכיב פשוט `<filled-circle>`:

```javascript
class FilledCircle extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" });

    // צור יישום פנימי (לדוגמה, עיגול SVG)
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("r", "50");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    // צבע נלקח מתכונת המארח
    circle.setAttribute("fill", this.getAttribute("color"));
    
    svg.appendChild(circle);
    shadow.appendChild(svg);
  }
}
customElements.define("filled-circle", FilledCircle);
```

כעת נוכל להשתמש בו ב-HTML כתג רגיל, מבלי לדאוג למבנה הפנימי שלו:

```html
<filled-circle color="blue"></filled-circle>
<filled-circle color="green"></filled-circle>
```

כל אחד מהרכיבים הללו יהיה ארוז לחלוטין ומוגן מפני השפעת דף חיצוני.
