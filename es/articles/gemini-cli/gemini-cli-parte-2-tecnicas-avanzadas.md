## Gemini CLI: Técnicas avanzadas y automatización de scripts (Parte 2)

En la primera parte, cubrimos los conceptos básicos: instalación, autenticación y ejecución de comandos individuales. Ahora pasemos al siguiente nivel. En esta parte, enseñaremos a Gemini CLI a realizar escenarios complejos y de varios pasos que se pueden guardar, reutilizar y compartir con el equipo. Esto convertirá la herramienta de un simple asistente en un potente motor para la automatización.

### Mecanismo de ejecución de scripts

La idea clave es usar archivos `.md` como "recetas" o "scripts" para Gemini. Dentro de dicho archivo, describimos en lenguaje natural la secuencia de acciones que la IA debe realizar.

Para ejecutar un script, usaremos la herramienta incorporada `ReadFile`. Simplemente le pediremos a Gemini que lea el archivo con las instrucciones y las ejecute.

**Comando principal para ejecutar cualquier script:**
```
> Lee y ejecuta las instrucciones del archivo 'nombre_del_script.md'
```

Ahora veamos algunos escenarios útiles.

Crea un directorio `scenarios`.
```bash
/path/to/gemini-cli > mkdir scenarios
```

en él almacenaremos nuestros escenarios.

### Escenario: "Auditoría del repositorio Git"

Esta tarea es familiar para todo desarrollador: antes de comenzar a trabajar, debes verificar el estado actual del proyecto. Creemos un escenario que haga esto por nosotros.

1.  **En el directorio `scenarios`, crea un archivo `git-health-check.md`** con el siguiente contenido:

    ```markdown
    Eres un ingeniero de Git experimentado. Tu tarea es realizar una auditoría completa del repositorio actual.

    Realiza los siguientes pasos estrictamente en orden y espera mi confirmación para cada comando:

    1.  **Comprueba el estado:** Muéstrame el estado actual del repositorio para ver los archivos sin seguimiento o modificados. Sugiere el comando `!git status`.
    2.  **Obtén actualizaciones:** Obtén los últimos cambios del servidor remoto, pero no los apliques. Sugiere el comando `!git fetch origin`.
    3.  **Compara ramas:** Muéstrame la diferencia entre mi rama local `main` y la remota `origin/main`. Sugiere el comando `!git log main..origin/main --oneline`.
    4.  **Encuentra archivos grandes:** Encuentra los 5 archivos más grandes del proyecto que no estén en `.git`. Sugiere el comando `!find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5`.
    5.  **Resume:** Finalmente, describe brevemente el estado del repositorio basándose en los datos obtenidos.
    ```

2.  **Ejecuta el escenario en Gemini CLI:**

    ```
    > Lee y ejecuta el escenario 'git-health-check.md'
    ```

![1](assets/1.png)

En realidad, no hay ningún repositorio en este directorio, Gemini sugerirá crear un nuevo repositorio.
Gemini CLI corregirá automáticamente los errores durante la creación del repositorio, por ejemplo, si olvidaste inicializarlo, te sugerirá hacerlo,
así como los errores actuales durante la ejecución del script.

## Paso 1: Comprobación del estado

![2](assets/2.png)

Respuesta de Gemini:
```text
>✦ Soy un ingeniero de Git experimentado. Iniciando la auditoría de tu repositorio.
> Paso 1: Comprobación del estado
>Para comprobar el estado actual del repositorio y ver los archivos sin seguimiento o modificados, ejecutaré el comando `git status`.
```
Ejecutando el comando `git status`...
![3](assets/3.png)

Respuesta de Gemini:
```text
✦ Error: C:\Users\user\Documents\repos no es un repositorio Git.

  Por favor, especifica en qué subdirectorio debo ejecutar la auditoría. Por ejemplo, public_repositories.
```
Pedimos crear un nuevo repositorio.
![4](assets/4.png)
Respuesta de Gemini:
```text
✦ Excelente, repositorio Git creado. Ahora puedo continuar con la auditoría.


  Ejecutando git status para comprobar si hay archivos sin seguimiento.
```
![5](assets/5.png)

...

![6](assets/6.png)

Respuesta de Gemini:
```text
✦ El repositorio tiene muchos archivos y carpetas sin seguimiento. Para continuar, necesito añadirlos al índice. Añadiré todos los archivos.
```

![7](assets/7.png)
...
![8](assets/8.png)

Se produjo un error durante la ejecución del comando
```text
error: pathspec 'commit" no coincidió con ningún archivo(s) conocido(s) por git
```
Respuesta de Gemini:
```text
✦ Parece que hubo un error con las comillas en el comando. Lo intentaré de nuevo usando comillas simples para el mensaje de confirmación.
```

![9](assets/9.png)
![10](assets/10.png)
¡Esta vez funcionó!

Respuesta de Gemini:
```text
✦ Excelente, la primera confirmación se ha creado con éxito. Ahora eliminaré el archivo temporal con el mensaje de confirmación.
```

Ahora gemini eliminará el archivo temporal con el mensaje de confirmación.

gemini cli aplica el comando relevante ('rm', 'del') a su vez.

![11](assets/11.png)

### Paso 2: Obtención de actualizaciones
Dado que el repositorio remoto no existe, gemini cli obtendrá un error.
Ten en cuenta que espera el error.

![12](assets/12.png)

### Paso 3: Comparación de ramas

También habrá un error aquí, ya que la rama `main` no existe.
![13](assets/13.png)

### Paso 4: Búsqueda de archivos grandes

![14](assets/14.png)
Respuesta de Gemini:
```text
El comando `find` no funcionó porque en Windows necesitas usar `dir`. Gemini corregirá el error por sí mismo y sugerirá el comando correcto.

A continuación, gemini cli discute qué hacer a continuación:
✦ THINK: El usuario quiere que encuentre los 5 archivos más grandes del proyecto.
  El comando anterior find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5 falló porque find, sort y head
  no son comandos nativos de Windows. Necesito usar un equivalente de PowerShell.

   1. Obtener todos los archivos: Get-ChildItem -Recurse -File
   2. Excluir el directorio .git: Where-Object { $_.FullName -notlike "*\.git\*" }
   3. Ordenar por tamaño (descendente): Sort-Object -Property Length -Descending
   4. Seleccionar los 5 primeros: Select-Object -First 5
   5. Formatear la salida: ForEach-Object { "{0} {1}" -f $_.Length, $_.FullName }

  Combinemos esto en un solo comando de PowerShell. Parece que find y head no están disponibles en tu entorno Windows. Usaré PowerShell,
  para realizar la misma tarea.
```
![15](assets/15.png)

Fallo de nuevo

gemini cli continúa razonando sobre qué hacer a continuación:
Respuesta de Gemini:
```text
 ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ THINK: El usuario quiere encontrar los 5 archivos más grandes.
  El comando de PowerShell sigue sin ejecutarse correctamente. Parece que la tubería | y los caracteres especiales están siendo malinterpretados por el
  shell cuando se pasan como una única cadena de comando.

  Intentaré ejecutar el comando guardando primero el script en un archivo y luego ejecutando el archivo con PowerShell.

   1. Crear un archivo de script de PowerShell (find_large_files.ps1).
   2. El contenido del script será: Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notlike "*\.git\*" } | Sort-Object
      -Property Length -Descending | Select-Object -First 5 | Format-Table Length, FullName -AutoSize
   3. Ejecutar el script usando powershell -File find_large_files.ps1.
   4. Eliminar el archivo de script. Parece que pasar comandos complejos a PowerShell directamente causa problemas. Crearé un archivo de script temporal
      PowerShell, lo ejecutaré y luego lo eliminaré.

```
![16](assets/16.png)

¡Esta vez funcionó!

### Paso 5: Resumen
gemini cli resume:
```text
 Estado del repositorio:

   * Repositorio local: Inicializado, y todos los archivos en la carpeta raíz C:\Users\user\Documents\repos se han añadido a la primera confirmación.
   * Repositorio remoto: No configurado. No hay origen remoto, por lo que no es posible obtener actualizaciones o comparar ramas.
   * Archivos grandes: Se encontraron varios archivos muy grandes, principalmente en los subdirectorios venv y public_repositories. Los más grandes son
     bibliotecas .lib y archivos .zip. Se recomienda añadir las rutas que contienen archivos binarios grandes (por ejemplo, venv, *.zip) al archivo .gitignore,
     para evitar que se incluyan en el repositorio.

  Auditoría completada.
```
![17](assets/17.png)

### Escenario: "Limpieza del entorno Docker"

Docker acumula muchas imágenes, contenedores y redes innecesarias con el tiempo. Este escenario ayudará a limpiar todo de forma segura.

1.  **Crea un archivo `docker-cleanup.md`**:

    ```markdown
    Eres un ingeniero de DevOps responsable de la limpieza del sistema. Tu tarea es limpiar de forma segura el entorno Docker.

    Procede paso a paso:

    1.  **Mostrar contenedores en ejecución:** Primero, lista todos los contenedores activos para que pueda asegurarme de no detener nada importante. Sugiere `!docker ps`.
    2.  **Detener todos los contenedores:** Después de mi aprobación, sugiere un comando para detener TODOS los contenedores en ejecución. Comando: `!docker stop $(docker ps -q)`.
    3.  **Limpieza global:** Ahora realiza una limpieza completa del sistema de imágenes "colgantes" (dangling), contenedores detenidos, redes no utilizadas y caché de compilación. Sugiere el comando más seguro y eficiente `!docker system prune -af`.
    4.  **Informe:** Después de la ejecución, informa cuánto espacio se liberó, basándose en la salida del último comando.
    ```

2.  **Ejecuta el escenario de limpieza de Docker en Gemini CLI:**

    ```
    > Lee y ejecuta el escenario de limpieza de Docker del archivo 'docker-cleanup.md'
    ```
**Resultado:** Gemini te guiará a través de un proceso de limpieza seguro, solicitando confirmación en cada paso crítico.

---


### Escenario: "Lanzamiento de aplicaciones del sistema"

Como se muestra en el ejemplo, Gemini maneja el lanzamiento de aplicaciones perfectamente. Formalicemos esto en un escenario simple para Windows.

1.  **Crea un archivo `open-windows-tools.md`**:

    ```markdown
    Eres un administrador de sistemas de Windows. Tu tarea es abrir utilidades del sistema a petición.

    - Si pido "programador de tareas", sugiere ejecutar `!taskschd.msc`.
    - Si pido "editor del registro", advierte sobre el peligro y sugiere ejecutar `!regedit`.
    - Si pido "monitor de recursos", sugiere ejecutar `!resmon`.
    - Si pido "administrador de tareas", sugiere ejecutar `!taskmgr`.
    - Si pido "símbolo del sistema", sugiere ejecutar `!cmd`.
    - Si pido "explorador", sugiere ejecutar `!explorer`.
    De manera similar para otras utilidades.
    ```

2.  **Ejecuta el escenario y da un comando:**

    ```
    > Usa las instrucciones de 'open-windows-tools.md'. Abre el programador de tareas.
    ```
**Resultado:** Gemini comprenderá el contexto del archivo y tu solicitud, luego sugerirá ejecutar el comando necesario.

> **Respuesta de Gemini:**
> ```text
> De acuerdo, abriendo el Programador de tareas.
>
> ¿Ejecutar `!taskschd.msc`? (s/n)
> ```
Después de la confirmación, la utilidad estándar de Windows se abrirá en tu pantalla.
```