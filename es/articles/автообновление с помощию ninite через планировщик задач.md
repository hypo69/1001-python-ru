Tienes toda la razón. Gracias por la aclaración. El uso de comillas «ёлочки» es estándar en la tipografía rusa.

Aquí tienes la versión corregida del artículo con las comillas correctas:

***

### Cómo actualizar programas automáticamente con Ninite y el Programador de tareas de Windows

Mantener el software actualizado es clave para la seguridad y estabilidad de tu sistema. Sin embargo, la verificación e instalación manual de actualizaciones para cada aplicación puede llevar mucho tiempo. En este artículo, veremos cómo automatizar este proceso utilizando el servicio Ninite.com y el Programador de tareas de Windows integrado.

### Parte 1: Familiarización con Ninite y creación de un instalador

Ninite es un servicio diseñado para la instalación y actualización simultánea de varias aplicaciones populares. Su objetivo es ahorrarte tiempo, eliminando la necesidad de instalar manualmente cada programa, desplazarte por los asistentes de instalación y rechazar ofertas para instalar barras de herramientas u otro software no deseado.

**Características y beneficios clave de Ninite:**

*   **Instalación sin acciones innecesarias:** No necesitas hacer clic en «siguiente» ni rechazar barras de herramientas y basura adicional. Simplemente selecciona las aplicaciones deseadas y ejecuta el instalador.
*   **Versiones siempre actualizadas:** Ninite utiliza bots para rastrear actualizaciones, por lo que siempre obtendrás las últimas versiones estables de las aplicaciones.
*   **Automatización del proceso:** Ninite funciona en segundo plano, instalando aplicaciones en ubicaciones estándar y en el idioma de tu sistema. Omite las aplicaciones ya actualizadas e ignora las solicitudes de reinicio de los instaladores.
*   **Seguridad:** Las aplicaciones se descargan directamente de los sitios web oficiales de los editores, y sus firmas digitales o hashes se verifican antes de la ejecución para garantizar la autenticidad.
*   **Soporte del sistema:** Ninite funciona en Windows 11, 10, 8.x, 7 y versiones de servidor equivalentes.
*   **Gratis para uso doméstico:** El sitio es gratuito para uso personal (sin anuncios ni software no deseado). La versión de pago Ninite Pro ofrece funciones extendidas para la gestión de software en organizaciones.

**Secciones de aplicaciones (categorías) entre las que puedes elegir:**

Ninite ofrece una amplia gama de programas, agrupados por categorías:

*   **Navegadores web (Web Browsers):** Chrome, Opera, Firefox, Edge, Brave.
*   **Mensajería (Messaging):** Zoom, Discord, Teams, Pidgin, Thunderbird.
*   **Multimedia (Media):** iTunes, VLC, AIMP, foobar2000, Audacity, K-Lite Codecs, Spotify, HandBrake.
*   **Imágenes (Imaging):** Krita, Blender, Paint.NET, GIMP, IrfanView, Inkscape, Greenshot, ShareX.
*   **Documentos (Documents):** Foxit Reader, LibreOffice, SumatraPDF, OpenOffice.
*   **Seguridad (Security):** Malwarebytes, Avast, AVG, Avira.
*   **Almacenamiento en la nube (Online Storage):** Dropbox, Google Drive, OneDrive.
*   **Utilidades (Utilities):** TeamViewer, ImgBurn, TeraCopy, Revo, WinDirStat, CCleaner.
*   **Compresión (Compression):** 7-Zip, PeaZip, WinRAR.
*   **Herramientas de desarrollo (Developer Tools):** Python, Git, FileZilla, Notepad++, WinSCP, PuTTY, Visual Studio Code.
*   **Y mucho más:** incluyendo .NET, Java, utilidades y otras herramientas útiles.

**Cómo seleccionar y descargar el archivo de instalación:**

1.  **Selecciona aplicaciones:** En la página principal de ninite.com, verás una lista de categorías con aplicaciones. Marca las casillas de los programas que deseas instalar o mantener actualizados.
2.  **Descarga el instalador:** Después de seleccionar las aplicaciones, haz clic en el botón **«Get Your Ninite»**. El sitio generará y te ofrecerá descargar un archivo ejecutable personal. Este pequeño archivo es tu instalador/actualizador universal.

### Parte 2: Configuración de la actualización automática

Ahora que tienes un instalador de Ninite configurado, veamos dónde es mejor colocarlo y cómo configurar el inicio automático.

**Dónde colocar el archivo de Ninite**

Para que el sistema pueda encontrar y ejecutar tu archivo de Ninite sin problemas, se recomienda crear una carpeta separada para él. Esto evitará la eliminación o el movimiento accidental del archivo.

**Recomendaciones de ubicación:**

*   **Evita las carpetas del sistema:** No guardes el archivo en la raíz de la unidad `C:` ni en la carpeta `C:\Windows`.
*   **Crea una carpeta dedicada:** Una buena práctica sería crear una carpeta, por ejemplo, `C:\NiniteUpdater`. Esto simplificará la gestión del archivo y su búsqueda en el futuro.

Mueve el archivo de Ninite descargado del sitio (por ejemplo, `Ninite-paquete-de-software.exe`) a la carpeta que creaste anteriormente (`C:\NiniteUpdater`).

**Configuración del inicio automático a través del Programador de tareas de Windows**

Para que la verificación y actualización de programas se realicen automáticamente cada domingo, utilizaremos la herramienta integrada de Windows: el **Programador de tareas**.

**1. Apertura del Programador de tareas:**

*   Presiona las teclas `Win + R`, escribe `taskschd.msc` y presiona Enter.

**2. Creación de una nueva tarea:**

En la ventana del Programador de tareas, en el panel derecho «Acciones», selecciona **«Crear tarea básica...»**.

*   **Nombre y descripción:** Introduce un nombre claro para tu tarea, por ejemplo, «Actualización semanal de Ninite». Haz clic en «Siguiente».
*   **Desencadenador (hora de inicio):** En este paso, debes especificar con qué frecuencia se ejecutará la tarea.
    *   Selecciona «Semanalmente» y haz clic en «Siguiente».
    *   Especifica el día de la semana — «domingo». También puedes elegir una hora de inicio conveniente para ti, por ejemplo, cuando el ordenador suele estar encendido pero no se utiliza activamente. Haz clic en «Siguiente».
*   **Acción:** Aquí especificaremos qué programa ejecutar.
    *   Selecciona «Iniciar un programa» y haz clic en «Siguiente».
    *   En el campo «Programa o script», haz clic en el botón «Examinar...» y busca tu archivo de Ninite en la carpeta que creaste anteriormente (`C:\NiniteUpdater\Ninite-paquete-de-software.exe`).
    *   Haz clic en «Siguiente».
*   **Finalización:** En el último paso, verifica todos los parámetros especificados. Si todo es correcto, haz clic en «Finalizar».

Ahora, el Programador de tareas ejecutará automáticamente tu archivo de Ninite cada domingo a la hora que especificaste. Cuando Ninite se ejecute en segundo plano, verificará las versiones de los programas que seleccionaste y, si encuentra actualizaciones, las descargará e instalará sin tu intervención. De este modo, obtendrás un sistema sencillo y fiable para mantener tu software actualizado.
