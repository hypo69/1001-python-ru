### Cómo comprobar y corregir errores en el disco duro en Windows: chuleta de CHKDSK y PowerShell

Con el tiempo, pueden acumularse errores lógicos en un disco duro o SSD, y pueden aparecer sectores dañados, lo que provoca la ralentización del sistema, fallos de programas e incluso la pérdida de datos. Afortunadamente, Windows dispone de herramientas integradas para diagnosticar y corregir estos problemas.

En esta chuleta, mostraré dos formas de controlar el estado de los discos: la utilidad `chkdsk` y los comandos de PowerShell.

### Parte 1: Utilidad CHKDSK

**CHKDSK** (Check Disk) es una utilidad estándar de línea de comandos que comprueba el sistema de archivos de un volumen en busca de errores lógicos y físicos.

#### Cómo ejecutar CHKDSK

Para ejecutar comandos que realicen cambios en el sistema, necesitará derechos de administrador.

1.  Pulse `Win + S` o el botón "Inicio".
2.  Escriba `cmd` o "Símbolo del sistema".
3.  En los resultados de la búsqueda, haga clic con el botón derecho en "Símbolo del sistema" y seleccione **"Ejecutar como administrador"**.

#### Parámetros principales (modificadores) de CHKDSK

El comando tiene la siguiente sintaxis: `chkdsk [unidad:] [parámetros]`

Parámetros de uso frecuente:

*   `chkdsk C:`
    Inicia la comprobación de la unidad C: en modo "solo lectura". La utilidad informará de los errores encontrados, pero no los corregirá.

*   **/f**
    Corrige errores en el disco. Si hay archivos abiertos en el disco (lo que casi siempre ocurre en el disco del sistema), la utilidad ofrecerá realizar la comprobación en el siguiente reinicio del sistema.
    *Ejemplo:* `chkdsk D: /f`

*   **/r**
    Busca sectores dañados (bad sectors) e intenta recuperar la información que se pueda leer. Este modificador **incluye la funcionalidad del modificador `/f`**, por lo que no es estrictamente necesario utilizarlos juntos, aunque no es un error. Una comprobación con `/r` lleva mucho más tiempo.
    *Ejemplo:* `chkdsk D: /r`

*   **/x**
    Desmonta forzosamente el volumen antes de la comprobación, si es necesario. Todos los identificadores abiertos para este disco dejarán de ser válidos. Este modificador también **incluye la funcionalidad de `/f`**.
    *Ejemplo:* `chkdsk D: /x`

*   **/b** (solo para el sistema de archivos NTFS)
    Realiza una reevaluación de los clústeres dañados en el disco. Este modificador es el más completo, ya que **incluye la funcionalidad de `/r`**.
    *Ejemplo:* `chkdsk C: /b`

*   **/scan** (solo para NTFS)
    Ejecuta una comprobación en línea del volumen. Esto significa que no es necesario desmontar el disco, y puede seguir trabajando en el sistema durante el escaneo. Sin embargo, para corregir los problemas encontrados, será necesario el siguiente modificador o un reinicio.
    *Ejemplo:* `chkdsk C: /scan`

*   **/spotfix** (solo para NTFS)
    Realiza una corrección puntual y muy rápida de errores en el volumen. Requiere desmontar el disco, al igual que el modificador `/f`.
    *Ejemplo:* `chkdsk D: /spotfix`

#### Ejemplos de ejecución de CHKDSK

*   **Comprobación rápida de la unidad D: sin corregir:**
    ```
    chkdsk D:
    ```

*   **Comprobar y corregir errores en la unidad D:**
    ```
    chkdsk D: /f
    ```

*   **Comprobación más completa de la unidad del sistema C: con búsqueda de sectores dañados y su recuperación:**
    ```
    chkdsk C: /f /r
    ```
    *o simplemente:*
    ```
    chkdsk C: /r
    ```

#### ¿Qué hacer si el disco está en uso?

Al intentar ejecutar una comprobación con corrección (`/f` o `/r`) para la unidad del sistema (normalmente `C:`), verá un mensaje:

`No se puede ejecutar el comando CHKDSK porque el volumen especificado está siendo utilizado por otro proceso. ¿Desea programar la comprobación de este volumen la próxima vez que se reinicie el sistema? (S/N)`

Pulse `S`, y luego `Intro`. La comprobación se programará y se iniciará automáticamente en el siguiente reinicio del equipo.

---

### Parte 2: Comandos de PowerShell

PowerShell es un shell de automatización que ofrece comandos modernos y flexibles para la administración del sistema.

#### Cómo ejecutar PowerShell

Al igual que con el Símbolo del sistema, necesitará derechos de administrador.

1.  Pulse `Win + S` o el botón "Inicio".
2.  Escriba `powershell`.
3.  En los resultados de la búsqueda, haga clic con el botón derecho en "Windows PowerShell" y seleccione **"Ejecutar como administrador"**.

#### Comando principal: `Repair-Volume`

En PowerShell, el cmdlet `Repair-Volume` se utiliza para comprobar y corregir discos.

Sначала puede ser útil ver una lista de todos los volúmenes del sistema con el comando:
```powershell
Get-Volume
```

#### Parámetros principales de `Repair-Volume`

*   `-DriveLetter`
    Especifica la letra de la unidad que se va a comprobar.

*   `-Scan`
    Escanea el volumen en busca de errores e informa de ellos. Esto es análogo a `chkdsk` sin modificadores.
    *Ejemplo:* `Repair-Volume -DriveLetter D -Scan`

*   `-SpotFix`
    Realiza una corrección rápida en línea sin necesidad de desmontar el volumen durante mucho tiempo. Análogo a `chkdsk /spotfix`.
    *Ejemplo:* `Repair-Volume -DriveLetter D -SpotFix`

*   `-OfflineScanAndFix`
    Realiza una comprobación y corrección completa del disco sin conexión. Este es el análogo más completo del comando `chkdsk /f /r`. El sistema pedirá un reinicio si el volumen está en uso.
    *Ejemplo:* `Repair-Volume -DriveLetter C -OfflineScanAndFix`

#### Ejemplos de PowerShell

*   **Escanear la unidad C: en busca de errores (sin corregir):**
    ```powershell
    Repair-Volume -DriveLetter C -Scan
    ```
    Verá el resultado en el campo `HealthStatus` (por ejemplo, `Healthy` o `Needs-Repair`).

*   **Realizar una corrección rápida para la unidad D:**
    ```powershell
    Repair-Volume -DriveLetter D -SpotFix
    ```

*   **Programar una comprobación y corrección completa para la unidad del sistema C: en el siguiente reinicio:**
    ```powershell
    Repair-Volume -DriveLetter C -OfflineScanAndFix
    ```
    PowerShell, al igual que `chkdsk`, le notificará la necesidad de un reinicio y programará la tarea.


Para la mayoría de los usuarios, el resultado de `chkdsk C: /r` y `Repair-Volume -DriveLetter C -OfflineScanAndFix` será el mismo. La elección depende de sus preferencias y tareas.

**Nota importante:** Antes de realizar cualquier operación seria en el disco, especialmente si sospecha problemas físicos, **¡siempre haga una copia de seguridad de los datos importantes!** Las herramientas pueden corregir errores, pero no pueden garantizar el 100% de la integridad de los datos en un medio dañado.