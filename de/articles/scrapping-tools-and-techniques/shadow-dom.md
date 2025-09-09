### Shadow DOM - „DOM im DOM“

DOM ist eine Programmierschnittstelle (API) für Seiten-Code, die die Seite als baumartige Objektstruktur darstellt.

Jedes HTML-Element (z. B. `<p>`, `<div>`, `<img>`), jedes Attribut und jeder Textabschnitt ist ein separater „Knoten“
(node) in diesem Baum. Mit JavaScript können wir auf diese Knoten zugreifen, um die Seite dynamisch zu ändern: Text ändern, Stile hinzufügen, neue Elemente erstellen oder bestehende löschen. Im Wesentlichen ist DOM ein „lebendes“ Modell des Dokuments, mit dem Code interagiert.

Aber diese Offenheit hat auch eine Kehrseite. Wenn wir eine komplexe, wiederverwendbare Komponente erstellen (z. B. einen benutzerdefinierten Videoplayer oder ein Kalender-Widget), werden ihre interne Struktur und ihre Stile anfällig. CSS-Stile von der Hauptseite können versehentlich in die Komponente „eindringen“ und ihr Aussehen zerstören. Ähnlich kann der JavaScript-Code der Seite unbeabsichtigt interne Elemente der Komponente ändern und so ihre Logik stören.

Um dieses Problem zu lösen, gibt es das **Shadow DOM (Schatten-DOM)**.

Im Kern ist Shadow DOM **„DOM im DOM“**. Es ist ein versteckter Baum von Elementen, der an ein normales Element auf der Seite (einen „Host“) angehängt wird, aber vom Haupt-DOM isoliert ist. Es ermöglicht dem Entwickler, eine hermetische Grenze um die interne Struktur einer Komponente zu schaffen und sie so vor der Außenwelt zu schützen.

Shadow DOM ermöglicht es Ihnen, versteckte DOM-Bäume an Elemente im normalen DOM-Baum anzuhängen. Dieser Schattenbaum beginnt mit einem **Schatten-Root** (shadow root), unter dem beliebige Elemente wie im normalen DOM angehängt werden können.

Es gibt mehrere Begriffe im Zusammenhang mit Shadow DOM, die Sie kennen sollten:
![DOM](../../assets/shadow_dom/file.png)
*   **Schatten-Host (Shadow host):** Ein normaler DOM-Knoten, an den das Schatten-DOM angehängt ist.
*   **Schattenbaum (Shadow tree):** Der DOM-Baum innerhalb des Schatten-DOM.
*   **Schatten-Grenze (Shadow boundary):** Der Ort, an dem das Schatten-DOM endet und das normale DOM beginnt.
*   **Schatten-Root (Shadow root):** Der Wurzelknoten des Schattenbaums.

Sie können Knoten im Schatten-DOM genau wie normale Knoten beeinflussen. Der Unterschied besteht darin, dass kein Code innerhalb des Schatten-DOM etwas außerhalb davon beeinflussen kann, was eine zuverlässige Kapselung gewährleistet.

Bevor Shadow DOM für Webentwickler verfügbar wurde, verwendeten Browser es bereits, um die interne Struktur von Standardelementen zu kapseln. Zum Beispiel das `<video>`-Element mit Steuerelementen. Alles, was Sie im DOM sehen, ist das `<video>`-Tag, aber es enthält eine Reihe von Schaltflächen und anderen Steuerelementen in seinem Schatten-DOM.

#### Erstellen eines Shadow DOM

Sie können ein Schatten-DOM auf zwei Arten erstellen: imperativ mit JavaScript oder deklarativ direkt in HTML.

##### Imperativ mit JavaScript

Diese Methode eignet sich hervorragend für clientseitig gerenderte Anwendungen. Wir wählen ein Host-Element aus und rufen darauf die Methode `attachShadow()` auf.

```html
<!-- HTML-Markup -->
<div id="host"></div>
<span>Ich bin nicht im Schatten-DOM</span>
```

```javascript
// Host finden und Schatten-DOM daran anhängen
const host = document.querySelector("#host");
const shadow = host.attachShadow({ mode: "open" });

// Elemente im Schattenbaum erstellen und hinzufügen
const span = document.createElement("span");
span.textContent = "Ich bin im Schatten-DOM";
shadow.appendChild(span);
```

Das Ergebnis auf der Seite wird so aussehen:
> Ich bin im Schatten-DOM
> Ich bin nicht im Schatten-DOM

##### Deklarativ mit HTML

Für Anwendungen, bei denen das serverseitige Rendering wichtig ist, können Sie das Schatten-DOM deklarativ definieren, indem Sie das `<template>`-Element mit dem Attribut `shadowrootmode` verwenden.



```html
<div id="host">
  <template shadowrootmode="open">
    <p>Dieser Absatz befindet sich im Schatten-DOM.</p>
    <style>
      p { color: red; } /* Diese Stile werden isoliert */
    </style>
  </template>
</div>
```

Wenn der Browser diesen Code verarbeitet, erstellt er automatisch einen Schatten-Root für das `<div>` und platziert den Inhalt des `<template>`-Tags darin. Das `<template>`-Tag selbst verschwindet dabei aus dem Haupt-DOM-Baum.

#### Kapselung: Schutz vor JavaScript und CSS

Der Hauptvorteil von Shadow DOM ist die Isolation. Sehen wir uns an, wie das funktioniert.

##### Kapselung von JavaScript

Fügen wir einen Button hinzu, der versuchen wird, alle `<span>`-Elemente auf der Seite zu ändern.

```javascript
// ... Code zur Erstellung des Schatten-DOM ...

const upper = document.querySelector("#upper-button");
upper.addEventListener("click", () => {
  // Dieser Selektor sucht im gesamten Dokument
  const spans = document.querySelectorAll("span");
  for (const span of spans) {
    span.textContent = span.textContent.toUpperCase();
  }
});
```

Beim Klicken auf den Button ändert sich der Text nur bei dem `<span>`, der sich im Hauptdokument befindet. Das Element innerhalb des Schatten-DOM bleibt unberührt, da `document.querySelectorAll()` nicht über die Schatten-Grenze „hinausschauen“ kann.

##### Zugriff auf das Schatten-DOM: `shadowRoot`-Eigenschaft und Arbeiten mit Verschachtelung

Wenn wir `host.attachShadow({ mode: "open" })` aufrufen, erstellen wir ein Schatten-DOM im „offenen“ Modus. Das bedeutet, dass wir von außen über die Eigenschaft `host.shadowRoot` auf seinen Inhalt zugreifen können.

```javascript
// Spans nur innerhalb des Schattenbaums eines bestimmten Hosts finden
const spansInShadow = host.shadowRoot.querySelectorAll("span");
```

Wenn Sie `mode: „closed“` angeben, gibt die Eigenschaft `host.shadowRoot` `null` zurück, und der Zugriff auf den Schattenbaum von außen wird geschlossen. Dies ist kein strenger Sicherheitsmechanismus, sondern eher eine Konvention für Entwickler, dass die internen Abläufe der Komponente nicht berührt werden sollten.

**Arbeiten mit verschachtelten Schattenbäumen**

In komplexen Komponentenarchitekturen kann ein benutzerdefiniertes Element andere benutzerdefinierte Elemente enthalten, von denen jedes sein eigenes Shadow DOM hat. Um auf ein Element in einem tief verschachtelten Schattenbaum zuzugreifen, müssen Sie nacheinander jeden `shadowRoot` „durchlaufen“.

Betrachten Sie die folgende Struktur:
*   `<nmbrs-form>`-Komponente (Hauptformular).
*   Darin befindet sich ein `<div>`, und darin – eine `<nmbrs-button>`-Komponente (benutzerdefinierter Button).
*   Innerhalb von `<nmbrs-button>` befindet sich ein echter HTML-Button `<button>`.

Um von globalen Kontext aus auf diesen Button zuzugreifen, sieht der Pfad so aus:

```javascript
// 1. Root-Komponente im Hauptdokument finden
const formComponent = document.querySelector('nmbrs-form');

// 2. In den Schattenbaum eintreten
const shadowRoot1 = formComponent.shadowRoot;

// 3. Verschachtelte Button-Komponente finden
const buttonComponent = shadowRoot1.querySelector('div div.btn-container nmbrs-button');

// 4. In den Schattenbaum dieser Komponente eintreten
const shadowRoot2 = buttonComponent.shadowRoot;

// 5. Und erst jetzt das endgültige Element finden
const finalButton = shadowRoot2.querySelector('button#button');
```

In einer einzigen Aufrufkette sieht es so aus:

```javascript
const button = document.querySelector('nmbrs-form').shadowRoot
                      .querySelector('div div.btn-container nmbrs-button').shadowRoot
                      .querySelector('button#button');
```

Eine so lange Kette demonstriert deutlich die Leistungsfähigkeit der Kapselung: Um an interne Details zu gelangen, müssen Sie explizit jede „Grenze“ durchlaufen. Dies macht den Code vorhersehbarer und schützt Komponenten vor versehentlichen Änderungen.

##### Kapselung von CSS

Auf der Hauptseite definierte Stile wirken sich nicht auf Elemente innerhalb des Schatten-DOM aus.

```css
/* Dieser Stil gilt nur für Spans im Hauptdokument */
span {
  color: blue;
  border: 1px solid black;
}
```

Das `<span>`-Element innerhalb des Schattenbaums erhält diese Stile nicht. Dies löst das enorme Problem versehentlicher Überschneidungen und CSS-Konflikte.

#### Anwenden von Stilen innerhalb des Schatten-DOM

Stile, die innerhalb des Schattenbaums definiert sind, wirken sich wiederum nicht auf die Hauptseite aus. Es gibt zwei Hauptmethoden, sie hinzuzufügen.

##### 1. Konstruierbare Stylesheets (Constructable Stylesheets)

Diese Methode ermöglicht es Ihnen, ein `CSSStyleSheet`-Objekt in JavaScript zu erstellen und es auf einen oder mehrere Schattenbäume anzuwenden. Dies ist effizient, wenn Sie gemeinsame Stile für mehrere Komponenten haben.

```javascript
const sheet = new CSSStyleSheet();
sheet.replaceSync("span { color: red; border: 2px dotted black; }");

const shadow = host.attachShadow({ mode: "open" });
// Stylesheet auf den Schatten-Root anwenden
shadow.adoptedStyleSheets = [sheet];
```

##### 2. Hinzufügen eines `<style>`-Elements

Eine einfache und deklarative Methode besteht darin, das `<style>`-Tag direkt in den Schattenbaum zu platzieren (oft innerhalb von `<template>`).

```html
<template id="my-element">
  <style>
    span {
      color: red;
      border: 2px dotted black;
    }
  </style>
  <span>Ich bin im Schatten-DOM</span>
</template>
```

#### Shadow DOM und benutzerdefinierte Elemente: eine perfekte Kombination

Die volle Leistungsfähigkeit des Schatten-DOM zeigt sich bei der Erstellung von **benutzerdefinierten Elementen (Custom Elements)**. Ohne Kapselung wären sie unglaublich zerbrechlich.

Ein benutzerdefiniertes Element ist eine Klasse, die von `HTMLElement` erbt. In der Regel fungiert das Element selbst als Schatten-Host, und seine gesamte interne Struktur wird innerhalb des Schattenbaums erstellt.

Hier ist ein Beispiel für eine einfache `<filled-circle>`-Komponente:

```javascript
class FilledCircle extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" });

    // Interne Implementierung erstellen (z. B. SVG-Kreis)
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("r", "50");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    // Farbe aus dem Attribut des Hosts übernehmen
    circle.setAttribute("fill", this.getAttribute("color"));
    
    svg.appendChild(circle);
    shadow.appendChild(svg);
  }
}
customElements.define("filled-circle", FilledCircle);
```

Jetzt können wir es in HTML als normales Tag verwenden, ohne uns um seine interne Struktur kümmern zu müssen:

```html
<filled-circle color="blue"></filled-circle>
<filled-circle color="green"></filled-circle>
```

Jede dieser Komponenten wird vollständig gekapselt und vor externen Seiteneinflüssen geschützt.
