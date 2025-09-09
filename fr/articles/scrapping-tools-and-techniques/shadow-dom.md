### Shadow DOM - «DOM à l'intérieur du DOM»

Le DOM est une interface de programmation (API) pour le code de la page qui représente la page comme une structure arborescente d'objets.

Chaque élément HTML (par exemple, `<p>`, `<div>`, `<img>`), chaque attribut et chaque fragment de texte est un «nœud» séparé
(node) dans cet arbre. Avec JavaScript, nous pouvons accéder à ces nœuds pour modifier dynamiquement la page : changer le texte, ajouter des styles, créer de nouveaux éléments ou supprimer des éléments existants. Essentiellement, le DOM est un modèle «vivant» du document avec lequel le code interagit.

Mais cette ouverture a un inconvénient. Lorsque nous créons un composant complexe et réutilisable (par exemple, un lecteur vidéo personnalisé ou un widget de calendrier), sa structure interne et ses styles deviennent vulnérables. Les styles CSS de la page principale peuvent accidentellement «fuir» à l'intérieur du composant et casser son apparence. De même, le code JavaScript de la page peut modifier involontairement les éléments internes du composant, perturbant sa logique.

Pour résoudre ce problème, il existe le **Shadow DOM (DOM fantôme)**.

À la base, le Shadow DOM est un **«DOM à l'intérieur du DOM»**. C'est un arbre d'éléments caché qui est attaché à un élément normal de la page (appelé «hôte»), mais il est isolé du DOM principal. Il permet au développeur de créer une frontière étanche autour de la structure interne d'un composant, le protégeant du monde extérieur.

Le Shadow DOM vous permet d'attacher des arbres DOM cachés à des éléments dans l'arbre DOM normal. Cet arbre fantôme commence par une **racine fantôme** (shadow root), sous laquelle n'importe quel élément peut être attaché, tout comme dans le DOM normal.

Il existe plusieurs termes liés au Shadow DOM que vous devez connaître :
![DOM](../../assets/shadow_dom/file.png)
*   **Hôte fantôme (Shadow host) :** Un nœud DOM normal auquel le DOM fantôme est attaché.
*   **Arbre fantôme (Shadow tree) :** L'arbre DOM à l'intérieur du DOM fantôme.
*   **Frontière fantôme (Shadow boundary) :** L'endroit où le DOM fantôme se termine et le DOM normal commence.
*   **Racine fantôme (Shadow root) :** Le nœud racine de l'arbre fantôme.

Vous pouvez agir sur les nœuds du DOM fantôme exactement comme sur les nœuds normaux. La différence est qu'aucun code à l'intérieur du DOM fantôme ne peut affecter quoi que ce soit à l'extérieur, ce qui assure une encapsulation fiable.

Avant que le Shadow DOM ne soit disponible pour les développeurs web, les navigateurs l'utilisaient déjà pour encapsuler la structure interne des éléments standard. Par exemple, l'élément `<video>` avec des commandes. Tout ce que vous voyez dans le DOM est la balise `<video>`, mais elle contient un certain nombre de boutons et d'autres commandes à l'intérieur de son DOM fantôme.

#### Création d'un Shadow DOM

Vous pouvez créer un DOM fantôme de deux manières : de manière impérative avec JavaScript ou de manière déclarative directement en HTML.

##### Impérativement avec JavaScript

Cette méthode est idéale pour les applications rendues côté client. Nous sélectionnons un élément hôte et appelons la méthode `attachShadow()` dessus.

```html
<!-- Balisage HTML -->
<div id="host"></div>
<span>Je ne suis pas dans le DOM fantôme</span>
```

```javascript
// Trouver l'hôte et y attacher le DOM fantôme
const host = document.querySelector("#host");
const shadow = host.attachShadow({ mode: "open" });

// Créer et ajouter des éléments à l'arbre fantôme
const span = document.createElement("span");
span.textContent = "Je suis dans le DOM fantôme";
shadow.appendChild(span);
```

Le résultat sur la page ressemblera à ceci :
> Je suis dans le DOM fantôme
> Je ne suis pas dans le DOM fantôme

##### Déclarativement avec HTML

Pour les applications où le rendu côté serveur est important, vous pouvez définir le DOM fantôme de manière déclarative en utilisant l'élément `<template>` avec l'attribut `shadowrootmode`.



```html
<div id="host">
  <template shadowrootmode="open">
    <p>Ce paragraphe est à l'intérieur du DOM fantôme.</p>
    <style>
      p { color: red; } /* Ces styles seront isolés */
    </style>
  </template>
</div>
```

Lorsque le navigateur traitera ce code, il créera automatiquement une racine fantôme pour le `<div>` et y placera le contenu de la balise `<template>`. La balise `<template>` elle-même disparaîtra de l'arbre DOM principal.

#### Encapsulation : protection contre JavaScript et CSS

Le principal avantage du Shadow DOM est l'isolation. Voyons comment cela fonctionne.

##### Encapsulation de JavaScript

Ajoutons un bouton qui tentera de modifier tous les éléments `<span>` de la page.

```javascript
// ... code de création du DOM fantôme ...

const upper = document.querySelector("#upper-button");
upper.addEventListener("click", () => {
  // Ce sélecteur recherche dans tout le document
  const spans = document.querySelectorAll("span");
  for (const span of spans) {
    span.textContent = span.textContent.toUpperCase();
  }
});
```

Lorsque l'on clique sur le bouton, seul le `<span>` du document principal changera de texte. L'élément à l'intérieur du DOM fantôme restera intact, car `document.querySelectorAll()` ne peut pas «regarder» au-delà de la frontière fantôme.

##### Accès au DOM fantôme : propriété `shadowRoot` et travail avec l'imbrication

Lorsque nous appelons `host.attachShadow({ mode: "open" })`, nous créons un DOM fantôme en mode «ouvert». Cela signifie que nous pouvons accéder à son contenu depuis l'extérieur via la propriété `host.shadowRoot`.

```javascript
// Trouver les spans uniquement à l'intérieur de l'arbre fantôme d'un hôte spécifique
const spansInShadow = host.shadowRoot.querySelectorAll("span");
```

Si vous spécifiez `mode: "closed"`, la propriété `host.shadowRoot` renverra `null`, et l'accès à l'arbre fantôme depuis l'extérieur sera fermé. Ce n'est pas un mécanisme de sécurité strict, mais plutôt une convention pour les développeurs selon laquelle les éléments internes du composant ne doivent pas être modifiés.

**Travailler avec des arbres fantômes imbriqués**

Dans les architectures de composants complexes, un élément utilisateur peut contenir d'autres éléments utilisateur, chacun avec son propre Shadow DOM. Pour accéder à un élément dans un arbre fantôme profondément imbriqué, vous devrez «passer» séquentiellement par chaque `shadowRoot`.

Considérons la structure suivante :
*   Composant `<nmbrs-form>` (formulaire principal).
*   À l'intérieur se trouve un `<div>`, et à l'intérieur de celui-ci — un composant `<nmbrs-button>` (bouton personnalisé).
*   À l'intérieur de `<nmbrs-button>` se trouve un véritable bouton HTML `<button>`.

Pour accéder à ce bouton depuis le contexte global, le chemin ressemblera à ceci :

```javascript
// 1. Trouver le composant racine dans le document principal
const formComponent = document.querySelector('nmbrs-form');

// 2. «Entrer» dans son arbre fantôme
const shadowRoot1 = formComponent.shadowRoot;

// 3. Trouver le composant bouton imbriqué
const buttonComponent = shadowRoot1.querySelector('div div.btn-container nmbrs-button');

// 4. «Entrer» dans l'arbre fantôme de ce composant
const shadowRoot2 = buttonComponent.shadowRoot;

// 5. Et seulement maintenant trouver l'élément final
const finalButton = shadowRoot2.querySelector('button#button');
```

Dans une seule chaîne d'appels, cela ressemble à ceci :

```javascript
const button = document.querySelector('nmbrs-form').shadowRoot
                      .querySelector('div div.btn-container nmbrs-button').shadowRoot
                      .querySelector('button#button');
```

Une chaîne aussi longue démontre clairement la puissance de l'encapsulation : pour accéder aux détails internes, vous devez passer explicitement par chaque «frontière». Cela rend le code plus prévisible et protège les composants des modifications accidentelles.

##### Encapsulation CSS

Les styles définis sur la page principale n'affectent pas les éléments à l'intérieur du DOM fantôme.

```css
/* Ce style ne s'appliquera qu'aux spans du document principal */
span {
  color: blue;
  border: 1px solid black;
}
```

L'élément `<span>` à l'intérieur de l'arbre fantôme ne recevra pas ces styles. Cela résout l'énorme problème des chevauchements accidentels et des conflits CSS.

#### Application des styles à l'intérieur du DOM fantôme

Les styles définis à l'intérieur de l'arbre fantôme, à leur tour, n'affectent pas la page principale. Il existe deux méthodes principales pour les ajouter.

##### 1. Feuilles de style constructibles (Constructable Stylesheets)

Cette méthode permet de créer un objet `CSSStyleSheet` en JavaScript et de l'appliquer à un ou plusieurs arbres fantômes. C'est efficace si vous avez des styles communs pour plusieurs composants.

```javascript
const sheet = new CSSStyleSheet();
sheet.replaceSync("span { color: red; border: 2px dotted black; }");

const shadow = host.attachShadow({ mode: "open" });
// Appliquer la feuille de style à la racine fantôme
shadow.adoptedStyleSheets = [sheet];
```

##### 2. Ajout d'un élément `<style>`

Une méthode simple et déclarative consiste à placer la balise `<style>` directement à l'intérieur de l'arbre fantôme (souvent à l'intérieur de `<template>`).

```html
<template id="my-element">
  <style>
    span {
      color: red;
      border: 2px dotted black;
    }
  </style>
  <span>Je suis dans le DOM fantôme</span>
</template>
```

#### Shadow DOM et éléments personnalisés : une combinaison parfaite

Toute la puissance du DOM fantôme se révèle lors de la création d'**éléments personnalisés (Custom Elements)**. Sans encapsulation, ils seraient incroyablement fragiles.

Un élément personnalisé est une classe qui hérite de `HTMLElement`. En règle générale, l'élément lui-même agit comme un hôte fantôme, et toute sa structure interne est créée à l'intérieur de l'arbre fantôme.

Voici un exemple de composant simple `<filled-circle>` :

```javascript
class FilledCircle extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" });

    // Créer l'implémentation interne (par exemple, un cercle SVG)
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("r", "50");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    // La couleur est tirée de l'attribut de l'hôte
    circle.setAttribute("fill", this.getAttribute("color"));
    
    svg.appendChild(circle);
    shadow.appendChild(svg);
  }
}
customElements.define("filled-circle", FilledCircle);
```

Maintenant, nous pouvons l'utiliser en HTML comme une balise normale, sans nous soucier de sa structure interne :

```html
<filled-circle color="blue"></filled-circle>
<filled-circle color="green"></filled-circle>
```

Chacun de ces composants sera entièrement encapsulé et protégé de l'influence de la page externe.
