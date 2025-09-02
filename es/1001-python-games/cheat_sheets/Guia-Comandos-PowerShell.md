**Guía de comandos de PowerShell**

**1. Navegación básica y operaciones con archivos y directorios**

*   **`Get-ChildItem` (o `gci`, `ls`, `dir`)**: Obtiene una lista de archivos y subdirectorios en la ubicación especificada.
    *   **Sintaxis**: `Get-ChildItem [ruta] [parámetros]`
    *   **Parámetros clave:**
        *   `-Path`: Especifica la ruta al directorio.
        *   `-Include`: Filtra por nombre de archivo (con comodines `*` y `?`).
        *   `-Exclude`: Excluye archivos por nombre.
        *   `-Recurse`: Muestra archivos y carpetas en todos los subdirectorios.
        *   `-Force`: Mostrar archivos ocultos.
        *   `-File`: Mostrar solo archivos.
        *   `-Directory`: Mostrar solo carpetas.
    *   **Ejemplos:**
        *   `Get-ChildItem`: Lista de archivos y carpetas en el directorio actual.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: Lista de archivos y carpetas en `C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: Lista solo archivos de texto en el directorio actual.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: Mostrar todos los directorios en la unidad C.
        *  `Get-ChildItem -Force`: Mostrar todos los archivos, incluidos los ocultos.

*   **`Set-Location` (o `sl`, `cd`)**: Cambia el directorio actual.
    *   **Sintaxis**: `Set-Location [ruta]`
    *   **Ejemplos:**
        *   `Set-Location C:\Windows`: Ir al directorio `C:\Windows`.
        *   `Set-Location ..`: Ir al directorio padre.
        * `Set-Location /` - Ir a la raíz de la unidad.
*   **`New-Item`**: Crea un nuevo archivo o directorio.
    *   **Sintaxis**: `New-Item -Path [ruta] -ItemType [tipo] -Name [nombre]`
    *   **Parámetros clave:**
        *   `-ItemType`: `file` o `directory`.
        *   `-Name`: Nombre del nuevo elemento.
        *   `-Value`: Contenido del archivo.
    *   **Ejemplos:**
        *   `New-Item -ItemType directory -Name NewFolder`: Crear una carpeta `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: Crear un archivo vacío `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: Crear `myfile.txt` con contenido.

*  **`Remove-Item` (o `rm`, `del`, `erase`)**: Elimina archivos y directorios.
    *   **Sintaxis:** `Remove-Item [ruta] [parámetros]`
    *   **Parámetros clave:**
         *   `-Recurse`:  Eliminar todos los subdirectorios.
        *   `-Force`: Eliminación forzada (incluidos archivos "solo lectura" y directorios).
       *  `-Confirm` - Pedir confirmación para cada eliminación.
    *   **Ejemplos:**
        *   `Remove-Item myfile.txt`: Eliminar `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: Eliminar la carpeta `C:\Temp` con todas las carpetas y archivos anidados.

*   **`Copy-Item`**: Copia archivos y directorios.
    *   **Sintaxis**: `Copy-Item [ruta_origen] [ruta_destino] [parámetros]`
    *   **Parámetros clave:**
        *   `-Recurse`: Copiar todos los subdirectorios.
        *   `-Force`: Sobrescribir archivos existentes sin preguntar.
    *   **Ejemplos:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: Copiar `myfile.txt` a `mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: Copiar la carpeta `C:\Source` a todos los subdirectorios en la carpeta `D:\Backup`.

*   **`Move-Item`**: Mueve archivos y directorios.
    *   **Sintaxis**: `Move-Item [ruta_origen] [ruta_destino] [parámetros]`
      *  `-Force` - Forzar movimiento y sobrescritura.

    *   **Ejemplos:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: Mover `myfile.txt` a la carpeta `D:\Documents`.
         *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force`: Mover la carpeta C:\MyFolder a D:\ forzosamente, incluso si ya existe una carpeta con ese nombre.

*   **`Rename-Item`**: Cambia el nombre de un archivo o directorio.
    *   **Sintaxis**: `Rename-Item -Path [ruta] -NewName [nuevo_nombre]`
    *   **Ejemplo:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: Cambiar el nombre de `myfile.txt` a `newfile.txt`.

*   **`Get-Content` (o `gc`)**: Muestra u obtiene el contenido de un archivo.
    *   **Sintaxis**: `Get-Content [ruta]`
    *   **Ejemplo:**
        *   `Get-Content myfile.txt`: Mostrar el contenido de `myfile.txt`.
*   **`Set-Content`**: Reemplaza o crea el contenido de un archivo.
    *  **Sintaxis:** `Set-Content [ruta] [parámetros]`
        *  `-value` - texto a escribir.
   *   **Ejemplo:** `Set-Content myfile.txt "Nuevo texto"` - Reemplazar el contenido de `myfile.txt`.

*   **`Add-Content`**: Agrega contenido al final de un archivo.
   * **Sintaxis:** `Add-Content [ruta] [parámetros]`
       *  `-value` - texto a agregar.

   *   **Ejemplo:** `Add-Content myfile.txt "Más texto"` - Agregar texto al final de `myfile.txt`.

**2. Gestión de procesos:**

*   **`Get-Process` (o `gps`)**: Obtiene una lista de procesos en ejecución.
    *   **Sintaxis**: `Get-Process [parámetros]`
    *   **Parámetros clave:**
        *   `-Name`: Filtrar por nombre de proceso.
        *   `-Id`: Filtrar por ID de proceso.
        *    `-IncludeUserName`: Mostrar el usuario que inició el proceso.
    *   **Ejemplos:**
        *   `Get-Process`: Lista de todos los procesos en ejecución.
        *   `Get-Process -Name notepad`: Lista de procesos con nombre `notepad`.
        *    `Get-Process -IncludeUserName`: Lista de todos los procesos en ejecución con usuarios.

*   **`Stop-Process`**: Termina un proceso.
    *   **Sintaxis**: `Stop-Process [parámetros]`
     *  `-Id` - Especificar ID de proceso.
    *   `-Name` - Especificar nombre de proceso.
    *  `-Force` - Forzar la terminación del proceso.
    *   **Ejemplos:**
        *   `Stop-Process -Name notepad`: Terminar todos los procesos `notepad`.
         *    `Stop-Process -Id 1234` : Terminar proceso con ID 1234.
        *    `Stop-Process -Name chrome -Force` : Forzar la terminación de todos los procesos `chrome`.

**3. Gestión de servicios:**

*   **`Get-Service`**: Obtiene una lista de servicios.
    *   **Sintaxis**: `Get-Service [parámetros]`
    *   **Parámetros clave:**
         * `-Name`: Mostrar solo servicios con el nombre especificado.
         * `-DisplayName`: Mostrar solo servicios con el nombre de visualización especificado.
        *   `-Status`: Filtrar por estado (Running, Stopped).
    *   **Ejemplos:**
        *   `Get-Service`: Lista de todos los servicios.
        *   `Get-Service -Name Spooler`: Mostrar el servicio Spooler.
       *   `Get-Service -Status Running`: Mostrar servicios en ejecución.
*  **`Start-Service`**: Inicia un servicio.
   *   **Sintaxis**: `Start-Service [nombre_servicio]`
   *   **Ejemplo:** `Start-Service Spooler` - Iniciar el servicio Spooler.

*   **`Stop-Service`**: Detiene un servicio.
    *   **Sintaxis**: `Stop-Service [nombre_servicio]`
        *  `-Force` - Forzar la detención del servicio.
    *   **Ejemplo:** `Stop-Service Spooler`: Detener el servicio Spooler.
        *   `Stop-Service Spooler -Force` - Forzar la detención del servicio Spooler.

*  **`Restart-Service`**: Reinicia un servicio.
   *   **Sintaxis:** `Restart-Service [nombre_servicio]`
   *   **Ejemplo:** `Restart-Service Spooler` - Reiniciar el servicio Spooler.

**4. Redes**

*   **`Test-NetConnection`**: Prueba la conexión de red.
    *   **Sintaxis**: `Test-NetConnection [nombre_host_o_direccion_ip] [parámetros]`
    *  `-Port` - Número de puerto.
    *   **Ejemplos:**
        *   `Test-NetConnection google.com`: Probar la conexión a `google.com`.
        * `Test-NetConnection google.com -Port 80`: Probar la conexión a google.com en el puerto 80.
*   **`Get-NetIPConfiguration`**: Obtiene la configuración de red.
    *   **Sintaxis**: `Get-NetIPConfiguration`
    *   **Ejemplo:**
        *   `Get-NetIPConfiguration`: Mostrar la configuración de red.
*   **`Resolve-DnsName`**: Consulta información DNS.
    *   **Sintaxis**: `Resolve-DnsName [nombre_host]`
    *   **Ejemplo:** `Resolve-DnsName google.com`: Consultar información DNS para `google.com`.

**5. Operaciones de registro**

*   **`Get-ItemProperty`**: Obtiene el valor de una propiedad del registro.
    *   **Sintaxis**: `Get-ItemProperty -Path [ruta_registro]`
    *   **Ejemplo:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`**: Establece el valor de una propiedad en el registro.
    *   **Sintaxis**: `Set-ItemProperty -Path [ruta_registro] -Name [nombre_propiedad] -Value [valor]`
    *   **Ejemplo:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

**6. Otros**

*   **`Clear-Host`**: Borra la pantalla de la consola.
    *   **Sintaxis:** `Clear-Host`
*   **`Get-Date`**: Obtiene la fecha y hora actuales.
    *   **Sintaxis:** `Get-Date`
*    **`Start-Process`**: Inicia un programa o abre un archivo.
    *   **Sintaxis:** `Start-Process [nombre_programa_o_archivo] [opciones]`
   *   **Ejemplos:**
        *   `Start-Process notepad.exe`: Iniciar el Bloc de notas.
        *   `Start-Process myfile.txt`: Abrir `myfile.txt` con el programa predeterminado.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"` - Abrir sitio web en Chrome.

*   **`Get-Help`**: Muestra la ayuda de un comando.
    *   **Sintaxis**: `Get-Help [nombre_comando]`
    *   **Ejemplo:** `Get-Help Get-Process`: Mostrar la ayuda del comando `Get-Process`.
*   **`Exit`**: Finaliza la sesión de PowerShell.
    *   **Sintaxis:** `Exit`
*  **`Get-Variable`**: Muestra las variables actuales.
    *  **Sintaxis**: `Get-Variable`
*   **`Get-Alias`**: Muestra los alias de comandos.
    *   **Sintaxis**: `Get-Alias`
*   **`Set-Alias`**: Crea un alias para un comando.
    *  **Sintaxis**: `Set-Alias [nombre_alias] [nombre_comando]`
    *  **Ejemplo**: `Set-Alias gci Get-ChildItem`

**Notas:**

*   Los comandos de `PowerShell` (cmdlets) suelen tener la forma `Verbo-Sustantivo` (por ejemplo, `Get-Process`, `Set-Location`).
*   `PowerShell` no distingue entre mayúsculas y minúsculas, por lo que puede escribir comandos como `Get-ChildItem` o `get-childitem`.
*   `PowerShell` trabaja con objetos, por lo que puede usar el operador `|` para canalizar la salida de un comando a la entrada de otro (por ejemplo, `Get-Process | Sort-Object -Property CPU`).
*  Muchos comandos admiten el uso de comodines (*) para trabajar con varios archivos (por ejemplo, `Get-ChildItem *.txt`).
*   Algunos comandos requieren privilegios de administrador.
