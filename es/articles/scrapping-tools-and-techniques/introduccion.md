### **Ciclo «NO Selenium». Introducción**

Aquellos que se dedican al web scraping, las pruebas y la automatización están familiarizados con Selenium, el más moderno Playwright y/o el framework Crawlee. Son potentes, pueden hacer casi todo, y... no siempre son necesarios. Es más, en muchos casos, el uso de estas herramientas es como clavar clavos con un microscopio: el trabajo, por supuesto, se hará, pero a costa de gastos injustificados: velocidad, recursos del sistema y complejidad de configuración.

Bienvenidos al ciclo de artículos «NO Selenium». Aquí mostraré otras formas (no siempre obvias) de interactuar con el contenido de Internet.

#### Paradigma #1: Comunicación directa. Clientes HTTP

*   **`Requests`** — Forma y envía una solicitud de red a la dirección de destino (URL), exactamente como lo hace tu navegador en el primer momento de la carga de la página, pero sin el navegador en sí. En esta solicitud, empaqueta el método (por ejemplo, `GET`, para obtener datos), los encabezados (`Headers`), que se presentan al sitio (por ejemplo, `User-Agent: "soy-un-navegador"`), y otros parámetros. En respuesta del servidor, recibe datos sin procesar, la mayoría de las veces, el código HTML original de la página o una cadena en formato JSON, así como un código de estado (por ejemplo, `200 OK`).

*   **`HTTPX`** — es un sucesor moderno de `Requests`. A un nivel fundamental, hace lo mismo: envía las mismas solicitudes HTTP con los mismos encabezados y recibe las mismas respuestas. Pero hay una diferencia clave: `Requests` funciona **sincrónicamente** — envía una solicitud, se sienta y espera una respuesta, recibe una respuesta, envía la siguiente. `HTTPX`, por otro lado, puede funcionar **asincrónicamente** — puede "lanzar" cien solicitudes a la vez sin esperar respuestas, y luego procesarlas eficientemente a medida que llegan.

Son excelentes para recopilar datos de sitios estáticos, trabajar con API, analizar miles de páginas donde no se requiere la ejecución de JavaScript.

*   **Ventajas:** **Velocidad y eficiencia.** Gracias a la naturaleza asíncrona de `HTTPX`, donde `Requests` haría secuencialmente 100 solicitudes durante varios minutos, `HTTPX` lo hará en unos pocos segundos.
*   **Desventajas:** No apto para sitios donde el contenido se genera mediante JavaScript.

#### Paradigma #2: Protocolo de herramientas de desarrollo de Chrome (CDP)

¿Qué hacer si el sitio es dinámico y el contenido se genera mediante JavaScript? Los navegadores modernos (Chrome, Chromium, Edge) tienen un protocolo integrado para depuración y control: **Chrome DevTools Protocol (CDP)**. Permite enviar comandos directamente al navegador, evitando la engorrosa capa de WebDriver que utiliza Selenium.

*   **Herramientas:** El principal representante de este enfoque hoy en día es `Pydoll`, que reemplazó al alguna vez popular pero ahora sin soporte `pyppeteer`.
*   **Cuándo usar:** Cuando se necesita renderizado de JavaScript, pero se desea mantener una alta velocidad y evitar las complejidades de los controladores.
*   **Ventajas:** **Equilibrio.** Obtienes el poder de un navegador real, pero con una sobrecarga mucho menor y, a menudo, con mecanismos integrados de elusión de protecciones.
*   **Desventajas:** Puede ser más difícil de depurar que Playwright y requiere una comprensión más profunda del funcionamiento del navegador.

#### Paradigma #3: Agentes LLM autónomos

Este es el límite más avanzado. ¿Qué pasa si en lugar de escribir código que dice "haz clic aquí, escribe esto", simplemente damos una tarea en lenguaje natural? "Encuentra todos los proveedores en este sitio y recopila sus categorías de productos".

Esta es exactamente la tarea que resuelven los agentes LLM. Utilizando un "cerebro" en forma de un gran modelo de lenguaje (GPT, Gemini) y "manos" en forma de un conjunto de herramientas (navegador, búsqueda de Google), estos agentes pueden planificar y ejecutar de forma independiente tareas complejas en la web.

*   **Herramientas:** Conjuntos como `LangChain` + `Pydoll` o soluciones personalizadas, como en `simple_browser.py`, que analizaremos más adelante.
*   **Cuándo usar:** Para tareas de investigación complejas donde los pasos son desconocidos de antemano y se requiere adaptación en tiempo real.
*   **Ventajas:** **Inteligencia.** La capacidad de resolver problemas no estructurados y adaptarse a los cambios sobre la marcha.
*   **Desventajas:** "No determinismo" (los resultados pueden variar de una ejecución a otra), costo de las llamadas a la API de LLM, menor velocidad en comparación con el código directo.

#### Paradigma #4: Scraping sin código

A veces la tarea es tan simple que escribir código es excesivo. ¿Necesitas extraer rápidamente una tabla de una página? Para esto existen soluciones elegantes que no requieren programación.

*   **Herramientas:** Funciones de Google Sheets (`IMPORTXML`, `IMPORTHTML`), extensiones del navegador.
*   **Cuándo usar:** Para tareas únicas, prototipado rápido o cuando simplemente no quieres escribir código.
*   **Ventajas:** **Simplicidad.** Abrió, especificó qué recopilar, — obtuvo el resultado.
*   **Desventajas:** Funcionalidad limitada, no apto para tareas complejas o grandes volúmenes de datos.

### ¿Qué sigue?

Este artículo es solo una introducción. En los próximos números de nuestro ciclo «NO Selenium», pasaremos de la teoría a la práctica dura. Nos sumergiremos profundamente en cada uno de estos paradigmas y mostraremos cómo funcionan con ejemplos del mundo real:

*   Analizaremos **Pydoll** y veremos cómo elude Cloudflare.
*   Organizaremos una batalla entre **JavaScript vs. Python** por el título del mejor lenguaje para scraping.
*   Aprenderemos a exprimir la máxima velocidad del análisis con **lxml**.
*   Escribiremos un script que recopila datos de **Amazon** y los guarda en **Excel**.
*   Mostraremos cómo **Google Sheets** puede convertirse en tu primer scraper.
*   Y, por supuesto, analizaremos en detalle cómo crear y usar un **agente LLM autónomo** para controlar el navegador.

Prepárate para cambiar tu visión sobre la automatización y la recopilación de datos en la web. Será rápido, eficiente y muy interesante. Suscríbete
