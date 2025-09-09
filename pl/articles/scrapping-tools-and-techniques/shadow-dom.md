### Shadow DOM - «DOM wewnątrz DOM»

DOM to interfejs programistyczny (API) dla kodu strony, który reprezentuje stronę jako drzewiastą strukturę obiektów.

Każdy element HTML (np. `<p>`, `<div>`, `<img>`), każdy atrybut i każdy fragment tekstu jest osobnym „węzłem”
(node) w tym drzewie. Za pomocą JavaScriptu możemy odwoływać się do tych węzłów, aby dynamicznie zmieniać stronę: zmieniać tekst, dodawać style, tworzyć nowe elementy lub usuwać istniejące. Zasadniczo DOM to „żywy” model dokumentu, z którym kod wchodzi w interakcje.

Ale ta otwartość ma też swoją ciemną stronę. Kiedy tworzymy złożony, wielokrotnie używany komponent (np. niestandardowy odtwarzacz wideo lub widżet kalendarza), jego wewnętrzna struktura i style stają się podatne na zagrożenia. Style CSS z głównej strony mogą przypadkowo „przeciekać” do wnętrza komponentu i zepsuć jego wygląd. Podobnie, kod JavaScript strony może nieumyślnie zmieniać wewnętrzne elementy komponentu, naruszając jego logikę.

Aby rozwiązać ten problem, istnieje **Shadow DOM (DOM cienia)**.

Zasadniczo Shadow DOM to **„DOM wewnątrz DOM”**. Jest to ukryte drzewo elementów, które jest dołączone do zwykłego elementu na stronie (zwanego „hostem”), ale jest izolowane od głównego DOM. Pozwala programiście stworzyć hermetyczną granicę wokół wewnętrznej struktury komponentu, chroniąc go przed światem zewnętrznym.

Shadow DOM pozwala na dołączanie ukrytych drzew DOM do elementów w zwykłym drzewie DOM. To drzewo cienia zaczyna się od **korzenia cienia** (shadow root), pod którym można dołączać dowolne elementy, tak samo jak w zwykłym DOM.

Istnieje kilka terminów związanych z Shadow DOM, które warto znać:
![DOM](../../assets/shadow_dom/file.png)
*   **Host cienia (Shadow host):** Zwykły węzeł DOM, do którego dołączony jest DOM cienia.
*   **Drzewo cienia (Shadow tree):** Drzewo DOM wewnątrz DOM cienia.
*   **Granica cienia (Shadow boundary):** Miejsce, w którym kończy się DOM cienia i zaczyna się zwykły DOM.
*   **Korzeń cienia (Shadow root):** Węzeł korzenia drzewa cienia.

Możesz wpływać na węzły w DOM cienia dokładnie tak samo, jak na zwykłe węzły. Różnica polega na tym, że żaden kod wewnątrz DOM cienia nie może wpływać na nic poza nim, co zapewnia niezawodną hermetyzację.

Zanim Shadow DOM stał się dostępny dla programistów webowych, przeglądarki już go używały do hermetyzacji wewnętrznej struktury standardowych elementów. Na przykład element `<video>` z kontrolkami. Wszystko, co widzisz w DOM, to tag `<video>`, ale zawiera on szereg przycisków i innych kontrolek wewnątrz swojego DOM cienia.

#### Tworzenie Shadow DOM

Możesz utworzyć Shadow DOM na dwa sposoby: imperatywnie za pomocą JavaScriptu lub deklaratywnie bezpośrednio w HTML.

##### Imperatywnie za pomocą JavaScriptu

Ta metoda doskonale nadaje się do aplikacji renderowanych po stronie klienta. Wybieramy element hosta i wywołujemy na nim metodę `attachShadow()`.

```html
<!-- Znaczniki HTML -->
<div id="host"></div>
<span>Nie jestem w DOM cienia</span>
```

```javascript
// Znajdź hosta i dołącz do niego DOM cienia
const host = document.querySelector("#host");
const shadow = host.attachShadow({ mode: "open" });

// Utwórz i dodaj elementy do drzewa cienia
const span = document.createElement("span");
span.textContent = "Jestem w DOM cienia";
shadow.appendChild(span);
```

Wynik na stronie będzie wyglądał tak:
> Jestem w DOM cienia
> Nie jestem w DOM cienia

##### Deklaratywnie za pomocą HTML

Dla aplikacji, w których ważne jest renderowanie po stronie serwera, można zdefiniować Shadow DOM deklaratywnie, używając elementu `<template>` z atrybutem `shadowrootmode`.



```html
<div id="host">
  <template shadowrootmode="open">
    <p>Ten akapit znajduje się wewnątrz DOM cienia.</p>
    <style>
      p { color: red; } /* Te style będą izolowane */
    </style>
  </template>
</div>
```

Kiedy przeglądarka przetworzy ten kod, automatycznie utworzy korzeń cienia dla `<div>` i umieści w nim zawartość tagu `<template>`. Sam tag `<template>` zniknie z głównego drzewa DOM.

#### Hermetyzacja: ochrona przed JavaScriptem i CSS

Główną zaletą Shadow DOM jest izolacja. Zobaczmy, jak to działa.

##### Hermetyzacja z JavaScriptu

Dodajmy przycisk, który będzie próbował zmienić wszystkie elementy `<span>` na stronie.

```javascript
// ... kod tworzenia DOM cienia ...

const upper = document.querySelector("#upper-button");
upper.addEventListener("click", () => {
  // Ten selektor przeszukuje cały dokument
  const spans = document.querySelectorAll("span");
  for (const span of spans) {
    span.textContent = span.textContent.toUpperCase();
  }
});
```

Po kliknięciu przycisku tekst zmieni się tylko w `<span>`, który znajduje się w głównym dokumencie. Element wewnątrz DOM cienia pozostanie nienaruszony, ponieważ `document.querySelectorAll()` nie może „zajrzeć” poza granicę cienia.

##### Dostęp do DOM cienia: właściwość `shadowRoot` i praca z zagnieżdżeniem

Kiedy wywołujemy `host.attachShadow({ mode: "open" })`, tworzymy DOM cienia w trybie „otwartym”. Oznacza to, że możemy uzyskać dostęp do jego zawartości z zewnątrz poprzez właściwość `host.shadowRoot`.

```javascript
// Znajdź spany tylko w drzewie cienia konkretnego hosta
const spansInShadow = host.shadowRoot.querySelectorAll("span");
```

Jeśli określisz `mode: „closed”`, właściwość `host.shadowRoot` zwróci `null`, a dostęp do drzewa cienia z zewnątrz zostanie zablokowany. Nie jest to ścisły mechanizm bezpieczeństwa, a raczej konwencja dla programistów, że wnętrza komponentu nie należy dotykać.

**Praca z zagnieżdżonymi drzewami cienia**

W złożonych architekturach komponentów, jeden element użytkownika może zawierać w sobie inne elementy użytkownika, z których każdy ma swój własny Shadow DOM. Aby uzyskać dostęp do elementu w głęboko zagnieżdżonym drzewie cienia, trzeba będzie kolejno „przechodzić” przez każdy `shadowRoot`.

Wyobraźmy sobie taką strukturę:
*   Komponent `<nmbrs-form>` (główny formularz).
*   Wewnątrz niego znajduje się `<div>`, a w nim — komponent `<nmbrs-button>` (niestandardowy przycisk).
*   Wewnątrz `<nmbrs-button>` znajduje się prawdziwy przycisk HTML `<button>`.

Aby uzyskać dostęp do tego przycisku z kontekstu globalnego, ścieżka będzie wyglądać tak:

```javascript
// 1. Znajdź komponent główny w głównym dokumencie
const formComponent = document.querySelector('nmbrs-form');

// 2. „Wejdź” do jego drzewa cienia
const shadowRoot1 = formComponent.shadowRoot;

// 3. Znajdź zagnieżdżony komponent przycisku
const buttonComponent = shadowRoot1.querySelector('div div.btn-container nmbrs-button');

// 4. „Wejdź” do drzewa cienia tego komponentu
const shadowRoot2 = buttonComponent.shadowRoot;

// 5. I dopiero teraz znajdź końcowy element
const finalButton = shadowRoot2.querySelector('button#button');
```

W postaci jednego łańcucha wywołań wygląda to tak:

```javascript
const button = document.querySelector('nmbrs-form').shadowRoot
                      .querySelector('div div.btn-container nmbrs-button').shadowRoot
                      .querySelector('button#button');
```

Taki długi łańcuch wyraźnie demonstruje moc hermetyzacji: aby dostać się do wewnętrznych szczegółów, trzeba jawnie przejść przez każdą „granicę”. To sprawia, że kod jest bardziej przewidywalny i chroni komponenty przed przypadkowymi zmianami.

##### Hermetyzacja z CSS

Style zdefiniowane na głównej stronie nie wpływają na elementy wewnątrz DOM cienia.

```css
/* Ten styl zastosuje się tylko do spanów w głównym dokumencie */
span {
  color: blue;
  border: 1px solid black;
}
```

Element `<span>` wewnątrz drzewa cienia nie otrzyma tych stylów. Rozwiązuje to ogromny problem przypadkowych nakładania się i konfliktów CSS.

#### Stosowanie stylów wewnątrz DOM cienia

Style zdefiniowane wewnątrz drzewa cienia, z kolei, nie wpływają na główną stronę. Istnieją dwie główne metody ich dodawania.

##### 1. Konstruowalne arkusze stylów (Constructable Stylesheets)

Ta metoda pozwala na tworzenie obiektu `CSSStyleSheet` w JavaScript i stosowanie go do jednego lub wielu drzew cienia. Jest to efektywne, jeśli masz wspólne style dla wielu komponentów.

```javascript
const sheet = new CSSStyleSheet();
sheet.replaceSync("span { color: red; border: 2px dotted black; }");

const shadow = host.attachShadow({ mode: "open" });
// Zastosuj arkusz stylów do korzenia cienia
shadow.adoptedStyleSheets = [sheet];
```

##### 2. Dodawanie elementu `<style>`

Prosty i deklaratywny sposób — umieść tag `<style>` bezpośrednio wewnątrz drzewa cienia (często wewnątrz `<template>`).

```html
<template id="my-element">
  <style>
    span {
      color: red;
      border: 2px dotted black;
    }
  </style>
  <span>Jestem w DOM cienia</span>
</template>
```

#### Shadow DOM i elementy niestandardowe: idealne połączenie

Cała moc DOM cienia ujawnia się podczas tworzenia **elementów niestandardowych (Custom Elements)**. Bez hermetyzacji byłyby one niezwykle kruche.

Element niestandardowy to klasa, która dziedziczy po `HTMLElement`. Z reguły sam element pełni rolę hosta cienia, a cała jego wewnętrzna struktura jest tworzona w drzewie cienia.

Oto przykład prostego komponentu `<filled-circle>`:

```javascript
class FilledCircle extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" });

    // Utwórz implementację wewnętrzną (np. okrąg SVG)
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("r", "50");
    circle.setAttribute("cx", "50");
    circle.setAttribute("cy", "50");
    // Kolor pobierany z atrybutu hosta
    circle.setAttribute("fill", this.getAttribute("color"));
    
    svg.appendChild(circle);
    shadow.appendChild(svg);
  }
}
customElements.define("filled-circle", FilledCircle);
```

Teraz możemy używać go w HTML jako zwykłego tagu, nie martwiąc się o jego wewnętrzną strukturę:

```html
<filled-circle color="blue"></filled-circle>
<filled-circle color="green"></filled-circle>
```

Każdy z tych komponentów będzie w pełni hermetyczny i chroniony przed wpływem strony zewnętrznej.
