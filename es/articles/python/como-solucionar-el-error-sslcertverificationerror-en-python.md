# Cómo solucionar el error SSLCertVerificationError en Python

    ¿Te has encontrado con el error `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` al intentar realizar una solicitud HTTPS en Python usando `requests` o `urllib3`?
En este artículo, te mostraré cómo diagnosticar y solucionar este problema.

El error significa que Python no pudo verificar el certificado SSL/TLS del sitio web al que te estás conectando porque no encontró un certificado raíz de confianza en su almacén.

## Paso 1: Diagnosticar el problema con OpenSSL (Recomendado)

    Antes de cambiar tu código Python, verifica la conexión SSL usando la utilidad `openssl`. Esto te ayudará a entender si el problema es específico de Python o está relacionado con la configuración del sistema o el propio servidor.

1.  **Instala OpenSSL** si no lo tienes (a menudo preinstalado en Linux/macOS; para Windows, descárgalo del [sitio web oficial](https://www.openssl.org/source/) o usa gestores de paquetes como Chocolatey/Scoop).
2.  **Ejecuta el comando** en tu terminal (línea de comandos), reemplazando `<hostname>` por la dirección del sitio web (sin `https://`) y `<port>` por el puerto (normalmente 443 para HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Ejemplo para rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Analiza la salida:** Presta atención a la línea `Verify return code`. Si contiene un error como `unable to get local issuer certificate` (código 20) o `certificate verify failed` (código 21), esto confirma un problema con la confianza en el certificado a nivel del sistema o del almacén utilizado por OpenSSL.

## Paso 2: Elige un método de solución

    Existen varias formas de solucionar el error `SSLCertVerificationError`. Elige la que mejor se adapte a tu situación.

### Método 1: Desactivar la verificación SSL (Rápido, pero INSEGURO)

    Este método desactiva completamente la verificación del certificado. Úsalo **solo** para pruebas temporales, scripts de un solo uso y **solo** para sitios en los que confíes absolutamente.

⚠️ **Advertencia:** Desactivar la verificación hace que tu conexión sea vulnerable a ataques de "hombre en el medio" (MITM). **¡Nunca uses `verify=False` en código de producción o al trabajar con datos confidenciales!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Ejemplo de URL

try:
    # Suprimimos las advertencias sobre solicitudes inseguras (opcional)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Comprobar errores HTTP (4xx, 5xx)

    # Tu código para procesar la respuesta, por ejemplo, guardar el archivo
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Archivo descargado con éxito (con verificación SSL desactivada).")

except requests.exceptions.RequestException as e:
    print(f"Error al descargar el archivo: {e}")

finally:
    # Importante: Si desactivaste las advertencias globalmente,
    # es posible que quieras volver a activarlas después de que la solicitud se complete,
    # aunque esto normally no es necesario si el script finaliza.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Método 2: Instalar/Actualizar certificados para Python (Depende de la plataforma)

    Python puede venir con scripts para instalar o actualizar el conjunto de certificados raíz del paquete `certifi`.

*   **En macOS:**
    1.  Ve a la carpeta de instalación de Python (normalmente `/Applications/Python <versión>/`).
    2.  Busca y haz doble clic en el archivo `Install Certificates.command`. Instalará/actualizará `certifi` y vinculará el módulo `ssl` estándar con estos certificados.
*   **En Windows:**
    1.  A veces, al instalar Python, se crea un script `install_certificates.bat`. Búscalo en el directorio `Scripts` dentro de la carpeta de instalación de Python (por ejemplo, `C:\Users\<nombre_de_usuario>\AppData\Local\Programs\Python\Python<versión>\Scripts\`).
    2.  Si lo encuentras, ejecútalo.
    3.  Si el script no está presente, es probable que este método no funcione. Usa el Método 3.

### Método 3: Usar el paquete `certifi` directamente (Recomendado, multiplataforma)

    Esta es la forma más fiable de indicar explícitamente a Python qué conjunto de certificados raíz usar.

1.  **Instala `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Usa `certifi` en tu código:** Pasa la ruta al archivo de certificados `certifi` al parámetro `verify` de la función `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # Ejemplo de URL

    try:
        # Indicamos explícitamente que use los certificados de certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Tu código para procesar la respuesta
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("Archivo descargado con éxito usando certificados certifi.")

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")
    ```
    Incluso si `requests` puede usar `certifi` por defecto, la especificación explícita `verify=certifi.where()` garantiza este comportamiento.

### Método 4: Usar almacenes del sistema o variables de entorno (Avanzado)

    El módulo `ssl` de Python también puede buscar certificados en almacenes del sistema o en rutas especificadas en variables de entorno. Esto es útil, por ejemplo, en entornos corporativos con sus propias autoridades de certificación (CA).

1.  **Almacenes del sistema:**
    *   **Linux/macOS:** Python a menudo usa automáticamente los certificados del sistema (por ejemplo, de `/etc/ssl/certs/`). Asegúrate de que tu sistema tenga certificados raíz actualizados (`sudo apt update && sudo apt install ca-certificates` para Debian/Ubuntu, `sudo yum update ca-certificates` para CentOS/RHEL).
    *   **Windows:** Python *puede* intentar usar el almacén del sistema de Windows, pero esto no siempre funciona de forma fiable sin paquetes adicionales (por ejemplo, `python-certifi-win32`). Se recomienda usar `certifi` (Método 3).
2.  **Variables de entorno:** Puedes especificar explícitamente la ruta a un archivo o directorio con certificados:
    *   `SSL_CERT_FILE`: Especifica la ruta a un *archivo* (en formato PEM) que contenga todos los certificados raíz de confianza.
    *   `SSL_CERT_DIR`: Especifica la ruta a un *directorio* donde cada certificado se encuentra en un archivo PEM separado con un nombre tipo hash (usa `c_rehash` de OpenSSL para preparar el directorio).

    **Cómo establecer variables de entorno:**

    *   **Linux/macOS (temporalmente, para la sesión actual):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, temporalmente):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, temporalmente):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    Para añadir tu propia CA (por ejemplo, corporativa), debes añadir su certificado al archivo `SSL_CERT_FILE` o al directorio `SSL_CERT_DIR`.

## Paso 3 (Bonus): Cómo crear un certificado autofirmado para desarrollo local

    Si estás desarrollando un servidor web local (API, sitio) y quieres probarlo con HTTPS, necesitarás un certificado SSL. Como no tienes un dominio público para obtener un certificado de una CA normal, puedes crear un certificado *autofirmado*.

**Uso de OpenSSL (multiplataforma):**

1.  **Ejecuta el comando:** Este comando creará una clave privada (`key.pem`) y el propio certificado (`cert.pem`), válido por 10 años, para `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Crea una clave sin protección de contraseña (conveniente para el desarrollo).
    *   `-subj "/CN=localhost"`: Establece el Common Name.
    *   `-addext "subjectAltName = ..."`: Añade Subject Alternative Names (importante para navegadores y clientes modernos).

2.  **Usa `key.pem` y `cert.pem`** en la configuración de tu servidor web local (Flask, Django, Node.js, etc.) para habilitar HTTPS.

**Uso de PowerShell (Windows 10/11):**

1.  **Ejecuta el comando en PowerShell (con derechos de administrador):** Este comando creará un certificado y lo colocará en el almacén de certificados del equipo.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Es posible que necesites exportar este certificado del almacén (`certlm.msc`) a archivos `.pfx` o `.pem` para que tu servidor web use.

**Nota:** Los navegadores y clientes HTTP (incluido `requests` de Python por defecto) no confiarán en los certificados autofirmados. Al acceder a dicho servidor, recibirás una advertencia o error SSL. Para las pruebas, deberás añadir este certificado a los certificados raíz de confianza de tu sistema/navegador, o usar `verify=False` (para `requests`), o especificar la ruta a tu `cert.pem` a través de `verify='/path/to/cert.pem'`. 
