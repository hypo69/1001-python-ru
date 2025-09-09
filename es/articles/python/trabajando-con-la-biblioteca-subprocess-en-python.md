## Trabajando con la biblioteca `subprocess` en Python


### 1. **¿Qué es `subprocess` y para qué sirve?**

El módulo `subprocess` en Python proporciona una interfaz para crear nuevos procesos,
conectarse a sus flujos de entrada/salida/errores y obtener sus códigos de retorno.
Permite que los scripts de Python inicien y administren otros programas,
escritos en cualquier lenguaje, ya sean utilidades del sistema, scripts de shell u otros ejecutables.

**Contexto histórico:**

Antes de `subprocess`, para ejecutar procesos externos se utilizaban funciones del módulo `os`, como `os.system()`, `os.spawn*()`, así como el módulo `commands` (en Python 2). Estos enfoques tenían una serie de desventajas:
*   `os.system()`: Ejecuta un comando a través del shell del sistema, lo que es inseguro al trabajar con entrada de usuario y menos flexible en la gestión de flujos.
*   `os.spawn*()`: Más flexibles, pero complejos de usar y dependientes de la plataforma.
*   El módulo `popen2` (y sus variaciones): Proporcionaba acceso a los flujos, pero era complejo y tenía problemas de bloqueo.

El módulo `subprocess` se introdujo en Python 2.4 (PEP 324) como una forma unificada y más segura de interactuar con procesos secundarios. Encapsula la mejor funcionalidad de los módulos anteriores y proporciona una API más limpia.

**Tareas principales resueltas con `subprocess`:**

*   Ejecución de comandos del sistema operativo (por ejemplo, `ls`, `dir`, `ping`).
*   Inicio de utilidades externas para el procesamiento de datos (por ejemplo, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Integración con sistemas de control de versiones (`git`, `svn`).
*   Inicio de compiladores o intérpretes de otros lenguajes.
*   Automatización de la administración del sistema.
*   Organización de la interacción entre diferentes programas.

--- 

### 2. Funciones y clases principales

El módulo `subprocess` ofrece varias formas de iniciar procesos:

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   Esta es la API de alto nivel **recomendada**, introducida en Python 3.5.
    *   Ejecuta un comando, espera su finalización y devuelve un objeto `CompletedProcess`.
    *   Adecuado para la mayoría de los casos en los que solo se necesita ejecutar un comando y obtener un resultado.

    ```python
    import subprocess

    # Ejecución simple
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Si check=True y el comando devuelve un valor distinto de 0, se lanzará CalledProcessError
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Esta es la clase principal para crear y administrar procesos secundarios.
    *   Proporciona la máxima flexibilidad: inicio no bloqueante, control detallado de los flujos de E/S, capacidad de enviar señales al proceso.
    *   La función `run()` utiliza `Popen` internamente.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Proceso iniciado con PID: {process.pid}")
    # ... se puede hacer otro trabajo ...
    process.wait() # Esperar la finalización
    print(f"Proceso finalizado con código: {process.returncode}")
    ```

*   **Funciones obsoletas, pero aún presentes (antes de Python 3.5 eran la API principal):**
    *   `subprocess.call(args, ...)`: Ejecuta un comando y espera su finalización. Devuelve el código de retorno. Similar a `os.system()`, pero más seguro si `shell=False`.
    *   `subprocess.check_call(args, ...)`: Como `call()`, pero lanza `CalledProcessError` si el código de retorno no es 0.
    *   `subprocess.check_output(args, ...)`: Ejecuta un comando, espera su finalización y devuelve su salida estándar (stdout) como una cadena de bytes. Lanza `CalledProcessError` si el código de retorno no es 0.

    Aunque estas funciones todavía funcionan, `subprocess.run()` proporciona una interfaz más conveniente y unificada para las mismas tareas.

--- 

### 3. Argumentos clave de las funciones `run()` y `Popen()`

Estos argumentos permiten configurar con precisión el inicio y la interacción con el proceso secundario:

*   **`args`**:
    *   Primer argumento y obligatorio.
    *   Puede ser una lista de cadenas (recomendado) o una sola cadena (si `shell=True`).
    *   El primer elemento de la lista es el nombre del ejecutable, los demás son sus argumentos.
    *   Ejemplo: `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`**:
    *   Determinan cómo se manejarán la entrada estándar, la salida y el flujo de errores del proceso secundario.
    *   Valores posibles:
        *   `None` (predeterminado): Se heredan del proceso padre.
        *   `subprocess.PIPE`: Se crea una tubería (pipe), a través de la cual se pueden intercambiar datos. `process.stdin`, `process.stdout`, `process.stderr` se convierten en objetos tipo archivo.
        *   `subprocess.DEVNULL`: Redirige el flujo a "ningún lugar" (análogo a `/dev/null`).
        *   Un descriptor de archivo abierto (un número entero).
        *   Un objeto de archivo existente (por ejemplo, un archivo abierto `open('output.txt', 'w')`).

*   **`capture_output=True` (para `run()`):**
    *   Una opción conveniente, equivalente a establecer `stdout=subprocess.PIPE` y `stderr=subprocess.PIPE`.
    *   El resultado estará disponible en `result.stdout` y `result.stderr`.

*   **`text=True` (o `universal_newlines=True` para compatibilidad):**
    *   Si es `True`, los flujos `stdout` y `stderr` (así como `stdin`, si se pasa una cadena) se abrirán en modo texto utilizando la codificación predeterminada (normalmente UTF-8). La decodificación/codificación se realiza automáticamente.
    *   Si es `False` (predeterminado), los flujos se tratan como bytes.
    *   A partir de Python 3.7, `text` es el alias preferido para `universal_newlines`. También se puede especificar una codificación específica a través de `encoding` y un manejador de errores a través de `errors`.

*   **`shell=False` (predeterminado):**
    *   Si es `False` (recomendado por razones de seguridad y previsibilidad), `args` debe ser una lista. El comando se inicia directamente.
    *   Si es `True`, `args` se pasa como una cadena al shell del sistema (por ejemplo, `/bin/sh` en Unix, `cmd.exe` en Windows) para su interpretación. Esto permite usar las características del shell (variables, sustituciones, tuberías), pero es **PELIGROSO** si `args` contiene entrada de usuario no confiable (riesgo de inyección de comandos).

*   **`cwd=None`:**
    *   Establece el directorio de trabajo actual para el proceso secundario. Por defecto, se hereda del proceso padre.

*   **`env=None`:**
    *   Un diccionario que define las variables de entorno para el nuevo proceso. Por defecto, se hereda el entorno del proceso padre. Si se especifica, reemplaza completamente el entorno heredado. Para añadir/cambiar variables, manteniendo el resto, primero hay que copiar `os.environ` y luego modificarlo.

*   **`timeout=None`:**
    *   Tiempo máximo en segundos permitido para la ejecución del comando. Si el proceso no finaliza en este tiempo, se lanzará una excepción `subprocess.TimeoutExpired`.

*   **`check=False` (para `run()`):**
    *   Si es `True` y el proceso finaliza con un código de retorno distinto de cero, se lanzará una excepción `subprocess.CalledProcessError`.

--- 

### 4. Trabajar con resultados y errores

**Objeto `CompletedProcess` (resultado de `run()`):**

```python
import subprocess

try:
    # Intentamos ejecutar un comando que puede fallar
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - error tipográfico para demostración
        capture_output=True,
        text=True,
        check=True, # Lanzará una excepción si returncode != 0
        timeout=10
    )
    print("Comando ejecutado con éxito.")
    print("Código de retorno:", result.returncode)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr) # Normalmente vacío si tiene éxito

except subprocess.CalledProcessError as e:
    print(f"Error de ejecución de comando (CalledProcessError):")
    print(f"  Comando: {e.cmd}")
    print(f"  Código de retorno: {e.returncode}")
    print(f"  Stdout: {e.stdout}") # Puede contener salida antes del error
    print(f"  Stderr: {e.stderr}") # Normalmente aquí está la información del error
except subprocess.TimeoutExpired as e:
    print(f"El comando no finalizó en {e.timeout} segundos.")
    print(f"  Comando: {e.cmd}")
    if e.stdout: print(f"  Stdout (parcial): {e.stdout.decode(errors='ignore')}") # stdout es bytes
    if e.stderr: print(f"  Stderr (parcial): {e.stderr.decode(errors='ignore')}") # stderr es bytes
except FileNotFoundError:
    print("Error: comando o programa no encontrado.")
except Exception as e:
    print(f"Ocurrió otro error: {e}")
```

**Atributos de `CompletedProcess`:**
*   `args`: Argumentos utilizados para iniciar el proceso.
*   `returncode`: Código de retorno del proceso. 0 normally significa éxito.
*   `stdout`: Salida estándar del proceso (bytes o cadena, si `text=True` y `capture_output=True`).
*   `stderr`: Flujo de error estándar del proceso (bytes o cadena, si `text=True` y `capture_output=True`).

**Excepciones:**
*   `subprocess.CalledProcessError`: Se lanza si `check=True` (para `run()`) o se usan `check_call()`, `check_output()` y el comando finalizó con un código distinto de cero. Contiene `returncode`, `cmd`, `output` (o `stdout`), `stderr`.
*   `subprocess.TimeoutExpired`: Si se agotó el tiempo de espera. Contiene `cmd`, `timeout`, `stdout`, `stderr` (salida parcial, si la hubo).
*   `FileNotFoundError`: Si no se encuentra el ejecutable.

**Interacción con el objeto `Popen`:**

La clase `Popen` ofrece más control:

```python
import subprocess
import time

# Iniciar proceso en segundo plano
process = subprocess.Popen(["ping", "-c", "5", "google.com"], stdout=subprocess.PIPE, text=True)

print(f"Proceso PID: {process.pid} iniciado.")

# Comprobación de estado no bloqueante
while process.poll() is None: # poll() devuelve None si el proceso aún se está ejecutando
    print("El proceso aún se está ejecutando...")
    # Se puede leer la salida a medida que llega (¡cuidado, puede bloquear!)
    # line = process.stdout.readline()
    # if line: print(f"Salida: {line.strip()}")
    time.sleep(1)

# Esperar la finalización y obtener toda la salida/errores
# stdout_data, stderr_data = process.communicate(timeout=10) # Forma segura

# Si communicate() no se usó, después de poll() != None se pueden leer los restantes
if process.stdout:
    for line in process.stdout:
        print(f"Salida final: {line.strip()}")

print(f"Proceso finalizado con código: {process.returncode}")

# Si es necesario terminar forzosamente
# process.terminate() # Envía SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Si no finalizó
#     process.kill()      # Envía SIGKILL
```

*   `process.poll()`: Comprueba si el proceso secundario ha terminado. Devuelve el código de retorno o `None`. No bloqueante.
*   `process.wait(timeout=None)`: Espera a que el proceso secundario termine. Devuelve el código de retorno. Bloqueante.
*   `process.communicate(input=None, timeout=None)`:
    *   La forma más segura de interactuar con un proceso cuando se usan `PIPE`.
    *   Envía datos a `stdin` (si se especifica `input`), lee todos los datos de `stdout` y `stderr` hasta el final y espera a que el proceso termine.
    *   Devuelve una tupla `(stdout_data, stderr_data)`.
    *   Ayuda a evitar interbloqueos que pueden ocurrir con la lectura/escritura directa en `process.stdout`/`process.stdin` si los búferes se desbordan.
*   `process.terminate()`: Envía una señal `SIGTERM` al proceso (terminación suave).
*   `process.kill()`: Envía una señal `SIGKILL` al proceso (terminación forzada).
*   `process.send_signal(signal)`: Envía la señal especificada al proceso.
*   `process.stdin`, `process.stdout`, `process.stderr`: Objetos tipo archivo para tuberías, si se crearon con `PIPE`.

--- 

### 5. Escenarios de uso avanzados

**Redireccionar la salida de un comando a la entrada de otro (tuberías/pipelines):**

Emulamos `ps aux | grep python`:

```python
import subprocess

# Iniciar el primer comando, su stdout será PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Iniciar el segundo comando, su stdin será stdout del primer comando
# stdout del segundo comando también PIPE, para leer el resultado
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Enlazar stdout de ps con stdin para grep
    stdout=subprocess.PIPE,
    text=True
)

# ¡Importante! Cerrar stdout del primer comando en el proceso padre, 
# para que grep reciba EOF cuando ps termine.
if ps_process.stdout:
    ps_process.stdout.close()

# Obtener la salida de grep
stdout_data, stderr_data = grep_process.communicate()

print("Resultado de la tubería:")
print(stdout_data)

if stderr_data:
    print("Errores de grep:", stderr_data)

# Asegurarse de que ambos procesos hayan terminado
ps_process.wait() 
# grep_process.wait() # communicate() ya esperó
print(f"Código de retorno de ps: {ps_process.returncode}")
print(f"Código de retorno de grep: {grep_process.returncode}")
```
*Nota:* Para tuberías simples, `subprocess.run("ps aux | grep python", shell=True, ...)` puede ser más simple, pero menos seguro y flexible.

**Inicio asíncrono de procesos:**

`Popen` es inherentemente no bloqueante. Puedes iniciar varios procesos y gestionarlos en paralelo.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Comando con error
]

processes = []
for cmd_args in commands:
    print(f"Iniciando: {' '.join(cmd_args)}")
    # Para la asincronía, stdout/stderr es mejor redirigirlos, 
    # para no interferir entre sí o con la consola del padre.
    # DEVNULL si la salida no es necesaria, PIPE si es necesaria más tarde.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Hacer otro trabajo o esperar la finalización
while any(p.poll() is None for p in processes):
    print("Esperando la finalización de todos los procesos...")
    time.sleep(0.5)

print("\nResultados:")
for i, p in enumerate(processes):
    print(f"Comando '{' '.join(commands[i])}' finalizado con código: {p.returncode}")
```

**Interacción interactiva con el proceso:**

Esta es una tarea compleja, que requiere una gestión cuidadosa de los flujos para evitar interbloqueos. `communicate()` es bueno para un intercambio único. Para una sesión interactiva prolongada, puede ser necesaria la lectura/escritura directa en `p.stdin`, `p.stdout`, `p.stderr` utilizando E/S no bloqueante o hilos separados.

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
    # Leer la salida puede ser complejo, ya que necesitas saber cuándo detenerte.
    # Este es un ejemplo muy simplificado. Para tareas reales se necesitan soluciones más robustas.
    # Por ejemplo, leer hasta un patrón determinado (prompt de línea de comandos).
    output = ""
    # Leemos stdout. En una aplicación real, esto debe hacerse de forma no bloqueante o en un hilo separado.
    # Aquí asumimos que después de un comando, habrá alguna salida inmediatamente.
    # ¡Esta es una suposición muy frágil para el caso general!
    try:
        # Popen no tiene readline con timeout, esta es una de las dificultades
        # Se puede usar select en process.stdout.fileno()
        # o leer carácter por carácter/línea por línea en un hilo separado
        # Por simplicidad, esto no está incluido aquí
        while True: # ¡Cuidado, puede bloquearse!
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Detector de prompt primitivo
                output += line
                break
            output += line
    except Exception as e:
        print(f"Error de lectura: {e}")
    return output.strip()

# Inicialización: leer el prompt inicial
initial_output = ""
# Leer el saludo de Python
# Esto es muy simplificado, ya que no sabemos exactamente cuántas líneas leer
for _ in range(5): # Intentar leer algunas líneas
    try:
        # Popen stdout no tiene timeout, hay que leer con cuidado
        # stdout.readline() puede bloquearse.
        # En aplicaciones reales, aquí se necesita select o hilos.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Encontrado el prompt
    except BlockingIOError:
        break # Si se usara lectura no bloqueante
print(f"Salida inicial:\n{initial_output.strip()}")


send_command("a = 10")
# Para la interacción interactiva, leer la salida es la parte más compleja.
# communicate() no es adecuado, ya que cierra los flujos.
# Es necesario leer cuidadosamente de process.stdout y process.stderr, 
# posiblemente en hilos separados, para evitar bloquear el principal.
# Este ejemplo NO está listo para producción para interactividad compleja.
# print(read_output()) # Este read_output es muy primitivo

send_command("print(a * 2)")
# print(read_output())

# Terminar proceso
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Esperar la finalización y recopilar lo restante

print("\nSalida estándar final:")
print(stdout_data)
if stderr_data:
    print("\nError estándar final:")
    print(stderr_data)

print(f"Proceso Python finalizado con código: {process.returncode}")

# Para una verdadera interacción interactiva, a menudo se utilizan pty (pseudo-terminales) 
# a través del módulo `pty` en sistemas tipo Unix, o bibliotecas como `pexpect`.
```
*Advertencia*: La interacción interactiva directa con `Popen` a través de `stdin`/`stdout`/`stderr` es compleja debido a los bloqueos y la búferización. Para una interactividad fiable, a menudo se utilizan bibliotecas como `pexpect` (para Unix) o equivalentes que funcionan con pseudo-terminales (pty).

**Trabajar con codificaciones:**
*   Usa `text=True` (o `universal_newlines=True`) para la decodificación/codificación automática.
*   Si es necesario, puedes especificar `encoding="tu-codificación"` y `errors="manejador-de-errores"` (por ejemplo, `replace`, `ignore`).
*   Si `text=False` (predeterminado), `stdout` y `stderr` serán cadenas de bytes. Deberás decodificarlas manualmente: `result.stdout.decode('utf-8', errors='replace')`.

--- 

### 6. Seguridad y mejores prácticas

*   **Riesgos de `shell=True` e inyección de comandos:**
    *   **Nunca** uses `shell=True` con comandos construidos a partir de entrada de usuario no confiable. Esto abre la puerta a la inyección de comandos.
    *   Ejemplo de vulnerabilidad:
        ```python
        # ¡PELIGROSO!
        filename = input("Introduce el nombre del archivo a eliminar: ") # El usuario introduce "miarchivoinocente.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Si `shell=True` es absolutamente necesario (por ejemplo, para usar tuberías `|` o sustituciones `*` directamente en la cadena de comandos), escapa cuidadosamente todas las partes del comando formadas a partir de entrada externa usando `shlex.quote()` (a partir de Python 3.3).

*   **Validación y escape de la entrada del usuario:**
    *   Incluso si `shell=False`, si los argumentos del comando se forman a partir de la entrada del usuario, deben validarse. Por ejemplo, si se espera un nombre de archivo, asegúrate de que sea realmente un nombre de archivo válido y no algo como `../../../etc/passwd`.

*   **Pasar argumentos como una lista (cuando `shell=False`):**
    *   Esta es la forma más segura. Cada argumento se pasa como un elemento de lista separado, y el sistema operativo los maneja correctamente, sin intentar interpretarlos como parte del comando del shell.
    *   Ejemplo: `subprocess.run(["rm", filename_from_user])` — aquí `filename_from_user` siempre se tratará como un único argumento (nombre de archivo), incluso si contiene espacios o caracteres especiales.

*   **Manejo de errores y códigos de retorno:**
    *   Siempre verifica `returncode` o usa `check=True` (para `run()`) / `check_call()` / `check_output()` para asegurarte de que el comando se ejecutó correctamente.
    *   Maneja las posibles excepciones (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Gestión de recursos:**
    *   Si abres tuberías (`PIPE`), asegúrate de que finalmente se cierren. `Popen.communicate()` lo hace automáticamente. Si trabajas directamente con `p.stdin/stdout/stderr`, puede ser necesario cerrarlos explícitamente.
    *   En aplicaciones de larga duración, asegúrate de que los procesos secundarios terminen correctamente y no se conviertan en "zombies". Usa `p.wait()` o `p.communicate()`. Si es necesario, usa `p.terminate()` o `p.kill()`.

*   **Codificaciones:** Ten cuidado con las codificaciones al usar `text=True` o al decodificar manualmente cadenas de bytes. Los problemas de codificación son una fuente común de errores.

--- 

### 7. Ejemplos prácticos

**1. Ejecutar un comando simple y verificar el código de retorno:**
```python
import subprocess

try:
    # Ejecutamos 'ls' para un directorio existente
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Comando 'ls /tmp' ejecutado, código de retorno: {result.returncode}")

    # Ejecutamos 'ls' para un directorio inexistente
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Esta línea no se ejecutará si check=True, ya que se lanzará una excepción
except subprocess.CalledProcessError as e:
    print(f"Error de ejecución de comando: {e.cmd}")
    print(f"Código de retorno: {e.returncode}")
    if e.stderr:
        print(f"Stderr: {e.stderr.strip()}")
```

**2. Capturar la salida del comando:**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Especificar el directorio actual como de trabajo para git
    )
    print("Estado de Git:")
    print(result.stdout)
except FileNotFoundError:
    print("Error: comando 'git' no encontrado. ¿Está Git instalado y en PATH?")
except subprocess.CalledProcessError as e:
    print(f"Error de Git: {e.stderr}")
```

**3. Enviar datos a la entrada del proceso (usando `communicate`):**
```python
import subprocess

# Enviamos texto a 'grep' para buscar
input_text = "hola mundo\npython es divertido\nhello python"
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
        print("No se encontraron coincidencias de 'python'.")
    else: # otro error de grep
        print(f"Error de grep (código {process.returncode}):")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep no respondió a tiempo.")
    process.kill() # Matar el proceso si se colgó
    process.communicate() # Recopilar la salida/errores restantes
```

**4. Crear una tubería (`ls -l | wc -l`) sin `shell=True`:**
(Un ejemplo más detallado estaba en la sección 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # Asegurarse de que stdout exista
    ls_proc.stdout.close()  # Permite que wc_proc reciba EOF cuando ls_proc termine

output, _ = wc_proc.communicate()
print(f"Número de archivos/directorios: {output.strip()}")
```

**5. Uso de `timeout`:**
```python
import subprocess

try:
    # Comando que se ejecutará durante 5 segundos
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Comando 'sleep 5' completado (no debería haberlo hecho con timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Comando '{e.cmd}' no finalizó en {e.timeout} segundos.")
```

--- 

### 8. Conclusión y recursos útiles

El módulo `subprocess` es una herramienta indispensable para cualquier desarrollador de Python que necesite interactuar con programas externos o el entorno del sistema. Ofrece un equilibrio entre la facilidad de uso (a través de `subprocess.run()`) y una potente flexibilidad (a través de `subprocess.Popen()`).

**Puntos clave:**
*   Prefiere `subprocess.run()` para la mayoría de las tareas.
*   Usa `subprocess.Popen()` para la ejecución asíncrona o la gestión compleja de flujos.
*   **Evita `shell=True`**, especialmente con la entrada del usuario, debido a los riesgos de seguridad. Pasa los comandos como una lista de argumentos.
*   Siempre maneja los códigos de retorno y las posibles excepciones.
*   Ten cuidado con las codificaciones al trabajar con la salida de texto (`text=True` o decodificación manual).
*   `communicate()` es tu amigo para el intercambio seguro de datos a través de `PIPE`.

**Recursos útiles:**
*   Documentación oficial de Python para el módulo `subprocess`: [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - Un nuevo módulo de proceso: [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)

```