### **Ciclo "NO Selenium". Introducción**

Aquellos que se dedican al web scraping, las pruebas y la automatización están familiarizados con Selenium, el más moderno Playwright y/o el framework Crawlee. Son potentes, pueden hacer casi de todo, y... no siempre son necesarios. Es más, en muchos casos, usar estas herramientas es como clavar clavos con un microscopio: el trabajo, por supuesto, se hará, pero a costa de gastos injustificados: velocidad, recursos del sistema y complejidad de configuración.

Bienvenido al ciclo de artículos "NO Selenium". Aquí te mostraré otras formas (no siempre obvias) de interactuar con el contenido de Internet.

#### Paradigma #1: Comunicación Directa. Clientes HTTP

*   **`Requests`** — Forma y envía una solicitud de red a la dirección de destino (URL), exactamente como lo hace tu navegador en el primer momento de la carga de la página, pero sin el navegador en sí. En esta solicitud, empaqueta el método (por ejemplo, `GET` para obtener datos), encabezados (`Headers`), que se presentan al sitio (por ejemplo, `User-Agent: "soy-un-navegador"`), y otros parámetros. En respuesta del servidor, recibe datos sin procesar — la mayoría de las veces, es el código HTML original de la página o una cadena en formato JSON, así como un código de estado (por ejemplo, `200 OK`).

*   **`HTTPX`** — es un sucesor moderno de `Requests`. A nivel fundamental, hace lo mismo: envía las mismas solicitudes HTTP con los mismos encabezados y recibe las mismas respuestas. Pero hay una diferencia clave: `Requests` funciona **sincrónicamente** — envía una solicitud, se sienta y espera una respuesta, obtiene una respuesta, envía la siguiente. `HTTPX`, por otro lado, puede funcionar **asincrónicamente** — puede "lanzar" cien solicitudes a la vez sin esperar respuestas, y luego procesarlas eficientemente a medida que llegan.

Son excelentes para recopilar datos de sitios estáticos, trabajar con APIs, analizar miles de páginas donde no se requiere la ejecución de JavaScript.

*   **Ventajas:** **Velocidad y eficiencia.** Gracias a la naturaleza asíncrona de `HTTPX`, donde `Requests` haría secuencialmente 100 solicitudes durante varios minutos, `HTTPX` lo manejará en unos pocos segundos.
*   **Desventajas:** No son adecuados para sitios donde el contenido se genera mediante JavaScript.

#### Paradigma #2: Protocolo de Herramientas de Desarrollo de Chrome (CDP)

¿Qué hacer si el sitio es dinámico y el contenido se genera mediante JavaScript? Los navegadores modernos (Chrome, Chromium, Edge) tienen un protocolo integrado para depuración y control — **Chrome DevTools Protocol (CDP)**. Permite enviar comandos directamente al navegador, evitando la engorrosa capa de WebDriver que utiliza Selenium.

*   **Herramientas:** El principal representante de este enfoque hoy en día es `Pydoll`, que reemplazó al alguna vez popular pero ahora sin soporte `pyppeteer`.</li>
*   **Cuándo usar:** Cuando se necesita renderizado de JavaScript, pero se desea mantener una alta velocidad y evitar complejidades con los controladores.</li>
*   **Ventajas:** **Equilibrio.** Obtienes el poder de un navegador real, pero con una sobrecarga mucho menor y, a menudo, con mecanismos integrados para eludir las protecciones.</li>
*   **Desventajas:** Puede ser más difícil de depurar que Playwright y requiere una comprensión más profunda del funcionamiento del navegador.</li>
</ul>
<h4>Paradigma #3: Agentes LLM Autónomos</h4>
<p>Este es el límite más avanzado. ¿Qué pasaría si, en lugar de escribir código que diga "haz clic aquí, introduce esto", simplemente diéramos una tarea en lenguaje natural? "Encuentra todos los proveedores en este sitio y recopila sus categorías de productos".</p>
<p>Este es exactamente el problema que resuelven los agentes LLM. Utilizando un "cerebro" en forma de un gran modelo de lenguaje (GPT, Gemini) y "manos" en forma de un conjunto de herramientas (navegador, búsqueda de Google), estos agentes pueden planificar y ejecutar de forma independiente tareas complejas en la web.</p>
<ul>
<li><strong>Herramientas:</strong> Conjuntos como `LangChain` + `Pydoll` o soluciones personalizadas, como en `simple_browser.py`, que analizaremos más adelante.</li>
<li><strong>Cuándo usar:</strong> Para tareas de investigación complejas donde los pasos son desconocidos de antemano y se requiere adaptación en tiempo real.</li>
<li><strong>Ventajas:</strong> **Inteligencia.** La capacidad de resolver problemas no estructurados y adaptarse a los cambios sobre la marcha.</li>
<li><strong>Desventajas:</strong> "No determinismo" (los resultados pueden variar de una ejecución a otra), costo de las llamadas a la API de LLM, menor velocidad en comparación con el código directo.</li>
</ul>
<h4>Paradigma #4: Scraping sin código</h4>
<p>A veces la tarea es tan simple que escribir código es excesivo. ¿Necesitas extraer rápidamente una tabla de una página? Para esto existen soluciones elegantes que no requieren programación.</p>
<ul>
<li><strong>Herramientas:</strong> Funciones Google Sheets (<code>IMPORTXML</code>, <code>IMPORTHTML</code>), extensiones de navegador.</li>
<li><strong>Cuándo usar:</strong> Para tareas únicas, prototipado rápido o cuando simplemente no quieres escribir código.</li>
<li><strong>Ventajas:</strong> **Simplicidad.** Abrió, especificó qué recopilar, — obtuvo el resultado.</li>
<li><strong>Desventajas:</strong> Funcionalidad limitada, no aptas para tareas complejas o grandes volúmenes de datos.</li>
</ul>
<h3>¿Qué sigue?</h3>
<p>Este artículo es solo una introducción. En las próximas entregas de nuestro ciclo "NO Selenium", pasaremos de la teoría a la práctica dura. Profundizaremos en cada uno de estos paradigmas y mostraremos cómo funcionan con ejemplos del mundo real:</p>
<ul>
<li>Analizaremos <strong>Pydoll</strong> y veremos cómo elude Cloudflare.</li>
<li>Organizaremos una batalla entre <strong>JavaScript vs. Python</strong> por el título del mejor lenguaje para web scraping.</li>
<li>Aprenderemos a exprimir la máxima velocidad del análisis con <strong>lxml</strong>.</li>
<li>Escribiremos un script que recopila datos de <strong>Amazon</strong> y los guarda en <strong>Excel</strong>.</li>
<li>Mostraremos cómo <strong>Google Sheets</strong> puede convertirse en tu primer scraper.</li>
<li>Y, por supuesto, analizaremos en detalle cómo crear y usar un <strong>agente LLM autónomo</strong> para controlar el navegador.</li>
</ul>
<p>Prepárate para cambiar tu visión sobre la automatización y la recopilación de datos en la web. Será rápido, eficiente y muy interesante. Suscríbete</p>
