### Shadow DOM - «DOM all'interno del DOM»

Il DOM è un'interfaccia di programmazione (API) per il codice della pagina che rappresenta la pagina come una struttura ad albero di oggetti.

Ogni elemento HTML (ad esempio, `<p>`, `<div>`, `<img>`), ogni attributo e ogni frammento di testo è un «nodo» separato
(node) in questo albero. Con JavaScript, possiamo accedere a questi nodi per modificare dinamicamente la pagina: cambiare il testo, aggiungere stili, creare nuovi elementi o eliminare quelli esistenti. In sostanza, il DOM è un modello «vivo» del documento con cui il codice interagisce.

Ma questa apertura ha anche un lato negativo. Quando creiamo un componente complesso e riutilizzabile (ad esempio, un lettore video personalizzato o un widget calendario), la sua struttura interna e i suoi stili diventano vulnerabili. Gli stili CSS dalla pagina principale possono accidentalmente «trapelare» all'interno del componente e rovinarne l'aspetto. Allo stesso modo, il codice JavaScript della pagina può modificare involontariamente gli elementi interni del componente, interrompendone la logica.

Per risolvere questo problema, esiste lo **Shadow DOM (DOM ombra)**.

Nella sua essenza, lo Shadow DOM è **«DOM all'interno del DOM»**. È un albero di elementi nascosto che è attaccato a un elemento normale della pagina (chiamato «host»), ma è isolato dal DOM principale. Permette allo sviluppatore di creare un confine ermetico attorno alla struttura interna di un componente, proteggendolo dal mondo esterno.

Lo Shadow DOM consente di allegare alberi DOM nascosti agli elementi nell'albero DOM normale. Questo albero ombra inizia con una **radice ombra** (shadow root), sotto la quale è possibile allegare qualsiasi elemento proprio come nel DOM normale.

Ci sono diversi termini relativi allo Shadow DOM che dovresti conoscere:
![DOM](../../assets/shadow_dom/file.png)
*   **Host ombra (Shadow host):** Un nodo DOM normale a cui è attaccato lo Shadow DOM.
*   **Albero ombra (Shadow tree):** L'albero DOM all'interno dello Shadow DOM.
*   **Confine ombra (Shadow boundary):** Il punto in cui termina lo Shadow DOM e inizia il DOM normale.
*   **Radice ombra (Shadow root):** Il nodo radice dell'albero ombra.

Puoi influenzare i nodi nello Shadow DOM esattamente come i nodi normali. La differenza è che nessun codice all'interno dello Shadow DOM può influenzare qualcosa al di fuori di esso, il che fornisce un'incapsulamento affidabile.

Prima che lo Shadow DOM diventasse disponibile per gli sviluppatori web, i browser lo usavano già per incapsulare la struttura interna degli elementi standard. Ad esempio, l'elemento `<video>` con i controlli. Tutto ciò che vedi nel DOM è il tag `<video>`, ma contiene una serie di pulsanti e altri controlli all'interno del suo Shadow DOM.

#### Creazione di uno Shadow DOM

Puoi creare uno Shadow DOM in due modi: imperativamente con JavaScript o dichiarativamente direttamente in HTML.

##### Imperativamente con JavaScript

Questo metodo è ottimo per le applicazioni renderizzate lato client. Selezioniamo un elemento host e chiamiamo il metodo `attachShadow()` su di esso.

```html
<!-- Markup HTML -->
<div id="host"></div>
<span>Non sono nello Shadow DOM</span>
```

```javascript
// Trova l'host e allega lo Shadow DOM ad esso
const host = document.querySelector("#host");
const shadow = host.attachShadow({ mode: "open" });

// Crea e aggiungi elementi all'albero ombra
const span = document.createElement("span");
span.textContent = "Sono nello Shadow DOM";
shadow.appendChild(span);
```

Il risultato sulla pagina sarà simile a questo:
> Sono nello Shadow DOM
> Non sono nello Shadow DOM

##### Dichiarativamente con HTML

Per le applicazioni in cui il rendering lato server è importante, puoi definire lo Shadow DOM in modo dichiarativo utilizzando l'elemento `<template>` con l'attributo `shadowrootmode`.



```html
<div id="host">
  <template shadowrootmode="open">
    <p>Questo paragrafo è all'interno dello Shadow DOM.</p>
    <style>
      p { color: red; } /* Questi stili saranno isolati */
    </style>
  </template>
</div>
```

Quando il browser elaborerà questo codice, creerà automaticamente una radice ombra per il `<div>` e vi inserirà il contenuto del tag `<template>`. Il tag `<template>` stesso scomparirà dall'albero DOM principale.

#### Incapsulamento: protezione da JavaScript e CSS

Il principale vantaggio dello Shadow DOM è l'isolamento. Vediamo come funziona.

##### Incapsulamento da JavaScript

Aggiungiamo un pulsante che cercherà di modificare tutti gli elementi `<span>` sulla pagina.

```javascript
// ... codice di creazione dello Shadow DOM ...

const upper = document.querySelector("#upper-button");
upper.addEventListener("click", () => {
  // Questo selettore cerca nell'intero documento
  const spans = document.querySelectorAll("span");
  for (const span of spans) {
    span.textContent = span.textContent.toUpperCase();
  }
});
```

Quando si fa clic sul pulsante, solo lo `<span>` nel documento principale cambierà il suo testo. L'elemento all'interno dello Shadow DOM rimarrà intatto perché `document.querySelectorAll()` non può "guardare" oltre il confine dell'ombra.

##### Accesso allo Shadow DOM: proprietà `shadowRoot` e lavoro con l'annidamento

Quando chiamiamo `host.attachShadow({ mode: "open" })`, creiamo uno Shadow DOM in modalità "aperta". Ciò significa che possiamo accedere al suo contenuto dall'esterno tramite la proprietà `host.shadowRoot`.

```javascript
// Trova gli span solo all'interno dell'albero ombra di un host specifico
const spansInShadow = host.shadowRoot.querySelectorAll("span");
```

Se si specifica `mode: "closed"`, la proprietà `host.shadowRoot` restituirà `null`, e l'accesso all'albero ombra dall'esterno sarà chiuso. Questo non è un meccanismo di sicurezza rigoroso, ma piuttosto una convenzione per gli sviluppatori che le parti interne del componente non devono essere toccate.

**Lavorare con alberi ombra annidati**

Nelle architetture di componenti complesse, un elemento personalizzato può contenere altri elementi personalizzati, ognuno con il proprio Shadow DOM. Per accedere a un elemento in un albero ombra profondamente annidato, dovrai "passare" sequenzialmente attraverso ogni `shadowRoot`.

Consideriamo la seguente struttura:
*   Componente `<nmbrs-form>` (modulo principale).
*   Al suo interno c'è un `<div>`, e al suo interno — un componente `<nmbrs-button>` (pulsante personalizzato).
*   All'interno di `<nmbrs-button>` c'è un vero pulsante HTML `<button>`.

Per accedere a questo pulsante dal contesto globale, il percorso sarà simile a questo:

```javascript
// 1. Trova il componente radice nel documento principale
const formComponent = document.querySelector('nmbrs-form');

// 2. "Entra" nel suo albero ombra
const shadowRoot1 = formComponent.shadowRoot;

// 3. Trova il componente pulsante annidato
const buttonComponent = shadowRoot1.querySelector('div div.btn-container nmbrs-button');

// 4. "Entra" nell'albero ombra di questo componente
const shadowRoot2 = buttonComponent.shadowRoot;

// 5. E solo ora trova l'elemento finale
const finalButton = shadowRoot2.querySelector('button#button');
```

In una singola catena di chiamate, appare così:

```javascript
const button = document.querySelector('nmbrs-form').shadowRoot
                      .querySelector('div div.btn-container nmbrs-button').shadowRoot
                      .querySelector('button#button');
```

Una catena così lunga dimostra chiaramente la potenza dell'incapsulamento: per accedere ai dettagli interni, è necessario passare esplicitamente attraverso ogni "confine". Questo rende il codice più prevedibile e protegge i componenti da modifiche accidentali.

##### Incapsulamento da CSS

Gli stili definiti sulla pagina principale non influenzano gli elementi all'interno dello Shadow DOM.

```css
/* Questo stile si applicherà solo agli span nel documento principale */
span {
  color: blue;
  border: 1px solid black;
}
```

L'elemento `<span>` all'interno dell'albero ombra non riceverà questi stili. Questo risolve l'enorme problema di sovrapposizioni accidentali e conflitti CSS.

#### Applicazione degli stili all'interno dello Shadow DOM

Gli stili definiti all'interno dell'albero ombra, a loro volta, non influenzano la pagina principale. Ci sono due modi principali per aggiungerli.

##### 1. Fogli di stile costruibili (Constructable Stylesheets)

Questo metodo consente di creare un oggetto `CSSStyleSheet` in JavaScript e applicarlo a uno o più alberi ombra. Questo è efficiente se si hanno stili comuni per più componenti.

```javascript
const sheet = new CSSStyleSheet();
sheet.replaceSync("span { color: red; border: 2px dotted black; }");

const shadow = host.attachShadow({ mode: "open" });
// Applica il foglio di stile alla radice ombra
shadow.adoptedStyleSheets = [sheet];
```

##### 2. Aggiunta di un elemento `<style>`

Un modo semplice e dichiarativo è posizionare il tag `<style>` direttamente all'interno dell'albero ombra (spesso all'interno di `<template>`).

```html
<template id="my-element">
  <style>
    span {
      color: red;
      border: 2px dotted black;
    }
  </style>
  <span>Sono nello Shadow DOM</span>
</template>
```

#### Shadow DOM ed elementi personalizzati: una combinazione perfetta

Tutta la potenza dello Shadow DOM si rivela quando si creano **elementi personalizzati (Custom Elements)**. Senza incapsulamento, sarebbero incredibilmente fragili.

Un elemento personalizzato è una classe che eredita da `HTMLElement`. Di norma, l'elemento stesso agisce come host ombra, e tutta la sua struttura interna viene creata all'interno dell'albero ombra.

Ecco un esempio di un semplice componente `<filled-circle>`:

```javascript
class FilledCircle extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" });

    // Crea l'implementazione interna (ad esempio, un cerchio SVG)
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("r", "50");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    // Il colore viene preso dall'attributo dell'host
    circle.setAttribute("fill", this.getAttribute("color"));
    
    svg.appendChild(circle);
    shadow.appendChild(svg);
  }
}
customElements.define("filled-circle", FilledCircle);
```

Ora possiamo usarlo in HTML come un normale tag, senza preoccuparci della sua struttura interna:

```html
<filled-circle color="blue"></filled-circle>
<filled-circle color="green"></filled-circle>
```

Ciascuno di questi componenti sarà completamente incapsulato e protetto dall'influenza della pagina esterna.
