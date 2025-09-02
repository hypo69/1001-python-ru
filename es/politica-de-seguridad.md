<table>
<tr>
<TD>
<A HREF = 'https://github.com/hypo69/hypotez/blob/master/README.MD'>[Raíz ↑]</A>
</TD>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/src/README.MD'>Código</a>
</td>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/docs/gemini/out/README.MD'>Documentación</a> 
</td>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/README.RU.MD'>Русский</a>
</td>
</tr>
</table>

Almacenamiento de la configuración de la aplicación
=====================================================

### 1. Almacenamiento de contraseñas y credenciales en KeePass

Para almacenar de forma segura credenciales como contraseñas y claves de API, utilice KeePass. Siga estos pasos:

1.  **Crear una base de datos de KeePass**:
    -   Abra KeePass y cree una nueva base de datos seleccionando **Archivo > Nueva base de datos**.
    -   Establezca una contraseña maestra segura para proteger la base de datos.
    -   **Ubicación**: Guarde el archivo de la base de datos de KeePass (`credentials.kdbx`) en la carpeta `secrets` de su proyecto:
        ```
        raíz
        ├── datos
        ├── secrets
        │   └── credentials.kdbx  # <-- Archivo de la base de datos de KeePass
        │   └── passowrd.txt
        │   └── <googke api josn kes>.json
        ├── src
        └── ...

        - Nunca comparta el archivo `credentials.kdbx` con otros. ❗
        - Asegúrese de que el archivo se almacena en una ubicación segura a la que solo usted tenga acceso. (La carpeta `secrets` en la raíz del proyecto está excluida de `git`).
        - Actualice periódicamente sus claves de API y las contraseñas de la base de datos.     ```

2.  **Crear grupos y entradas**:
    -   Su base de datos debe contener varios grupos para organizar las credenciales. Por ejemplo:
        -   **proveedores**
            -   **aliexpress**
                -   Entrada para la API que contiene:
                    -   `api_key`: Su clave de API de Aliexpress.
                    -   `secret`: Su clave secreta de Aliexpress.
                    -   `tracking_id`: ID de seguimiento.
                    -   `email`: Su dirección de correo electrónico.
                    -   `password`: Su contraseña de Aliexpress.
            -   **openai**
                -   Entrada para la API de OpenAI que contiene:
                    -   `api_key`: Su clave de API de OpenAI.
            -   **discord**
                -   Entrada para la API de Discord que contiene:
                    -   `application_id`: ID de la aplicación de Discord.
                    -   `public_key`: Clave pública.
                    -   `bot_token`: Token del bot.
            -   **prestashop** y otros servicios con las entradas correspondientes.

3.  **Añadir propiedades personalizadas**:
    -   Al crear entradas, añada propiedades personalizadas para almacenar datos adicionales. Por ejemplo, en la entrada de Aliexpress, añada campos para:
        -   `tracking_id`
        -   `username`
        -   `email`

### 2. Configuración del archivo `settings.json`

El archivo `settings.json` almacena la configuración principal de su proyecto. A continuación se explica cómo configurarlo:

1.  **Crear el archivo `settings.json`**:
    -   Cree un archivo llamado `settings.json` en el directorio `/src` de su proyecto.

2.  **Ejemplo de contenido del archivo `settings.json`**:
    ```json
    {
      "google_drive": "H:\\Mi unidad\\hypo69",  // Ruta a la carpeta de Google Drive utilizada para almacenar datos.
      "mode": "debug",                          // Modo de la aplicación: 'debug' para desarrollo o 'production' para modo en vivo.
      "git_user": "hypo69",                    // Nombre de usuario para acceder al repositorio de Git.
      "git": "hypo"                             // Nombre del repositorio de Git.
    }
    ```

3.  **Descripción de los campos**:
    -   **google_drive**: La ruta al directorio de su Google Drive donde se almacenarán los datos del proyecto. Asegúrese de que esta ruta es correcta para su sistema.
    -   **mode**: Especifique el modo de su aplicación. Utilice `debug` para las pruebas y `production` para la implementación.
    -   **git_user**: Su nombre de usuario en GitHub u otra plataforma donde esté alojado su repositorio.
    -   **git**: El nombre de su repositorio que se utiliza para realizar el seguimiento de los cambios en el código.

### 3. Protección de la información sensible

-   **Datos sensibles**: El archivo que contiene sus claves de API y contraseñas se almacena en la carpeta `secrets`, que **no se incluye en el repositorio de Git** para evitar el acceso no autorizado. Todas las contraseñas y claves de API deben cargarse desde KeePass al inicio del programa, como se describe en el código.
-   **Copia de seguridad**: Realice copias de seguridad periódicas de su base de datos de KeePass y del archivo `settings.json` para evitar la pérdida de datos.

## Informar de una vulnerabilidad

Si encuentra una vulnerabilidad de seguridad en nuestro proyecto, por favor, infórmenos siguiendo estos pasos:

1.  **Correo electrónico**: Envíe un correo electrónico a [security@example.com] con una descripción de la vulnerabilidad.
2.  **Información a incluir**:
    -   Una descripción detallada del problema
    -   Pasos para reproducir la vulnerabilidad
    -   Versión(es) afectada(s)
    -   Cualquier otra información relevante

3.  **Tiempo de respuesta**: Puede esperar recibir un acuse de recibo en un plazo de 48 horas. Nuestro objetivo es proporcionar actualizaciones sobre el estado de la vulnerabilidad notificada cada semana hasta que se resuelva.

4.  **Resultado**: Si se confirma la vulnerabilidad, trabajaremos en una solución y le notificaremos cuando esté disponible. Si determinamos que el informe no es una vulnerabilidad, le informaremos de nuestra decisión.

## Versiones compatibles

| Versión | Compatible         |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

¡Gracias por ayudarnos a mantener nuestro proyecto seguro!

--- 

¡Avíseme si necesita más ajustes!
