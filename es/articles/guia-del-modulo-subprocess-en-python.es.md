## Trabajar con la biblioteca `subprocess` en Python


### 1. **¿Qué es `subprocess` y para qué sirve?**

El módulo `subprocess` en Python proporciona una interfaz para crear nuevos procesos,
conectarse a sus flujos de entrada/salida/error y obtener sus códigos de retorno.
Permite que los scripts de Python ejecuten y administren otros programas,
escritos en cualquier lenguaje, ya sean utilidades del sistema, scripts de shell u otros ejecutables.

**Contexto histórico:**

Antes de la llegada de `subprocess`, se usaban funciones del módulo `os`, como `os.system()`, `os.spawn*()`, así como el módulo `commands` (en Python 2) para ejecutar procesos externos. Estos enfoques tenían una serie de desventajas:
*   `os.system()`: Ejecuta un comando a través del shell del sistema, lo que no es seguro cuando se trabaja con entradas de usuario y es menos flexible en la gestión de flujos.
*   `os.spawn*()`: Más flexibles, pero difíciles de usar y dependientes de la plataforma.
*   El módulo `popen2` (y sus variaciones): Proporcionaba acceso a los flujos, pero era complejo y tenía problemas de bloqueo.

El módulo `subprocess` se introdujo en Python 2.4 (PEP 324) como una forma unificada y más segura de interactuar con los procesos secundarios. Encapsula la mejor funcionalidad de los módulos anteriores y proporciona una API más limpia.

**Tareas principales que se resuelven con `subprocess`:**

*   Ejecución de comandos del sistema operativo (por ejemplo, `ls`, `dir`, `ping`).
*   Ejecución de utilidades externas para el procesamiento de datos (por ejemplo, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Integración con sistemas de control de versiones (`git`, `svn`).
*   Ejecución de compiladores o intérpretes de otros lenguajes.
*   Automatización de la administración del sistema.
*   Organización de la interacción entre diferentes programas.

---

### 2. Funciones y clases principales

El módulo `subprocess` ofrece varias formas de ejecutar procesos:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   Esta es la API de alto nivel **recomendada**, que apareció en Python 3.5.
    *   Ejecuta un comando, espera a que se complete y devuelve un objeto `CompletedProcess`.
    *   Adecuado para la mayoría de los casos en los que solo necesita ejecutar un comando y obtener el resultado.

    ```python
    import subprocess

    # Ejecución simple
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Si check=True y el comando devolvió un valor distinto de cero, se lanzará CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Esta es la clase principal para crear y administrar procesos secundarios.
    *   Proporciona la máxima flexibilidad: ejecución no bloqueante, control detallado de los flujos de E/S, la capacidad de enviar señales al proceso.
    *   La función `run()` utiliza `Popen` internamente.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Proceso iniciado con PID: {process.pid}")
    # ... se puede hacer otro trabajo ...
    process.wait() # Esperar a que se complete
    print(f"El proceso finalizó con el código: {process.returncode}")
    ```

*   **Funciones obsoletas, pero que aún se encuentran (eran la API principal antes de Python 3.5):**
    *   `subprocess.call(args, ...)`: Ejecuta un comando y espera a que se complete. Devuelve el código de retorno. Similar a `os.system()`, pero más seguro si `shell=False`.
    *   `subprocess.check_call(args, ...)`: Como `call()`, pero lanza `CalledProcessError` si el código de retorno no es 0.
    *   `subprocess.check_output(args, ...)`: Ejecuta un comando, espera a que se complete y devuelve su salida estándar (stdout) como una cadena de bytes. Lanza `CalledProcessError` si el código de retorno no es 0.

    Aunque estas funciones todavía funcionan, `subprocess.run()` proporciona una interfaz más conveniente y unificada para las mismas tareas.

---

### 3. Argumentos clave de las funciones `run()` y `Popen()`

Estos argumentos le permiten ajustar el inicio y la interacción con el proceso secundario:

*   **`args`**: 
    *   El primer argumento y obligatorio.
    *   Puede ser una lista de cadenas (recomendado) o una sola cadena (si `shell=True`).
    *   El primer elemento de la lista es el nombre del archivo ejecutable, el resto son sus argumentos.
    *   Ejemplo: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**: 
    *   Definen cómo se manejarán la entrada estándar, la salida y el flujo de errores del proceso secundario.
    *   Valores posibles:
        *   `None` (predeterminado): Se heredan del proceso principal.
        *   `subprocess.PIPE`: Se crea una tubería (pipe) a través de la cual se pueden intercambiar datos. `process.stdin`, `process.stdout`, `process.stderr` se convierten en objetos similares a archivos.
        *   `subprocess.DEVNULL`: Redirige el flujo a "ninguna parte" (análogo a `/dev/null`).
        *   Un descriptor de archivo abierto (un número entero).
        *   Un objeto de archivo existente (por ejemplo, un archivo abierto `open('output.txt', 'w')`).

*   **`capture_output=True` (para `run()`):**
    *   Una opción conveniente, equivalente a establecer `stdout=subprocess.PIPE` y `stderr=subprocess.PIPE`.
    *   El resultado estará disponible en `result.stdout` y `result.stderr`.

*   **`text=True` (o `universal_newlines=True` para compatibilidad):**
    *   Si es `True`, los flujos `stdout` y `stderr` (así como `stdin`, si se pasa una cadena) se abrirán en modo de texto utilizando la codificación predeterminada (generalmente UTF-8). La decodificación/codificación se produce automáticamente.
    *   Si es `False` (predeterminado), los flujos se tratan como bytes.
    *   Desde Python 3.7, `text` es el alias preferido para `universal_newlines`. También puede especificar una codificación específica a través de `encoding` y un controlador de errores a través de `errors`.

*   **`shell=False` (predeterminado):**
    *   Si es `False` (recomendado por razones de seguridad y previsibilidad), `args` debe ser una lista. El comando se ejecuta directamente.
    *   Si es `True`, `args` se pasa como una cadena al shell del sistema (por ejemplo, `/bin/sh` en Unix, `cmd.exe` en Windows) para su interpretación. Esto le permite usar las funciones del shell (variables, sustituciones, tuberías), pero es **PELIGROSO** si `args` contiene una entrada de usuario no verificada (riesgo de inyección de comandos).

*   **`cwd=None`:**
    *   Establece el directorio de trabajo actual para el proceso secundario. Por defecto, se hereda del principal.

*   **`env=None`:**
    *   Un diccionario que define las variables de entorno para el nuevo proceso. Por defecto, se hereda el entorno del proceso principal. Si se especifica, reemplaza por completo el entorno heredado. Para agregar/cambiar variables mientras se conserva el resto, primero debe copiar `os.environ` y luego modificarlo.

*   **`timeout=None`:**
    *   El tiempo máximo en segundos asignado para la ejecución del comando. Si el proceso no se completa en este tiempo, se lanzará una excepción `subprocess.TimeoutExpired`. `Popen.communicate()` también acepta un `timeout`.

*   **`check=False` (para `run()`):**
    *   Si es `True` y el proceso finaliza con un código de retorno distinto de cero, se lanzará una excepción `subprocess.CalledProcessError`.

---

### 4. Trabajar con resultados y errores

**El objeto `CompletedProcess` (el resultado de `run()`):**

```python
import subprocess

try:
    # Intentando ejecutar un comando que puede fallar
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - un error tipográfico para demostrar un error
        capture_output=True,
        text=True,
        check=True, # Lanzará una excepción si returncode != 0
        timeout=10
    )
    print("Comando ejecutado con éxito.")
    print("Código de retorno:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Generalmente vacío en caso de éxito

except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando (CalledProcessError):")
    print(f"  Comando: {e.cmd}")
    print(f"  Código de retorno: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # Puede contener salida antes del error
    print(f"  Stderr: {e.stderr}") # Generalmente contiene información de error
except subprocess.TimeoutExpired as e:
    print(f"El comando no se completó en {e.timeout} segundos.")
    print(f"  Comando: {e.cmd}")
    if e.stdout: print(f"  Stdout (parcial): {e.stdout.decode(errors='ignore')}") # stdout es bytes
    if e.stderr: print(f"  Stderr (parcial): {e.stderr.decode(errors='ignore')}") # stderr es bytes
except FileNotFoundError:
    print("Error: comando o programa no encontrado.")
except Exception as e:
    print(f"Se ha producido otro error: {e}")
```

**Atributos de `CompletedProcess`:**
*   `args`: Los argumentos utilizados para iniciar el proceso.
*   `returncode`: El código de retorno del proceso. 0 suele significar éxito.
*   `stdout`: La salida estándar del proceso (bytes o una cadena si `text=True` y `capture_output=True`).
*   `stderr`: El flujo de error estándar del proceso (bytes o una cadena si `text=True` y `capture_output=True`).

**Excepciones:**
*   `subprocess.CalledProcessError`: Se lanza si `check=True` (para `run()`) o se usan `check_call()`, `check_output()` y el comando finaliza con un código distinto de cero. Contiene `returncode`, `cmd`, `output` (o `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: Si el tiempo de espera ha expirado. Contiene `cmd`, `timeout`, `stdout`, `stderr` (salida parcial, si la hay).
*   `FileNotFoundError`: Si no se encuentra el archivo ejecutable.

**Interacción con un objeto `Popen`:**

La clase `Popen` da más control:

```python
import subprocess
import time

# Ejecutar un proceso en segundo plano
process = subprocess.Popen(["sleep", "5"])
print(f"Proceso PID: {process.pid} iniciado.")

# Comprobación de estado no bloqueante
while process.poll() is None: # poll() devuelve None si el proceso todavía se está ejecutando
    print("El proceso todavía se está ejecutando...")
    # Puede leer la salida a medida que llega (¡cuidado, puede bloquear!)
    # line = process.stdout.readline()
    # if line: print(f"Salida: {line.strip()}")
    time.sleep(1)

# Esperar a que se complete y obtener toda la salida/errores
# stdout_data, stderr_data = process.communicate(timeout=10) # Forma segura

# Si no se usó communicate(), después de poll() != None puede leer el resto
if process.stdout:
    for line in process.stdout:
        print(f"Salida final: {line.strip()}")

print(f"El proceso finalizó con el código: {process.returncode}")

# Si necesita forzar la terminación
# process.terminate() # Envía SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Si no ha terminado
#     process.kill()      # Envía SIGKILL
```

*   `process.poll()`: Comprueba si el proceso secundario ha finalizado. Devuelve el código de retorno o `None`. No bloqueante.
*   `process.wait(timeout=None)`: Espera a que el proceso secundario finalice. Devuelve el código de retorno. Bloqueante.
*   `process.communicate(input=None, timeout=None)`:
    *   La forma más segura de interactuar con un proceso cuando se usa `PIPE`.
    *   Envía datos a `stdin` (si se especifica `input`), lee todos los datos de `stdout` y `stderr` hasta el final y espera a que el proceso finalice.
    *   Devuelve una tupla `(stdout_data, stderr_data)`.
    *   Ayuda a evitar interbloqueos que pueden ocurrir con la lectura/escritura directa en `process.stdout`/`process.stdin` si los búferes se desbordan.
*   `process.terminate()`: Envía la señal `SIGTERM` al proceso (terminación suave).
*   `process.kill()`: Envía la señal `SIGKILL` al proceso (terminación forzada).
*   `process.send_signal(signal)`: Envía la señal especificada al proceso.
*   `process.stdin`, `process.stdout`, `process.stderr`: Objetos similares a archivos para las tuberías, si se crearon con `PIPE`.

---

### 5. Escenarios de uso avanzados

**Redirección de la salida de un comando a la entrada de otro (tuberías):**

Emulando `ps aux | grep python`:

```python
import subprocess

# Ejecutar el primer comando, su stdout será una tubería
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Ejecutar el segundo comando, su stdin será el stdout del primer comando
# El stdout del segundo comando también es una tubería para leer el resultado
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Vincular stdout de ps a stdin para grep
    stdout=subprocess.PIPE,
    text=True
)

# ¡Importante! Cierre el stdout del primer comando en el proceso principal,
# para que grep reciba EOF cuando ps termine.
if ps_process.stdout:
    ps_process.stdout.close()

# Obtener la salida de grep
stdout_data, stderr_data = grep_process.communicate()

print("Resultado de la tubería:")
print(stdout_data)

if stderr_data:
    print("Errores de grep:", stderr_data)

# Asegurarse de que ambos procesos hayan finalizado
ps_process.wait() # communicate() ya ha esperado
# grep_process.wait() # communicate() ya ha esperado
print(f"código de retorno de ps: {ps_process.returncode}")
print(f"código de retorno de grep: {grep_process.returncode}")
```
*Nota:* Para tuberías simples, `subprocess.run("ps aux | grep python", shell=True, ...)` puede ser más simple, pero menos seguro y flexible.

**Ejecución asíncrona de procesos:**

`Popen` no es bloqueante por naturaleza. Puede ejecutar varios procesos y administrarlos en paralelo.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Comando con un error
]

processes = []
for cmd_args in commands:
    print(f"Ejecutando: {' '.join(cmd_args)}")
    # Para la asincronicidad, es mejor redirigir stdout/stderr,
    # para no interferir entre sí o con la consola del padre.
    # DEVNULL si no se necesita la salida, PIPE si se necesita más tarde.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Hacer otro trabajo o esperar a que se complete
while any(p.poll() is None for p in processes):
    print("Esperando a que se completen todos los procesos...")
    time.sleep(0.5)

print("\nResultados:")
for i, p in enumerate(processes):
    print(f"El comando '{' '.join(commands[i])}' finalizó con el código: {p.returncode}")
```

**Interacción interactiva con un proceso:**

Esta es una tarea compleja que requiere una gestión cuidadosa de los flujos para evitar interbloqueos. `communicate()` es bueno para un intercambio único. Para una sesión interactiva larga, es posible que necesite leer/escribir directamente en `p.stdin`, `p.stdout`, `p.stderr` usando E/S no bloqueante o hilos separados.

```python
import subprocess

# Ejemplo: iniciar una sesión interactiva de python
process = subprocess.Popen(
    ['python', '-i'], # -i para modo interactivo
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Búfer de línea para stdout/stderr (para interactividad)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # ¡Importante!

def read_output():
    # Leer la salida puede ser complicado, ya que necesita saber cuándo detenerse.
    # Este es un ejemplo muy simplificado. Para tareas reales, se necesitan soluciones más robustas.
    # Por ejemplo, leer hasta un cierto patrón (el indicador de la línea de comandos).
    output = ""
    # Leer stdout. En una aplicación real, esto debe hacerse de forma no bloqueante o en un hilo separado.
    # Aquí asumimos que después del comando habrá alguna salida inmediatamente.
    # ¡Esta es una suposición muy frágil para el caso general!
    try:
        # Popen no tiene un readline con un tiempo de espera, esta es una de las dificultades
        # Puede usar select en process.stdout.fileno()
        # o leer carácter por carácter/línea por línea en un hilo separado
        # Por simplicidad, esto no está aquí
        while True: # ¡Cuidado, puede bloquearse!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Detector de indicador primitivo
                output += line
                break
            output += line
    except Exception as e:
        print(f"Error de lectura: {e}")
    return output.strip()

# Inicialización: leer el indicador inicial
initial_output = ""
# Leyendo el mensaje de bienvenida de Python
# Esto es muy simplificado, ya que no sabemos exactamente cuántas líneas leer
for _ in range(5): # Intentemos leer algunas líneas
    try:
        # Popen stdout no tiene tiempo de espera, debe leer con cuidado
        # stdout.readline() puede bloquearse.
        # En aplicaciones reales, aquí se necesitan select o hilos.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Se encontró el indicador
    except BlockingIOError:
        break # Si hubiera lectura no bloqueante
print(f"Salida inicial:\n{initial_output.strip()}")


send_command("a = 10")
# Para la interacción interactiva, leer la salida es la parte más difícil.
# communicate() no es adecuado, ya que cierra los flujos.
# Debe leer con cuidado desde process.stdout y process.stderr,
# posiblemente en hilos separados, para no bloquear el principal.
# Este ejemplo NO está listo para producción para interactividad compleja.
# print(read_output()) # Este read_output es muy primitivo

send_command("print(a * 2)")
# print(read_output())

# Terminar el proceso
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Esperar a que se complete y recopilar el resto

print("\nSalida estándar final:")
print(stdout_data)
if stderr_data:
    print("\nError estándar final:")
    print(stderr_data)

print(f"El proceso de Python finalizó con el código: {process.returncode}")

# Para una interacción interactiva real, a menudo se usan pty (pseudo-terminales)
# a través del módulo `pty` en sistemas similares a Unix, o bibliotecas como `pexpect`.
```
*Advertencia*: La interacción interactiva directa con `Popen` a través de `stdin`/`stdout`/`stderr` es difícil debido a los interbloqueos y el almacenamiento en búfer. Para una interactividad fiable, a menudo se utilizan bibliotecas como `pexpect` (para Unix) o análogas, que funcionan con pseudo-terminales (pty).

**Trabajar con codificaciones:**
*   Use `text=True` (o `universal_newlines=True`) para la decodificación/codificación automática.
*   Si es necesario, puede especificar `encoding="su-codificación"` y `errors="manejador-de-errores"` (por ejemplo, `replace`, `ignore`).
*   Si `text=False` (predeterminado), `stdout` y `stderr` serán cadenas de bytes. Deberá decodificarlos manualmente: `result.stdout.decode('utf-8', errors='replace')`.

---

### 6. Seguridad y mejores prácticas

*   **Riesgos de `shell=True` e inyección de comandos:**
    *   **Nunca** use `shell=True` con comandos construidos a partir de una entrada de usuario no fiable. Esto abre la puerta a la inyección de comandos.
    *   Ejemplo de una vulnerabilidad:
        ```python
        # ¡PELIGROSO!
        filename = input("Introduzca un nombre de archivo para eliminar: ") # El usuario introduce "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Si `shell=True` es absolutamente necesario (por ejemplo, para usar tuberías `|` o comodines `*` directamente en la línea de comandos), escape cuidadosamente todas las partes del comando formadas desde el exterior usando `shlex.quote()` (desde Python 3.3).

*   **Validación y escape de la entrada del usuario:**
    *   Incluso si `shell=False`, si los argumentos del comando se forman a partir de la entrada del usuario, deben validarse. Por ejemplo, si se espera un nombre de archivo, asegúrese de que sea un nombre de archivo válido y no algo como `../../../etc/passwd`.

*   **Pasar argumentos como una lista (cuando `shell=False`):**
    *   Esta es la forma más segura. Cada argumento se pasa como un elemento separado de la lista, y el sistema operativo los maneja correctamente, sin intentar interpretarlos como parte de un comando de shell.
    *   Ejemplo: `subprocess.run(["rm", filename_from_user])` — aquí `filename_from_user` siempre se tratará como un solo argumento (nombre de archivo), incluso si contiene espacios o caracteres especiales.

*   **Manejo de errores y códigos de retorno:**
    *   Compruebe siempre el `returncode` o use `check=True` (para `run()`) / `check_call()` / `check_output()` para asegurarse de que el comando se ejecutó correctamente.
    *   Maneje las posibles excepciones (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Gestión de recursos:**
    *   Si abre tuberías (`PIPE`), asegúrese de que finalmente se cierren. `Popen.communicate()` lo hace automáticamente. Si está trabajando directamente con `p.stdin`, `p.stdout`, `p.stderr`, es posible que deba cerrarlos explícitamente.
    *   En aplicaciones de larga duración, asegúrese de que los procesos secundarios finalicen correctamente y no se conviertan en "zombis". Use `p.wait()` o `p.communicate()`. Si es necesario, use `p.terminate()` o `p.kill()`.

*   **Codificaciones:** Tenga cuidado con las codificaciones cuando use `text=True` o cuando decodifique manualmente cadenas de bytes. Los problemas de codificación son una fuente común de errores.

---

### 7. Ejemplos prácticos

**1. Ejecutar un comando simple y comprobar el código de retorno:**
```python
import subprocess

try:
    # Ejecutar 'ls' para un directorio existente
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Comando 'ls /tmp' ejecutado, código de retorno: {result.returncode}")

    # Ejecutar 'ls' para un directorio inexistente
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Esta línea no se ejecutará si check=True, ya que se lanzará una excepción
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando: {e.cmd}")
    print(f"Código de retorno: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. Capturar la salida de un comando:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Especificar el directorio actual como directorio de trabajo para git
    )
    print("Estado de Git:")
    print(result.stdout)
except FileNotFoundError:
    print("Error: comando 'git' no encontrado. ¿Está Git instalado y en el PATH?")
except subprocess.CalledProcessError as e:
    print(f"Error de git: {e.stderr}")
```

**3. Enviar datos a la entrada de un proceso (usando `communicate`):**
```python
import subprocess

# Enviar texto a 'grep' para buscar
input_text = "hello world\npython is fun\nhello python"
try:
    process = subprocess.Popen(
        ["grep", "python"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout_data, stderr_data = process.communicate(input=input_text, timeout=5)

    if process.returncode == 0: # grep encontró coincidencias
        print("Líneas encontradas:")
        print(stdout_data)
    elif process.returncode == 1: # grep no encontró coincidencias
        print("No se encontraron coincidencias para 'python'.")
    else: # otro error de grep
        print(f"Error de grep (código {process.returncode}):")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep no respondió a tiempo.")
    process.kill() # matar el proceso si se cuelga
    process.communicate() # recopilar la salida/errores restantes
```

**4. Crear una tubería (`ls -l | wc -l`) sin `shell=True`:**
(Un ejemplo más detallado estaba en la sección 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Asegurarse de que stdout existe
    ls_proc.stdout.close()  # Permite que wc_proc reciba EOF cuando ls_proc termine

output, _ = wc_proc.communicate()
print(f"Número de archivos/directorios: {output.strip()}")
```

**5. Usar `timeout`:**
```python
import subprocess

try:
    # Un comando que se ejecutará durante 5 segundos
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("El comando 'sleep 5' se completó (no debería haberlo hecho con timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"El comando '{e.cmd}' no se completó en {e.timeout} segundos.")
```

---

### 8. Conclusión y recursos útiles

El módulo `subprocess` es una herramienta indispensable para cualquier desarrollador de Python que necesite interactuar con programas externos o con el entorno del sistema. Ofrece un equilibrio entre la facilidad de uso (a través de `subprocess.run()`) y una potente flexibilidad (a través de `subprocess.Popen()`).

**Puntos clave:**
*   Prefiera `subprocess.run()` para la mayoría de las tareas.
*   Use `subprocess.Popen()` para la ejecución asíncrona o la gestión compleja de flujos.
*   **Evite `shell=True`**, especialmente con la entrada del usuario, debido a los riesgos de seguridad. Pase los comandos como una lista de argumentos.
*   Maneje siempre los códigos de retorno y las posibles excepciones.
*   Tenga cuidado con las codificaciones cuando trabaje con salida de texto (`text=True` o decodificación manual).
*   `communicate()` es su amigo para un intercambio de datos seguro a través de `PIPE`.

**Recursos útiles:**
*   Documentación oficial de Python para el módulo `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - A New Process Module: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)
