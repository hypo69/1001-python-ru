# cmd

## Categoría: Shells del Sistema

### Propósito: Símbolo del sistema clásico de Windows.

### Introducción
El Símbolo del sistema de Windows (`cmd.exe`) es un intérprete de línea de comandos para los sistemas operativos Windows. Permite a los usuarios ejecutar comandos para realizar diversas tareas, gestionar archivos y directorios, configurar ajustes del sistema y mucho más. Proporciona una interfaz basada en texto para interactuar con el sistema operativo.

### Comandos Importantes y Ejemplos

Aquí se presentan algunos comandos esenciales de `cmd` y su uso:

#### 1. `dir` - Muestra una lista de archivos y subdirectorios

El comando `dir` muestra una lista de archivos y subdirectorios dentro de un directorio especificado.

```cmd
dir [unidad:][ruta][nombre_archivo] [/A[[:]atributos]] [/B] [/C] [/D] [/L] [/N] [/O[[:]orden_clasificacion]] [/P] [/Q] [/R] [/S] [/T[[:]campo_hora]] [/W] [/X] [/4]
```

**Banderas/Parámetros**:
*   `/A[[:]atributos]`: Muestra archivos con atributos especificados.
    *   `D`: Directorios
    *   `R`: Archivos de solo lectura
    *   `H`: Archivos ocultos
    *   `A`: Archivos listos para archivar
    *   `S`: Archivos del sistema
    *   `I`: Archivos no indexados por contenido
    *   `L`: Puntos de reanálisis
    *   `O`: Archivos sin conexión
    *   `-`: Prefijo que significa "no" (por ejemplo, `/A:-H` para excluir archivos ocultos).
*   `/B`: Utiliza formato simple (sin encabezado ni resumen), listando solo el nombre del directorio o el nombre y la extensión del archivo.
*   `/S`: Muestra archivos en el directorio especificado y todos los subdirectorios.
*   `/P`: Hace una pausa después de cada pantalla de información.
*   `/O[[:]orden_clasificacion]`: Ordena la salida.
    *   `N`: Alfabéticamente por nombre.
    *   `E`: Alfabéticamente por extensión.
    *   `S`: Por tamaño, el más pequeño primero.
    *   `D`: Por fecha/hora, el más antiguo primero.
    *   `G`: Agrupa los directorios primero.
    *   `-`: Prefijo para invertir el orden de clasificación.
*   `/W`: Utiliza formato de lista ancha.
*   `/?`: Muestra la ayuda para el comando.

**Ejemplos**:
*   `dir`: Lista archivos y directorios en el directorio actual.
*   `dir /S`: Lista todos los archivos y subdirectorios en el directorio actual y sus subdirectorios.
*   `dir *.txt`: Lista todos los archivos con extensión `.txt` en el directorio actual.
*   `dir /A:H`: Lista archivos ocultos.
*   `dir /S /B *.log > logs.txt`: Encuentra todos los archivos `.log` en el directorio actual y subdirectorios, los lista en formato simple y redirige la salida a `logs.txt`.

**Condiciones de Éxito**:
*   El comando se ejecuta y muestra la lista de directorios solicitada.
*   No se muestran mensajes de error.
*   El comando normalmente devuelve un código de salida de `0`.

**Condiciones de Fallo**:
*   "Archivo no encontrado": Si la ruta o el patrón de nombre de archivo especificado no existe.
*   "Acceso denegado.": Si no tiene los permisos necesarios para acceder al directorio.
*   Si la salida se redirige a un archivo y el directorio para el archivo de salida no existe, podría resultar en un "Error de creación de archivo".

#### 2. `copy` - Copia uno o más archivos

El comando `copy` duplica uno o más archivos de una ubicación a otra.

```cmd
copy [/D] [/V] [/N] [/Y | /-Y] [/Z] [/L] [/A | /B] origen [/A | /B] [+ origen [/A | /B] [+ ...]] [destino [/A | /B]] [/?]
```

**Banderas/Parámetros**:
*   `origen`: Especifica el(los) archivo(s) a copiar. Se pueden usar comodines (`*`, `?`).
*   `destino`: Especifica el directorio y/o nombre de archivo para el(los) nuevo(s) archivo(s).
*   `/V`: Verifica que los nuevos archivos se escriban correctamente.
*   `/Y`: Suprime las solicitudes de confirmación para sobrescribir un archivo de destino existente.
*   `/-Y`: Fuerza la solicitud de confirmación para sobrescribir un archivo de destino existente.
*   `/A`: Indica un archivo de texto ASCII.
*   `/B`: Indica un archivo binario.
*   `/Z`: Copia archivos en modo reiniciable, útil para archivos grandes a través de una red.
*   `/?`: Muestra la ayuda para el comando.

**Ejemplos**:
*   `copy archivo.txt C:\backup`: Copia `archivo.txt` del directorio actual a `C:\backup`.
*   `copy *.doc C:\reports /V`: Copia todos los archivos `.doc` del directorio actual a `C:\reports` y verifica la copia.
*   `copy C:\source\file1.txt + C:\source\file2.txt C:\destination\combined.txt`: Combina `archivo1.txt` y `archivo2.txt` en `combined.txt`.
*   `copy D:\readme.htm`: Copia `readme.htm` de la unidad D: al directorio actual.

**Condiciones de Éxito**:
*   El(los) archivo(s) se copian al destino sin mensajes de error.
*   Se muestra un mensaje como "1 archivo(s) copiado(s).".
*   El `ERRORLEVEL` es `0`.

**Condiciones de Fallo**:
*   "El sistema no puede encontrar el archivo especificado.": Si el archivo de origen no existe.
*   "Acceso denegado.": Si no tiene permisos de escritura en el directorio de destino o permisos de lectura para el archivo de origen.
*   "No hay suficiente espacio en el disco.": Si la unidad de destino está llena.
*   Si se usa `/V` y la verificación falla, aparecerá un mensaje de error.
*   `ERRORLEVEL` será distinto de cero (por ejemplo, `1` para un fallo general).

#### 3. `ping` - Verifica la conectividad a nivel de IP

El comando `ping` envía mensajes de solicitud de eco del Protocolo de mensajes de control de Internet (ICMP) a un host de destino para verificar la conectividad a nivel de IP.

```cmd
ping [/t] [/a] [/n recuento] [/l tamaño] [/f] [/i TTL] [/v TOS] [/r recuento] [/s recuento] [{/j lista_hosts | /k lista_hosts}] [/w tiempo_espera] [/R] [/S dir_origen] [/4] [/6] nombre_destino
```

**Banderas/Parámetros**:
*   `nombre_destino`: Especifica el nombre de host o la dirección IP del destino.
*   `/t`: Hace ping al host especificado hasta que se interrumpe (Ctrl+C para detener, Ctrl+Break para mostrar estadísticas).
*   `/a`: Resuelve direcciones a nombres de host.
*   `/n recuento`: Especifica el número de solicitudes de eco a enviar (el valor predeterminado es 4).
*   `/l tamaño`: Especifica el tamaño del búfer de envío en bytes (el valor predeterminado es 32).
*   `/w tiempo_espera`: Especifica el tiempo de espera en milisegundos para cada respuesta (el valor predeterminado es 4000ms).
*   `/?`: Muestra la ayuda para el comando.

**Ejemplos**:
*   `ping google.com`: Hace ping a `google.com` cuatro veces.
*   `ping 192.168.1.1 -n 10`: Hace ping a la dirección IP `192.168.1.1` diez veces.
*   `ping localhost`: Hace ping a la máquina local.
*   `ping -t 8.8.8.8`: Hace ping continuamente al servidor DNS de Google hasta que se detiene manualmente.

**Condiciones de Éxito**:
*   "Respuesta desde <dirección IP>": Indica una respuesta exitosa del destino.
*   "TTL=" en la salida.
*   Un resumen que muestra "Paquetes: enviados = X, recibidos = X, perdidos = 0 (0% de pérdida)".
*   El comando devuelve un código de salida de `0`.

**Condiciones de Fallo**:
*   "Tiempo de espera agotado.": El destino no respondió dentro del tiempo de espera especificado.
*   "Host de destino inaccesible.": No se pudo encontrar una ruta al host de destino.
*   "La solicitud de ping no pudo encontrar el host <nombre_host>. Compruebe el nombre e inténtelo de nuevo.": El nombre de host no se pudo resolver a una dirección IP (problema de DNS).
*   "Fallo general.": Indica un problema con la interfaz de red local.
*   Un resumen que muestra "Paquetes: enviados = X, recibidos = Y, perdidos = Z (Z% de pérdida)" donde Z > 0.
*   El comando devuelve un código de salida distinto de cero (por ejemplo, `1` si el host es inaccesible).

#### 4. `mkdir` (o `md`) - Crea un directorio

El comando `mkdir` crea un nuevo directorio o subdirectorio.

```cmd
mkdir [unidad:]ruta
```

**Banderas/Parámetros**:
*   `[unidad:]ruta`: Especifica la unidad y la ruta del directorio a crear.
*   `/?`: Muestra la ayuda para el comando.
*   (Nota: La bandera `-p` para crear directorios padre, común en sistemas tipo Unix, no es una bandera estándar de `cmd`. Las extensiones de comando en Windows permiten crear directorios intermedios en una ruta especificada con un solo comando `mkdir`, de manera similar a `-p` en algunos casos).

**Ejemplos**:
*   `mkdir nueva_carpeta`: Crea un directorio llamado `nueva_carpeta` en el directorio actual.
*   `mkdir C:\projects\my_project`: Crea `mi_proyecto` dentro de `C:\projects`. Si `C:\projects` no existe, `cmd` con las extensiones de comando habilitadas lo creará.
*   `md "Mis Documentos"`: Crea un directorio llamado "Mis Documentos" (se necesitan comillas debido al espacio).

**Condiciones de Éxito**:
*   El directorio se crea sin mensajes de error.
*   Normalmente no se muestra ninguna salida en caso de éxito.
*   El `ERRORLEVEL` es `0`.

**Condiciones de Fallo**:
*   "Ya existe un subdirectorio o archivo <nombre_directorio>.": Si ya existe un directorio con el mismo nombre en la ubicación especificada.
*   "El sistema no puede encontrar la ruta especificada.": Si un directorio intermedio en la ruta no existe y las extensiones de comando están deshabilitadas (o si la ruta no es válida).
*   "Acceso denegado.": Si no tiene permisos de escritura en el directorio padre.
*   El `ERRORLEVEL` es distinto de cero (por ejemplo, `1`).

#### 5. `del` (o `erase`) - Elimina uno o más archivos

El comando `del` elimina uno o más archivos.

```cmd
del [/p] [/f] [/s] [/q] [/a[:atributos]] nombres
```

**Banderas/Parámetros**:
*   `nombres`: Especifica una lista de uno o más archivos a eliminar. Se pueden usar comodines (`*`, `?`).
*   `/P`: Solicita confirmación antes de eliminar cada archivo.
*   `/F`: Fuerza la eliminación de archivos de solo lectura.
*   `/S`: Elimina los archivos especificados de todos los subdirectorios. Muestra los nombres de los archivos a medida que se eliminan.
*   `/Q`: Modo silencioso; suprime las solicitudes de confirmación de eliminación.
*   `/A[:atributos]`: Elimina archivos según los atributos.
    *   `R`: Archivos de solo lectura
    *   `H`: Archivos ocultos
    *   `S`: Archivos del sistema
    *   `A`: Archivos listos para archivar
    *   `-`: Prefijo que significa "no"
*   `/?`: Muestra la ayuda para el comando.

**Ejemplos**:
*   `del archivo_antiguo.txt`: Elimina `archivo_antiguo.txt` del directorio actual.
*   `del *.bak /Q`: Elimina todos los archivos con extensión `.bak` en el directorio actual sin preguntar.
*   `del /S /Q C:\temp\*.*`: Elimina todos los archivos en `C:\temp` y sus subdirectorios sin preguntar.
*   `del /F archivo_solo_lectura.txt`: Fuerza la eliminación de un archivo de solo lectura llamado `archivo_solo_lectura.txt`.

**Condiciones de Éxito**:
*   El(los) archivo(s) se eliminan sin mensajes de error.
*   Si no se usa `/P`, es posible que no haya salida en caso de éxito, o un mensaje como "Archivo eliminado - <nombre_archivo>" si se usa `/S`.
*   El `ERRORLEVEL` es `0`.

**Condiciones de Fallo**:
*   "No se pudo encontrar <nombre_archivo>": Si el archivo especificado no existe.
*   "Acceso denegado.": Si no tiene los permisos necesarios para eliminar el archivo, o si el archivo está en uso por otro proceso y `/F` no es suficiente.
*   "El proceso no puede acceder al archivo porque está siendo utilizado por otro proceso.": Si el archivo está bloqueado por otra aplicación.
*   `del` eliminará archivos dentro de un directorio si se proporciona un nombre de directorio, pero no eliminará el directorio en sí. Para eliminar directorios, use `rmdir`.
*   El `ERRORLEVEL` es distinto de cero.

### Lectura Adicional
Para obtener información más detallada, consulte la documentación oficial de `cmd`.

```