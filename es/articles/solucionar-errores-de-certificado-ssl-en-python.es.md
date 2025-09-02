# Cómo corregir el error SSLCertVerificationError en Python

    ¿Se ha encontrado con el error `SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed` al intentar realizar una solicitud HTTPS en Python con `requests` o `urllib3`? 
En este artículo, le mostraré cómo diagnosticar y solucionar este problema.

El error significa que Python no pudo verificar el certificado SSL/TLS del sitio web al que se está conectando porque no pudo encontrar un certificado raíz de confianza en su almacén.

## Paso 1: Diagnóstico del problema con OpenSSL (recomendado)

    Antes de cambiar el código de Python, compruebe la conexión SSL con la utilidad `openssl`. Esto le ayudará a comprender si el problema es específico de Python o está relacionado con la configuración del sistema o con el propio servidor.

1.  **Instale OpenSSL** si no lo tiene (suele estar preinstalado en Linux/macOS; para Windows, descárguelo del [sitio web oficial](https://www.openssl.org/source/) o utilice gestores de paquetes como Chocolatey/Scoop).
2.  **Ejecute el comando** en su terminal (línea de comandos), sustituyendo `<hostname>` por la dirección del sitio (sin `https://`) y `<port>` por el puerto (normalmente 443 para HTTPS):

    ```bash
    openssl s_client -connect <hostname>:<port> -showcerts

    # Ejemplo para rosstat.gov.ru:
    openssl s_client -connect rosstat.gov.ru:443 -showcerts
    ```
3.  **Analice la salida:** Preste atención a la línea `Verify return code`. Si contiene un error como `unable to get local issuer certificate` (código 20) o `certificate verify failed` (código 21), esto confirma un problema de confianza en el certificado a nivel del sistema o del almacén que utiliza OpenSSL.

## Paso 2: Elija un método de solución

    Hay varias formas de corregir el error `SSLCertVerificationError`. Elija la que mejor se adapte a su situación.

### Método 1: Desactivar la verificación SSL (rápido, pero INSEGURO)

    Este método desactiva por completo la verificación del certificado. Úselo **solo** para pruebas temporales, scripts de un solo uso y **solo** para sitios en los que confíe absolutamente.

⚠️ **Advertencia:** Desactivar la verificación hace que su conexión sea vulnerable a ataques de intermediario (MITM). **¡Nunca use `verify=False` en código de producción o cuando trabaje con datos confidenciales!**

```python
import requests
import urllib3

url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # URL de ejemplo

# Desactivar la verificación SSL
try:
    # Suprimir las advertencias sobre solicitudes no seguras (opcional)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    response = requests.get(url, verify=False)
    response.raise_for_status() # Comprobar si hay errores HTTP (4xx, 5xx)

    # Su código para manejar la respuesta, por ejemplo, guardar un archivo
    with open("downloaded_file.xlsx", "wb") as f:
        f.write(response.content)
    print("Archivo descargado correctamente (con la verificación SSL desactivada).")

except requests.exceptions.RequestException as e:
    print(f"Error al descargar el archivo: {e}")

finally:
    # Importante: Si ha desactivado las advertencias globalmente,
    # es posible que desee volver a activarlas una vez completada la solicitud,
    # aunque esto no suele ser necesario si el script finaliza.
    # import warnings
    # warnings.simplefilter('default', urllib3.exceptions.InsecureRequestWarning)
    pass
```

### Método 2: Instalar/Actualizar certificados para Python (depende de la plataforma)

    Python puede venir con scripts para instalar o actualizar el conjunto de certificados raíz del paquete `certifi`.

*   **En macOS:**
    1.  Vaya a la carpeta de instalación de Python (normalmente `/Applications/Python <version>/`).
    2.  Busque y haga doble clic en el archivo `Install Certificates.command`. Instalará/actualizará `certifi` y vinculará el módulo `ssl` estándar a estos certificados.
*   **En Windows:**
    1.  A veces, al instalar Python, se crea un script `install_certificates.bat`. Búsquelo en el directorio `Scripts` dentro de la carpeta de instalación de Python (por ejemplo, `C:\Users\<username>\AppData\Local\Programs\Python\Python<version>\Scripts\`).
    2.  Si lo encuentra, ejecútelo.
    3.  Si el script no está allí, lo más probable es que este método no funcione. Utilice el método 3.

### Método 3: Usar el paquete `certifi` directamente (recomendado, multiplataforma)

    Esta es la forma más fiable de indicar explícitamente a Python qué conjunto de certificados raíz debe utilizar.

1.  **Instale `certifi`:**
    ```bash
    pip install --upgrade certifi
    ```
2.  **Use `certifi` en su código:** Pase la ruta al archivo de certificados de `certifi` al parámetro `verify` de la función `requests.get()`.

    ```python
    import requests
    import certifi

    url = "https://rosstat.gov.ru/storage/mediabank/tab5_v01.xlsx" # URL de ejemplo

    try:
        # Especificar explícitamente que se usen los certificados de certifi
        response = requests.get(url, verify=certifi.where())
        response.raise_for_status()

        # Su código para manejar la respuesta
        with open("downloaded_file_certifi.xlsx", "wb") as f:
            f.write(response.content)
        print("Archivo descargado correctamente usando los certificados de certifi.")

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")
    ```
    Aunque `requests` puede usar `certifi` por defecto, especificar explícitamente `verify=certifi.where()` garantiza este comportamiento.

### Método 4: Usar almacenes del sistema o variables de entorno (avanzado)

    El módulo `ssl` de Python también puede buscar certificados en los almacenes del sistema o en las rutas especificadas en las variables de entorno. Esto es útil, por ejemplo, en entornos corporativos con sus propias autoridades de certificación (CA).

1.  **Almacenes del sistema:**
    *   **Linux/macOS:** Python suele usar automáticamente los certificados del sistema (por ejemplo, de `/etc/ssl/certs/`). Asegúrese de que su sistema tenga los certificados raíz actualizados (`sudo apt update && sudo apt install ca-certificates` para Debian/Ubuntu, `sudo yum update ca-certificates` para CentOS/RHEL).
    *   **Windows:** Python *puede* intentar usar el almacén del sistema de Windows, but this does not always work reliably without additional packages (e.g., `python-certifi-win32`). It is recommended to use `certifi` (Method 3).
2.  **Variables de entorno:** Puede especificar explícitamente la ruta a un archivo o directorio con certificados:
    *   `SSL_CERT_FILE`: Especifique la ruta a un *archivo* (en formato PEM) que contenga todos los certificados raíz de confianza.
    *   `SSL_CERT_DIR`: Especifique la ruta a un *directorio* donde cada certificado se encuentre en un archivo PEM independiente con un nombre en forma de hash (use `c_rehash` de OpenSSL para preparar el directorio).

    **Cómo establecer variables de entorno:**

    *   **Linux/macOS (temporal, para la sesión actual):**
        ```bash
        export SSL_CERT_FILE=/path/to/your/ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (cmd, temporal):**
        ```cmd
        set SSL_CERT_FILE=C:\path\to\your\ca-bundle.pem
        python your_script.py
        ```
    *   **Windows (PowerShell, temporal):**
        ```powershell
        $env:SSL_CERT_FILE = "C:\path\to\your\ca-bundle.pem"
        python your_script.py
        ```
    Para añadir su propia CA (por ejemplo, corporativa), debe añadir su certificado al archivo `SSL_CERT_FILE` o al directorio `SSL_CERT_DIR`.

## Paso 3 (Extra): Cómo crear un certificado autofirmado para el desarrollo local

    Si está desarrollando un servidor web local (API, sitio web) y quiere probarlo a través de HTTPS, necesitará un certificado SSL. Como no tiene un dominio público para obtener un certificado de una CA normal, puede crear un certificado *autofirmado*.

**Uso de OpenSSL (multiplataforma):**

1.  **Ejecute el comando:** Este comando creará una clave privada (`key.pem`) y el propio certificado (`cert.pem`), válido durante 10 años, para `localhost`.

    ```bash
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/CN=localhost" -addext "subjectAltName = DNS:localhost,IP:127.0.0.1"
    ```
    *   `-nodes`: Crea una clave sin protección por contraseña (conveniente para el desarrollo).
    *   `-subj "/CN=localhost"`: Establece el nombre común.
    *   `-addext "subjectAltName = ..."`: Añade nombres alternativos de sujeto (importante para los navegadores y clientes modernos).

2.  **Use `key.pem` y `cert.pem`** en la configuración de su servidor web local (Flask, Django, Node.js, etc.) para habilitar HTTPS.

**Uso de PowerShell (Windows 10/11):**

1.  **Ejecute el comando en PowerShell (con derechos de administrador):** Este comando creará un certificado y lo colocará en el almacén de certificados del equipo.

    ```powershell
    New-SelfSignedCertificate -DnsName "localhost", "127.0.0.1" -CertStoreLocation "cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5) -FriendlyName "My Localhost Dev Cert"
    ```
    Es posible que necesite exportar este certificado del almacén (`certlm.msc`) a archivos `.pfx` o `.pem` para que lo use su servidor web.

**Nota:** Los navegadores y los clientes HTTP (incluido `requests` de Python por defecto) no confiarán en los certificados autofirmados. Al acceder a dicho servidor, recibirá una advertencia o un error de SSL. Para las pruebas, deberá añadir este certificado a los certificados raíz de confianza de su sistema/navegador, o usar `verify=False` (para `requests`), o especificar la ruta a su `cert.pem` a través de `verify='/path/to/cert.pem'`.
