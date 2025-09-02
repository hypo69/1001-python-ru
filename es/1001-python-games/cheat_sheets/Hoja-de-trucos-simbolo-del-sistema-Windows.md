**1. Gestión de archivos y directorios:**

*   **`attrib`**: Muestra o cambia los atributos de un archivo o directorio (oculto, solo lectura, archivo, etc.).
    *   **Sintaxis:** `attrib [+r|-r] [+a|-a] [+s|-s] [+h|-h] [unidad:][ruta]nombre_archivo`
    *   **Opciones:**
        *   `+r`: Establecer atributo "solo lectura"
        *   `-r`: Quitar atributo "solo lectura"
        *   `+a`: Establecer atributo "archivo"
        *   `-a`: Quitar atributo "archivo"
        *   `+s`: Establecer atributo "sistema"
        *   `-s`: Quitar atributo "sistema"
        *   `+h`: Establecer atributo "oculto"
        *   `-h`: Quitar atributo "oculto"
    *   **Ejemplos:**
        *   `attrib +h myfile.txt`: Ocultar `myfile.txt`.
        *   `attrib -r myfile.txt`: Quitar atributo "solo lectura" de `myfile.txt`.
        *   `attrib *.*`: Mostrar atributos de todos los archivos en el directorio actual.

*   **`cd` o `chdir`**: Cambia el directorio actual.
    *   **Sintaxis:** `cd [ruta]` o `chdir [ruta]`
    *   **Opciones:**
        *   `..`: Ir al directorio padre.
        *   `\`: Ir a la raíz de la unidad.
    *   **Ejemplos:**
        *   `cd Documents`: Ir a la carpeta `Documents` en el directorio actual.
        *   `cd C:\Users\User\Downloads`: Ir a la carpeta `Downloads` en la unidad C.
        *   `cd ..`: Ir al directorio padre.
        *   `cd \`: Ir a la raíz de la unidad actual.

*   **`copy`**: Copia uno o más archivos.
    *   **Sintaxis:** `copy [archivo_origen] [archivo_destino]`
    *   **Opciones:**
        *  `/a` - Copiar archivo ASCII
        *  `/b` - Copiar archivo binario
        *  `/v` - Verificar que los archivos se copiaron correctamente
    *   **Ejemplos:**
        *   `copy myfile.txt mycopy.txt`: Copiar `myfile.txt` a `mycopy.txt`.
        *   `copy *.txt C:\Backup`: Copiar todos los archivos con extensión `.txt` a la carpeta `C:\Backup`.

*   **`del` o `erase`**: Elimina uno o más archivos.
    *   **Sintaxis:** `del [nombre_archivo]` o `erase [nombre_archivo]`
    *   **Opciones:**
        *   `/p`: Pedir confirmación antes de eliminar cada archivo.
        *   `/f`: Eliminar archivos "solo lectura".
        *   `/s`: Eliminar archivos de subdirectorios.
        *   `/q` - Eliminar archivos sin preguntar.
    *   **Ejemplos:**
        *   `del myfile.txt`: Eliminar `myfile.txt`.
        *   `del *.tmp`: Eliminar todos los archivos con extensión `.tmp`.
        *   `del /f /s *.log` - Eliminar todos los archivos con extensión .log en el directorio actual y todos los subdirectorios, sin confirmación.

*   **`dir`**: Muestra una lista de archivos y directorios en el directorio actual.
    *   **Sintaxis:** `dir [ruta] [opciones]`
    *   **Opciones:**
        *   `/a`: Mostrar todos los archivos (incluidos los ocultos).
        *   `/w`: Mostrar lista en formato ancho.
        *   `/p`: Mostrar lista página por página.
        *   `/s`: Mostrar archivos también de subdirectorios.
        *   `/b` - Mostrar solo el nombre del archivo.
    *   **Ejemplos:**
        *   `dir`: Mostrar una lista de archivos y directorios en el directorio actual.
        *   `dir C:\Users\User\Documents /a`: Mostrar todos los archivos en el directorio `Documents`.
        *   `dir /w`: Mostrar una lista de archivos y directorios en el directorio actual en formato ancho.
         *   `dir /b /s *.txt`: Mostrar todos los archivos *.txt con la ruta completa.

*   **`mkdir` o `md`**: Crea un nuevo directorio.
    *   **Sintaxis:** `mkdir [ruta]` o `md [ruta]`
    *   **Ejemplos:**
        *   `mkdir NewFolder`: Crear una nueva carpeta `NewFolder` en el directorio actual.
        *   `mkdir C:\Backup`: Crear una nueva carpeta `Backup` en la unidad `C`.

*   **`move`**: Mueve uno o más archivos o directorios.
    *   **Sintaxis:** `move [archivo_origen] [archivo_destino]`
    *   **Ejemplos:**
        *   `move myfile.txt C:\Documents`: Mover `myfile.txt` a la carpeta `C:\Documents`.
        *  `move dir1 dir2` - Mover la carpeta `dir1` a la carpeta `dir2`.

*  **`rd` o `rmdir`**: Elimina un directorio.
    *   **Sintaxis:** `rd [ruta]` o `rmdir [ruta]`
    *   **Opciones:**
         *   `/s`: Eliminar directorio con todos sus subdirectorios.
        *   `/q` - Eliminar directorio sin preguntar.
    *   **Ejemplos:**
        *   `rd myfolder`: Eliminar la carpeta vacía `myfolder`.
        *  `rd /s /q myfolder` - Eliminar la carpeta `myfolder` con todo su contenido sin preguntar.

*   **`ren` o `rename`**: Cambia el nombre de un archivo o directorio.
    *   ****Sintaxis:** `ren [nombre_antiguo] [nombre_nuevo]`
    *   **Ejemplos:**
        *   `ren myfile.txt newfile.txt`: Cambiar el nombre de `myfile.txt` a `newfile.txt`.

*   **`type`**: Muestra el contenido de un archivo de texto.
    *   **Sintaxis:** `type [nombre_archivo]`
    *   **Ejemplo:** `type myfile.txt`: Mostrar el contenido de `myfile.txt`.

*   **`xcopy`**: Copia archivos y directorios (incluidos subdirectorios).
    *   **Sintaxis:** `xcopy [origen] [destino] [opciones]`
    *   **Opciones:**
        *   `/s`: Copiar directorios y subdirectorios (excepto los vacíos).
        *   `/e`: Copiar directorios y subdirectorios (incluidos los vacíos).
        *   `/i`: Si el destino no existe, crearlo.
        *   `/y`: Suprimir la solicitud de confirmación de sobrescritura.
        *  `/d` - Copiar solo archivos nuevos.
    *   **Ejemplos:**
        *   `xcopy C:\Source D:\Destination /s`: Copiar el directorio `C:\Source` a todos los subdirectorios en la carpeta `D:\Destination`.
        *   `xcopy C:\Source D:\Destination /e /y`: Copiar el directorio `C:\Source` a todos los subdirectorios en la carpeta `D:\Destination`, incluidos los vacíos y sin preguntar para sobrescribir.

**2. Operaciones de disco:**

*   **`diskpart`**: Inicia la utilidad de administración de discos (particiones, volúmenes).
    *   **Sintaxis:** `diskpart`
    *   **Notas:**
        *   `diskpart` es una utilidad interactiva que tiene su propio conjunto de comandos.
        *   Se requieren privilegios de administrador para usarla.
        *   Puede obtener más información sobre el uso de `diskpart` con el comando `help` dentro de esta utilidad.
*   **`format`**: Formatea un disco.
    *   **Sintaxis:** `format [unidad:] [opciones]`
    *   **Opciones:**
        *  `/q` - Formato rápido
        *  `/fs:file-system` - Elegir tipo de sistema de archivos (por ejemplo, NTFS, FAT32)
    *   **Ejemplos:**
        *   `format D: /q`: Formato rápido de la unidad D:.
        *   `format E: /fs:NTFS`: Formato de la unidad E: al sistema de archivos NTFS.
    *   **Advertencia:** ¡Formatear una unidad elimina todos los datos en ella!
*   **`label`**: Establece o cambia la etiqueta del disco.
    *   **Sintaxis:** `label [unidad:][etiqueta]`
    *   **Ejemplos:**
        * `label D: NewLabel` - Establecer la etiqueta en la unidad D como NewLabel.
        * `label D:` - Borrar la etiqueta de la unidad D.

**3. Gestión del sistema:**

*   **`cls`**: Borra la pantalla del símbolo del sistema.
    *   **Sintaxis:** `cls`
*   **`date`**: Muestra o cambia la fecha actual.
    *   **Sintaxis:** `date [nueva_fecha]`
    *   **Ejemplos:**
        *   `date`: Mostrar la fecha actual.
        *   `date 12-25-2024`: Cambiar la fecha al 25 de diciembre de 2024.
*   **`exit`**: Sale del símbolo del sistema.
    *   **Sintaxis:** `exit`
*   **`shutdown`**: Apaga o reinicia la computadora.
    *   **Sintaxis:** `shutdown [opciones]`
    *   **Opciones:**
        *   `/s`: Apagar la computadora.
        *   `/r`: Reiniciar la computadora.
        *   `/a`: Abortar el apagado o reinicio.
        *  `/t xxx` - Retraso en segundos antes del apagado o reinicio.
    *   **Ejemplos:**
        *   `shutdown /s /t 60`: Apagar la computadora en 60 segundos.
        *   `shutdown /r`: Reiniciar la computadora.
        *   `shutdown /a`: Abortar el apagado o reinicio programado.
*   **`tasklist`**: Muestra una lista de procesos en ejecución.
    *   **Sintaxis:** `tasklist [opciones]`
    *  `/v` - Información adicional.
    *  `/fo csv` - Salida en formato CSV.
    *  `/fi "nombre_imagen eq notepad.exe"` - Encontrar todos los procesos del bloc de notas.
    *   **Ejemplos:**
        *   `tasklist`: Mostrar una lista de procesos en ejecución.
        *   `tasklist /v`: Mostrar una lista de procesos en ejecución con información detallada.

*   **`taskkill`**: Termina un proceso.
    *   **Sintaxis:** `taskkill [opciones]`
    *   **Opciones:**
         * `/im nombre_imagen` - Terminar proceso por nombre.
        *   `/pid pid` - Terminar proceso por ID.
        *   `/f` - Forzar la terminación del proceso.
     *   **Ejemplos:**
        *   `taskkill /im notepad.exe`: Terminar todos los procesos llamados `notepad.exe`.
        *   `taskkill /pid 1234`: Terminar proceso con ID 1234.
        *  `taskkill /im notepad.exe /f` - Forzar la terminación de todos los procesos `notepad.exe`.
*   **`time`**: Muestra o cambia la hora actual.
    *   **Sintaxis:** `time [nueva_hora]`
    *   **Ejemplos:**
        *   `time`: Mostrar la hora actual.
        *   `time 15:30`: Establecer la hora en 15:30.
*   **`ver`**: Muestra la versión del sistema operativo.
    *   **Sintaxis:** `ver`
*   **`systeminfo`**: Muestra información detallada del sistema.
    *   **Sintaxis:** `systeminfo`

*   **`taskmgr`**: Inicia el Administrador de tareas.
    *  **Sintaxis:** `taskmgr`

**4. Red:**

*   **`ipconfig`**: Muestra la configuración de red.
    *   **Sintaxis:** `ipconfig [opciones]`
    *   **Opciones:**
        *   `/all`: Mostrar información completa sobre los adaptadores de red.
        *   `/release`: Liberar dirección IP.
        *   `/renew`: Solicitar una nueva dirección IP.
    *   **Ejemplos:**
        *   `ipconfig`: Mostrar la configuración básica de red.
        *   `ipconfig /all`: Mostrar información completa sobre todos los adaptadores de red.
        * `ipconfig /release` - Liberar dirección IP.
        * `ipconfig /renew` - Solicitar una nueva dirección IP.
*   **`ping`**: Envía una solicitud de eco a otra computadora en la red.
    *   **Sintaxis:** `ping [nombre_host_o_direccion_ip] [opciones]`
     *  `-n xxx` - Número de solicitudes.
     *  `-t` - Hacer ping indefinidamente.
    *   **Ejemplos:**
        *   `ping google.com`: Hacer ping al servidor `google.com`.
        *   `ping 192.168.1.100`: Hacer ping a la computadora con la dirección IP `192.168.1.100`.
        *  `ping google.com -n 10` - Realizar 10 pings.
*   **`tracert`**: Muestra la ruta de los paquetes a otra computadora en la red.
    *   **Sintaxis:** `tracert [nombre_host_o_direccion_ip]`
    *   **Ejemplo:** `tracert google.com`: Mostrar la ruta de los paquetes a `google.com`.
*   **`netstat`**: Muestra las conexiones de red.
    *   **Sintaxis:** `netstat [opciones]`
    *   **Opciones:**
         *   `-a`: Muestra todas las conexiones.
        *   `-b`: Muestra las aplicaciones que crearon conexiones.
    *   **Ejemplos:**
        * `netstat` - Mostrar todas las conexiones activas.
        * `netstat -a -b` - Mostrar todas las conexiones y las aplicaciones que las abrieron.

*   **`nslookup`**: Consulta información DNS.
    *   **Sintaxis:** `nslookup [nombre_host]`
    *   **Ejemplo:** `nslookup google.com`: Consultar información DNS para `google.com`.

**5. Otros comandos:**

*   **`assoc`**: Muestra o cambia las asociaciones de archivos.
    *   **Sintaxis:** `assoc [.extension]=[tipo_archivo]`
    *   **Ejemplos:**
        *   `assoc .txt`: Mostrar el tipo de archivo para la extensión `.txt`.
        *   `assoc .txt=txtfile`: Establecer el tipo de archivo para la extensión `.txt` como `txtfile`.
*   **`call`**: Llama a un archivo por lotes desde otro.
    *   **Sintaxis:** `call [nombre_archivo_por_lotes]`
    *   **Ejemplo:** `call mybatch.bat`: Llamar al archivo por lotes `mybatch.bat`.
*   **`chcp`**: Cambia la página de códigos de la consola.
    *   **Sintaxis:** `chcp [numero_pagina_de_codigos]`
    *   **Ejemplos:**
        *   `chcp 1251`: Establecer la página de códigos para cirílico.
        *   `chcp`: Mostrar la página de códigos actual.
*   **`choice`**: Permite al usuario elegir de una lista de opciones.
    *   **Sintaxis:** `choice [/c [opciones]] [/n] [/t [segundos]] [/d [opcion]] [texto]`
    *   **Opciones:**
        *   `/c`: Especifica las opciones disponibles.
        *   `/n`: Oculta la lista de opciones disponibles.
        *   `/t`: Especifica el tiempo de espera (en segundos).
        *   `/d`: Especifica la opción predeterminada.
    *   **Ejemplo:** `choice /c yn /t 10 /d n "¿Realmente desea salir?"
*   **`find`**: Busca una cadena de texto en un archivo.
    *   **Sintaxis:** `find "cadena" [nombre_archivo]`
    *   **Ejemplos:**
        *   `find "Hello" myfile.txt` - Busca la cadena "Hello" en el archivo myfile.txt.

*   **`findstr`**: Busca cadenas de texto en archivos (más potente que `find`).
    *   **Sintaxis:** `findstr [opciones] "cadena" [nombre_archivo]`
    *   **Opciones:**
         *  `/i` - Búsqueda sin distinción entre mayúsculas y minúsculas.
        *   `/n` - Mostrar números de línea.
        *   `/s` - Buscar en todos los subdirectorios.
    *   **Ejemplos:**
        *   `findstr /i "error" myfile.log`: Busca la cadena "error" (sin distinción entre mayúsculas y minúsculas) en `myfile.log`.
        * `findstr /n "error" *.log` - Busca la cadena "error" en todos los archivos .log, y muestra los números de línea.

*   **`gpupdate`**: Actualiza las políticas de grupo.
    *   **Sintaxis:** `gpupdate [opciones]`
    *   **Opciones:**
         *  `/force` - Forzar actualización.
    *   **Ejemplo:** `gpupdate /force` - Forzar la actualización de las políticas de grupo.
*   **`help` o `/?`**: Muestra la ayuda de un comando.
    *   **Sintaxis:** `help [nombre_comando]` o `[nombre_comando] /?`
    *   **Ejemplo:** `help dir` o `dir /?`: Mostrar la ayuda del comando `dir`.
*   **`pause`**: Pausa la ejecución de un archivo por lotes y espera una pulsación de tecla.
    *   **Sintaxis:** `pause`
*  **`path`**: Muestra o cambia las variables de entorno PATH.
   *   **Sintaxis**: `path [ruta]`
   *   **Ejemplos**: 
         *  `path`: Mostrar el valor actual de la variable PATH.
        *  `path C:\bin` - Agregar la carpeta C:\bin a la variable PATH.
*   **`prompt`**: Configura la cadena de comandos.
    *   **Sintaxis:** `prompt [texto]`
    *   **Ejemplos:**
        *   `prompt $p$g`: Establecer la cadena de comandos para la ruta actual.
        *   `prompt MyPrompt>`: Establecer la cadena de comandos `MyPrompt>`.
*   **`set`**: Muestra, establece o elimina variables de entorno.
    *   **Sintaxis:** `set [nombre=[valor]]`
    *   **Ejemplos:**
        *   `set`: Mostrar todas las variables de entorno.
        *   `set myvar=myvalue`: Establecer la variable de entorno `myvar` en `myvalue`.
        *   `set myvar=`: Eliminar la variable de entorno `myvar`.
*   **`start`**: Inicia un programa o abre un archivo.
    *   **Sintaxis:** `start [nombre_programa_o_archivo] [opciones]`
    *   **Ejemplos:**
        *   `start notepad.exe`: Iniciar el Bloc de notas.
        *   `start myfile.txt`: Abrir el archivo `myfile.txt` con el programa predeterminado.
        *   `start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com"` - Abrir un sitio web en Chrome.
*   **`tree`**: Muestra la estructura gráfica de directorios.
    *   **Sintaxis:** `tree [unidad:][ruta] [opciones]`
    *   **Opciones:**
        * `/f`: Mostrar también los nombres de archivo.
        * `/a` - Usar caracteres ASCII.
    *   **Ejemplos:**
         *   `tree` - Mostrar la estructura del directorio actual.
         *   `tree /f` - Mostrar la estructura del directorio actual con archivos.

*   **`where`**: Encuentra la ubicación de un archivo.
    *   **Sintaxis:** `where [nombre_archivo]`
    *   **Ejemplo:** `where notepad.exe`

**6. Comandos para archivos por lotes:**

*   **`echo`**: Muestra texto en la pantalla.
    *   **Sintaxis:** `echo [texto]`
    *  `echo on` - Habilitar la visualización de comandos al ejecutar el archivo por lotes.
    *  `echo off` - Deshabilitar la visualización de comandos al ejecutar el archivo por lotes.
    *   **Ejemplos:**
        *   `echo Hello, world!`: Mostrar "Hello, world!".
        *   `echo off` - Deshabilitar la salida de comandos.
        *  `echo on` - Habilitar la salida de comandos.
*   **`rem`**: Agrega un comentario a un archivo por lotes.
    *   **Sintaxis:** `rem [comentario]`
    *   **Ejemplo:** `rem This is a comment`
*   **`goto`**: Salta a una etiqueta.
    *   **Sintaxis:** `goto [etiqueta]`
    *   **Ejemplo:**
        ```batch
        :start
        echo Hello
        goto end
        echo This will not be displayed
        :end
        echo Goodbye
        ```
*   **`if`**: Ejecuta lógica condicional.
    *   **Sintaxis:** `if [not] condition (comando1) else (comando2)`
    *   **Ejemplos:**
         * `if exist file.txt echo file exists` - Comprobar la existencia de un archivo.
         * `if %var%== "text" echo variable has value` - Comprobar el valor de una variable.
*  **`for`**: Ejecuta una acción cíclica.
  * **Sintaxis:** `for %%variable in (conjunto) do [comando]`
  * **Ejemplo:**
        ```batch
        for %%a in (*.txt) do (
         echo %%a
         type %%a
         echo -------------
        )
       ```
       * Mostrar el nombre de cada archivo `.txt` y su contenido.

**Advertencia:**
*   Tenga cuidado al usar comandos que puedan modificar el sistema, especialmente cuando se usan con privilegios de administrador.
*   Antes de ejecutar el comando `format`, asegúrese de haber seleccionado la unidad correcta.
