## Gemini CLI: Técnicas avanzadas y automatización de escenarios (Parte 2)

En la primera parte, cubrimos los conceptos básicos: instalación, autenticación y ejecución de comandos individuales. Ahora, pasemos al siguiente nivel. En esta parte, le enseñaremos a Gemini CLI a ejecutar escenarios complejos de varios pasos que se pueden guardar, reutilizar y compartir con el equipo. Esto convertirá la herramienta de un simple asistente en un potente motor de automatización.

### Mecanismo de ejecución de escenarios

La idea clave es usar archivos `.md` como "recetas" o "escenarios" para Gemini. Dentro de dicho archivo, describimos en lenguaje natural la secuencia de acciones que la IA debe realizar.

Para ejecutar un escenario, usaremos la herramienta integrada `ReadFile`. Simplemente le pediremos a Gemini que lea el archivo de instrucciones y las ejecute.

**El comando básico para ejecutar cualquier escenario:**
```
> Lee y ejecuta las instrucciones del archivo 'nombre_del_escenario.md'
```

Ahora veamos algunos escenarios útiles.

Crea un directorio de `scenarios`.
```bash
/path/to/gemini-cli > mkdir scenarios
```

en el que almacenaremos nuestros escenarios.


### Escenario: "Auditoría del repositorio de Git"

Esta tarea es familiar para todos los desarrolladores: antes de comenzar a trabajar, debe verificar el estado actual del proyecto. Creemos un escenario que lo haga por nosotros.

1.  **En el directorio `scenarios`, crea un archivo `git-health-check.md`** con el siguiente contenido:

    ```markdown
    Eres un ingeniero de Git experimentado. Tu tarea es realizar una auditoría completa del repositorio actual.
    
    Sigue estos pasos estrictamente en orden y espera mi confirmación para cada comando:
    
    1.  **Comprobar estado:** Muéstrame el estado actual del repositorio para ver los archivos no rastreados o modificados. Sugiere el comando `!git status`.
    2.  **Obtener actualizaciones:** Obtén los últimos cambios del servidor remoto, pero no los apliques. Sugiere el comando `!git fetch origin`.
    3.  **Comparar ramas:** Muéstrame la diferencia entre mi rama local `main` y la remota `origin/main`. Sugiere el comando `!git log main..origin/main --oneline`.
    4.  **Encontrar archivos grandes:** Encuentra los 5 archivos más grandes del proyecto que no estén en `.git`. Sugiere el comando `!find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5`.
    5.  **Resumir:** Al final, describe brevemente el estado del repositorio en función de los datos obtenidos.
    ```

2.  **Ejecuta el escenario en Gemini CLI:**

    ```
    > Lee y ejecuta el script 'git-health-check.md'
    ```

![1](assets/1.png)


De hecho, no hay ningún repositorio en este directorio, Gemini se ofrecerá a crear un nuevo repositorio.
Gemini CLI corregirá de forma independiente los errores durante la creación del repositorio, por ejemplo, si olvidaste inicializarlo, se ofrecerá a hacerlo,
así como los errores actuales durante la ejecución del script

## Paso 1: Comprobación de estado

![2](assets/2.png)

Respuesta de Gemini:
```text
>✦ Soy un ingeniero de Git experimentado. Iniciando la auditoría de tu repositorio.
> Paso 1: Comprobación de estado
>Para comprobar el estado actual del repositorio y ver los archivos no rastreados o modificados, ejecutaré el comando `git status`.
```
Ejecutando el comando `git status`...
![3](assets/3.png)

Respuesta de Gemini:
```text
✦ Error: C:\Users\user\Documents\repos no es un repositorio de Git.

  Por favor, especifica en cuál de los subdirectorios debo ejecutar la auditoría. Por ejemplo, public_repositories.
```
Pedimos crear un nuevo repositorio.
![4](assets/4.png)
Respuesta de Gemini:
```text
✦ Excelente, el repositorio de Git ha sido creado. Ahora puedo continuar con la auditoría.


  Ejecutando git status para comprobar si hay archivos no rastreados.
```
![5](assets/5.png)

...

![6](assets/6.png)

Respuesta de Gemini:
```text
✦ Hay muchos archivos y carpetas sin seguimiento en el repositorio. Para continuar, necesito añadirlos al índice. Añadiré todos los archivos.
```

![7](assets/7.png)
...
![8](assets/8.png)

Se ha producido un error durante la ejecución del comando
```text 
error: pathspec 'commit"' did not match any file(s) known to git
```
Respuesta de Gemini:
```text
✦ Parece que ha habido un error con las comillas en el comando. Lo intentaré de nuevo, usando comillas simples para el mensaje de commit.
```

![9](assets/9.png)
![10](assets/10.png)
¡Esta vez ha funcionado!

Respuesta de Gemini:
```text
✦ Excelente, el primer commit se ha creado correctamente. Ahora eliminaré el archivo temporal con el mensaje de commit.
```
Ahora gemini eliminará el archivo temporal con el mensaje de commit.

gemini cli aplica el comando correspondiente por turno ('rm','del')

![11](assets/11.png)




### Paso 2: Obtener actualizaciones
Como el repositorio remoto no existe, gemini cli obtendrá un error.
Ten en cuenta que él mismo espera un error

![12](assets/12.png)


### Paso 3: Comparar ramas

Aquí también habrá un error, ya que la rama `main` no existe.
![13](assets/13.png)


###   Paso 4: Encontrar archivos grandes

![14](assets/14.png)
Respuesta de Gemini:
```text
El comando `find` no ha funcionado porque en Windows es necesario usar `dir`. Gemini corregirá el error por sí mismo y sugerirá el comando correcto.

A continuación, gemini cli discute los siguientes pasos:
✦ THINK: The user wants me to find the 5 largest files in the project.
  The previous command find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5 failed because find, sort, and head
  are not native Windows commands. I need to use a PowerShell equivalent.

   1. Get all files: Get-ChildItem -Recurse -File
   2. Exclude .git directory: Where-Object { $_.FullName -notlike "*\.git\*" }
   3. Sort by size (descending): Sort-Object -Property Length -Descending
   4. Select the top 5: Select-Object -First 5
   5. Format the output: ForEach-Object { "{0} {1}" -f $_.Length, $_.FullName }

  Let's combine these into a single PowerShell command.Parece que find y head no están disponibles en tu entorno de Windows. Usaré PowerShell,
  para realizar la misma tarea.
```
![15](assets/15.png)

Fallo de nuevo

gemini cli sigue razonando sobre qué hacer a continuación:
Respuesta de Gemini:
```text
 ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ THINK: The user wants to find the 5 largest files.
  The PowerShell command is still not executing correctly. It seems that the pipe | and special characters are being misinterpreted by the
  shell when passed as a single command string.

  I will try to execute the command by first saving the script to a file and then executing the file with PowerShell.

   1. Create a PowerShell script file (find_large_files.ps1).
   2. The content of the script will be: Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notlike "*\.git\*" } | Sort-Object
      -Property Length -Descending | Select-Object -First 5 | Format-Table Length, FullName -AutoSize
   3. Execute the script using powershell -File find_large_files.ps1.
   4. Delete the script file.Parece que pasar comandos complejos a PowerShell directamente causa problemas. Crearé un archivo de script de PowerShell temporal,
      lo ejecutaré y luego lo eliminaré.
```
![16](assets/16.png)

¡Esta vez todo ha funcionado!

### Paso 5: Resumen

gemini cli resume:
```text
 Estado del repositorio:

   * Repositorio local: Inicializado, y todos los archivos de la carpeta raíz C:\Users\user\Documents\repos se han añadido al primer commit.
   * Repositorio remoto: No configurado. No hay un origen remoto, por lo que no es posible obtener actualizaciones ni comparar ramas.
   * Archivos grandes: Se han encontrado varios archivos muy grandes, principalmente en los subdirectorios venv y public_repositories. Los más grandes son
     bibliotecas .lib y archivos .zip. Se recomienda añadir las rutas que contienen archivos binarios grandes (por ejemplo, venv, *.zip) al archivo .gitignore,
     para evitar que entren en el repositorio.

  La auditoría ha finalizado.
```
![17](assets/17.png)


### Escenario: "Limpieza del entorno de Docker"

Con el tiempo, Docker acumula muchas imágenes, contenedores y redes innecesarios. Este escenario te ayudará a limpiarlo todo de forma segura.

1.  **Crea un archivo `docker-cleanup.md`**:

    ```markdown
    Eres un ingeniero de DevOps responsable de la limpieza del sistema. Tu tarea es limpiar de forma segura el entorno de Docker.
    
    Sigue estos pasos:
    
    1.  **Mostrar los contenedores en ejecución:** Primero, enumera todos los contenedores activos para que pueda asegurarme de que no detengo nada importante. Sugiere `!docker ps`.
    2.  **Detener todos los contenedores:** Después de mi aprobación, sugiere un comando para detener TODOS los contenedores en ejecución. El comando es: `!docker stop $(docker ps -q)`.
    3.  **Limpieza global:** Ahora realiza una limpieza completa del sistema de imágenes colgantes (dangling), contenedores detenidos, redes no utilizadas y la caché de compilación. Sugiere el comando más seguro y eficaz `!docker system prune -af`.
    4.  **Informe:** Después de la ejecución, informa de cuánto espacio se ha liberado, basándote en la salida del último comando.
    ```

2.  **Ejecuta el escenario en Gemini CLI:**

    ```
    > Lee y ejecuta el script de limpieza de Docker del archivo 'docker-cleanup.md'
    ```
**Resultado:** Gemini te guiará a través de un proceso de limpieza seguro, pidiendo confirmación en cada paso crítico.

---


### Escenario: "Lanzamiento de aplicaciones del sistema"

Como se muestra en el ejemplo, Gemini es excelente para lanzar aplicaciones. Formalicemos esto como un escenario simple para Windows.

1.  **Crea un archivo `open-windows-tools.md`**:

    ```markdown
    Eres un administrador de sistemas de Windows. Tu tarea es abrir las utilidades del sistema a petición.
    
    - Si pido "programador de tareas", sugiere ejecutar `!taskschd.msc`.
    - Si pido "editor del registro", advierte del peligro y sugiere ejecutar `!regedit`.
    - Si pido "monitor de recursos", sugiere ejecutar `!resmon`.
    - Si pido "administrador de tareas", sugiere ejecutar `!taskmgr`.
    - Si pido "símbolo del sistema", sugiere ejecutar `!cmd`.
    - Si pido "explorador", sugiere ejecutar `!explorer`.
    Del mismo modo para otras utilidades.
    ```

2.  **Ejecuta el escenario y da una orden:**

    ```
    > Usa las instrucciones de 'open-windows-tools.md'. Abre el programador de tareas.
    ```
**Resultado:** Gemini entenderá el contexto del archivo y tu petición, y luego sugerirá ejecutar el comando necesario.

> **Respuesta de Gemini:**
> ```text
> De acuerdo, abriendo el Programador de tareas.
>
> ¿Ejecutar `!taskschd.msc`? (y/n)
> ```
Tras la confirmación, la utilidad estándar de Windows se abrirá en tu pantalla.
```