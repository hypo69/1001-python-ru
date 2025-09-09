### Shadow DOM - «DOM inside DOM»

DOM is a programming interface (API) for page code that represents the page as a tree-like structure of objects.

Each HTML element (e.g., `<p>`, `<div>`, `<img>`), each attribute, and each piece of text is a separate "node"
(node) in this tree. With JavaScript, we can access these nodes to dynamically change the page: change text, add styles, create new elements, or delete existing ones. In essence, DOM is a "live" model of the document with which code interacts.

But this openness has a downside. When we create a complex, reusable component (e.g., a custom video player or calendar widget), its internal structure and styles become vulnerable. CSS styles from the main page can accidentally "leak" inside the component and break its appearance. Similarly, the page's JavaScript code can unintentionally modify the component's internal elements, disrupting its logic.

To solve this problem, **Shadow DOM** exists.

At its core, Shadow DOM is **"DOM inside DOM"**. It is a hidden tree of elements that is attached to a regular element on the page (called a "host"), but it is isolated from the main DOM. It allows the developer to create a sealed boundary around the internal structure of a component, protecting it from the outside world.

Shadow DOM allows you to attach hidden DOM trees to elements in the regular DOM tree. This shadow tree starts with a **shadow root**, under which any elements can be attached just like in the regular DOM.

There are several terms related to Shadow DOM that you should know:
![DOM](../../assets/shadow_dom/file.png)
*   **Shadow host:** A regular DOM node to which the shadow DOM is attached.
*   **Shadow tree:** The DOM tree inside the shadow DOM.
*   **Shadow boundary:** The place where the shadow DOM ends and the regular DOM begins.
*   **Shadow root:** The root node of the shadow tree.

You can affect nodes in the shadow DOM just like regular nodes. The difference is that no code inside the shadow DOM can affect anything outside of it, which provides reliable encapsulation.

Before Shadow DOM became available to web developers, browsers already used it to encapsulate the internal structure of standard elements. For example, the `<video>` element with controls. All you see in the DOM is the `<video>` tag, but it contains a number of buttons and other controls inside its shadow DOM.

#### Creating a Shadow DOM

You can create a shadow DOM in two ways: imperatively with JavaScript or declaratively directly in HTML.

##### Imperatively with JavaScript

This method is great for client-side rendered applications. We select a host element and call the `attachShadow()` method on it.

```html
<!-- HTML markup -->
<div id="host"></div>
<span>I am not in the shadow DOM</span>
```

```javascript
// Find the host and attach the shadow DOM to it
const host = document.querySelector("#host");
const shadow = host.attachShadow({ mode: "open" });

// Create and add elements to the shadow tree
const span = document.createElement("span");
span.textContent = "I am in the shadow DOM";
shadow.appendChild(span);
```

The result on the page will look like this:
> I am in the shadow DOM
> I am not in the shadow DOM

##### Declaratively with HTML

For applications where server-side rendering is important, you can define the shadow DOM declaratively using the `<template>` element with the `shadowrootmode` attribute.



```html
<div id="host">
  <template shadowrootmode="open">
    <p>This paragraph is inside the shadow DOM.</p>
    <style>
      p { color: red; } /* These styles will be isolated */
    </style>
  </template>
</div>
```

When the browser processes this code, it will automatically create a shadow root for the `<div>` and place the contents of the `<template>` tag inside it. The `<template>` tag itself will disappear from the main DOM tree.

#### Encapsulation: protection from JavaScript and CSS

 The main advantage of Shadow DOM is isolation. Let's see how it works.

##### Encapsulation from JavaScript

Add a button that will try to change all `<span>` elements on the page.

```javascript
// ... shadow DOM creation code ...

const upper = document.querySelector("#upper-button");
upper.addEventListener("click", () => {
  // This selector searches the entire document
  const spans = document.querySelectorAll("span");
  for (const span of spans) {
    span.textContent = span.textContent.toUpperCase();
  }
});
```

When the button is clicked, only the `<span>` in the main document will change its text. The element inside the shadow DOM will remain untouched because `document.querySelectorAll()` cannot "look" beyond the shadow boundary.

##### Accessing the shadow DOM: `shadowRoot` property and working with nesting

When we call `host.attachShadow({ mode: "open" })`, we create a shadow DOM in "open" mode. This means that we can access its content from outside through the `host.shadowRoot` property.

```javascript
// Find spans only within the shadow tree of a specific host
const spansInShadow = host.shadowRoot.querySelectorAll("span");
```

If you specify `mode: "closed"`, the `host.shadowRoot` property will return `null`, and access to the shadow tree from outside will be closed. This is not a strict security mechanism, but rather a convention for developers that the internal workings of the component should not be touched.

**Working with nested shadow trees**

In complex component architectures, one custom element may contain other custom elements, each with its own Shadow DOM. To access an element in a deeply nested shadow tree, you will have to sequentially "pass through" each `shadowRoot`.

Consider the following structure:
*   `<nmbrs-form>` component (main form).
*   Inside it is a `<div>`, and inside that is an `<nmbrs-button>` component (custom button).
*   Inside `<nmbrs-button>` is a real HTML button `<button>`.

To access this button from the global context, the path will look like this:

```javascript
// 1. Find the root component in the main document
const formComponent = document.querySelector('nmbrs-form');

// 2. "Enter" its shadow tree
const shadowRoot1 = formComponent.shadowRoot;

// 3. Find the nested button component
const buttonComponent = shadowRoot1.querySelector('div div.btn-container nmbrs-button');

// 4. "Enter" the shadow tree of this component
const shadowRoot2 = buttonComponent.shadowRoot;

// 5. And only now find the final element
const finalButton = shadowRoot2.querySelector('button#button');
```

In a single chain of calls, it looks like this:

```javascript
const button = document.querySelector('nmbrs-form').shadowRoot
                      .querySelector('div div.btn-container nmbrs-button').shadowRoot
                      .querySelector('button#button');
```

Such a long chain clearly demonstrates the power of encapsulation: to get to internal details, you need to explicitly pass through each "boundary." This makes the code more predictable and protects components from accidental changes.

##### Encapsulation from CSS

Styles defined on the main page do not affect elements inside the shadow DOM.

```css
/* This style will only apply to spans in the main document */
span {
  color: blue;
  border: 1px solid black;
}
```

The `<span>` element inside the shadow tree will not receive these styles. This solves the huge problem of accidental overlaps and CSS conflicts.

#### Applying styles inside the shadow DOM

Styles defined inside the shadow tree, in turn, do not affect the main page. There are two main ways to add them.

##### 1. Constructable Stylesheets

This method allows you to create a `CSSStyleSheet` object in JavaScript and apply it to one or more shadow trees. This is efficient if you have common styles for multiple components.

```javascript
const sheet = new CSSStyleSheet();
sheet.replaceSync("span { color: red; border: 2px dotted black; }");

const shadow = host.attachShadow({ mode: "open" });
// Apply the stylesheet to the shadow root
shadow.adoptedStyleSheets = [sheet];
```

##### 2. Adding a `<style>` element

A simple and declarative way is to place the `<style>` tag directly inside the shadow tree (often inside `<template>`).

```html
<template id="my-element">
  <style>
    span {
      color: red;
      border: 2px dotted black;
    }
  </style>
  <span>I am in the shadow DOM</span>
</template>
```

#### Shadow DOM and custom elements: a perfect match

All the power of the shadow DOM is revealed when creating **Custom Elements**. Without encapsulation, they would be incredibly fragile.

A custom element is a class that inherits from `HTMLElement`. As a rule, the element itself acts as a shadow host, and its entire internal structure is created within the shadow tree.

Here is an example of a simple `<filled-circle>` component:

```javascript
class FilledCircle extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" });

    // Create internal implementation (e.g., SVG circle)
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("r", "50");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    // Get color from the host's attribute
    circle.setAttribute("fill", this.getAttribute("color"));
    
    svg.appendChild(circle);
    shadow.appendChild(svg);
  }
}
customElements.define("filled-circle", FilledCircle);
```

Now we can use it in HTML as a regular tag, without worrying about its internal structure:

```html
<filled-circle color="blue"></filled-circle>
<filled-circle color="green"></filled-circle>
```

Each of these components will be fully encapsulated and protected from external page influence.
