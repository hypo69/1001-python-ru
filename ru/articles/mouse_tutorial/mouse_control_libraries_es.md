# Control del Ratón en Python: Resumen y Comparación de Librerías

La automatización de las acciones del ratón es una herramienta poderosa para pruebas, investigación científica, procesos de negocio y la creación de tecnologías de asistencia. Dentro del ecosistema de Python, existen varias librerías para estos propósitos, cada una con sus propias fortalezas y casos de uso. En este artículo, examinaremos en detalle tres librerías multiplataforma principales: `PyAutoGUI`, `pynput` y `mouse`, y también mencionaremos brevemente otras soluciones especializadas.

## 1. Librería PyAutoGUI: Automatización GUI de Alto Nivel

`PyAutoGUI` es una librería multiplataforma potente y fácil de usar que permite a los scripts de Python controlar el ratón y el teclado, tomar capturas de pantalla y realizar otras tareas de automatización de la interfaz gráfica de usuario (GUI). Es ideal para automatizar tareas rutinarias, probar software y crear bots. **Soporta Windows, macOS y Linux.**

### Instalación

```bash
pip install pyautogui
```

### Características Clave

*   **Movimiento del Cursor**: `pyautogui.moveTo(x, y, duration=seconds)` para movimiento absoluto y `pyautogui.move(xOffset, yOffset, duration=seconds)` para movimiento relativo.
*   **Clics del Ratón**: `pyautogui.click()`, `pyautogui.rightClick()`, `pyautogui.doubleClick()`, `pyautogui.tripleClick()`. Puedes especificar coordenadas y el botón.
*   **Arrastrar y Soltar (Drag and Drop)**: `pyautogui.dragTo(x, y, duration=seconds)` o `pyautogui.drag(xOffset, yOffset, duration=seconds)`.
*   **Desplazamiento de la Rueda del Ratón**: `pyautogui.scroll(amount)` (valor positivo desplaza hacia arriba, negativo hacia abajo).
*   **Interacción con el Teclado**: `pyautogui.write()`, `pyautogui.press()`, `pyautogui.hotkey()`.
*   **Obtener Posición del Cursor**: `pyautogui.position()`.
*   **Failsafe**: Una característica de seguridad incorporada que detiene el script cuando el cursor del ratón se mueve a una de las cuatro esquinas de la pantalla.

### Ejemplos de Uso

```python
import pyautogui
import time

# Mover cursor
pyautogui.moveTo(100, 150, duration=1)
print(f"Cursor movido a {pyautogui.position()}")

# Clic izquierdo
pyautogui.click(200, 250)
print("Clic realizado.")

# Arrastrar
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.dragTo(600, 600, duration=1)
print("Arrastre realizado.")

# Desplazar rueda
pyautogui.scroll(-100)
print("Desplazamiento hacia abajo realizado.")

# Escribir texto
pyautogui.write('Hola, PyAutoGUI!', interval=0.1)
print("Texto escrito.")
```

### ¿Cuándo usar PyAutoGUI?

✅ Ideal si necesitas una forma rápida y sencilla de automatizar acciones de usuario, simular entradas y tomar capturas de pantalla. Es excelente para scripts de automatización de alto nivel donde no se requiere un control detallado sobre los eventos de entrada.

❌ No es la mejor opción para el monitoreo de eventos de bajo nivel o el bloqueo de entradas.

## 2. Librería pynput: Control y Monitoreo Flexible

`pynput` es una herramienta moderna y activamente mantenida para el monitoreo y control integral de dispositivos de entrada. Proporciona acceso detallado a los eventos del ratón y el teclado, incluida la capacidad de bloquear o modificarlos en tiempo real. **Soporta Windows, macOS y Linux.**

### Instalación

```bash
pip install pynput
```

### Características Clave

*   **Escuchadores de Eventos Completos**: `pynput.mouse.Listener` permite rastrear movimientos, clics y desplazamientos con acceso a coordenadas, tipo de botón y estado (presionado/soltado).
*   **Bloqueo de Eventos**: Si un manejador de eventos devuelve `False`, el evento no se pasa al sistema. Esta es una característica única y potente.
*   **Control del Ratón a través del Controlador**: `pynput.mouse.Controller` para emular acciones (posicionamiento, movimiento relativo, clics, desplazamiento).
*   **Arquitectura Unificada de Teclado**: Combina fácilmente acciones del ratón y el teclado.
*   **Seguridad de Hilos**: Los escuchadores operan en hilos separados, proporcionando una gestión flexible.

### Ejemplos de Uso

```python
from pynput import mouse
from pynput.mouse import Controller, Button
import time

# Control del ratón
mouse_ctrl = Controller()
print(f"Posición actual: {mouse_ctrl.position}")
mouse_ctrl.position = (100, 200)
mouse_ctrl.move(50, -50)
mouse_ctrl.click(Button.left, 1)
mouse_ctrl.scroll(0, 2)
print("Acciones del ratón realizadas.")

# Escuchador de eventos
def on_click(x, y, button, pressed):
    print(f"Clic en ({x}, {y}) con botón {button}. Presionado: {pressed}")
    if not pressed:
        # Detener escuchador después de soltar el botón
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
print("Escuchador activo. Haz clic con el ratón.")
listener.join() # Esperar a que el escuchador termine
print("Escuchador terminado.")
```

### ¿Cuándo usar pynput?

✅ Ideal si:
- Necesitas **analizar el comportamiento del usuario** (coordenadas, trayectorias, frecuencia de clics).
- Estás creando **sistemas de teclas de acceso rápido**, **filtros de entrada** o **tecnologías de asistencia**.
- Quieres **bloquear o modificar la entrada** en tiempo real.
- Estás realizando un **experimento científico**, **pruebas de usabilidad** o un **sistema de seguridad**.
- Se requiere **integración de ratón y teclado** en un solo script.

❌ No es la opción más rápida si solo necesitas grabar y reproducir acciones sin análisis.

## 3. Librería mouse: Simplicidad y Grabación de Acciones

La librería `mouse` es una herramienta minimalista pero efectiva para emular y grabar secuencias de acciones del ratón. Su característica principal es el soporte incorporado para la grabación y reproducción, lo que la hace ideal para la creación rápida de prototipos de macros. **Soporta Windows, macOS y Linux.**

### Instalación

```bash
pip install mouse
```

### Características Clave

*   **Movimiento del Cursor**: `mouse.move(x, y, absolute=True/False)`.
*   **Clics del Ratón**: `mouse.click('left'/'right'/'middle')`.
*   **Arrastrar y Soltar**: `mouse.drag(x1, y1, x2, y2, absolute=True)`.
*   **Rueda de Desplazamiento**: `mouse.wheel(delta)`.
*   **Obtener Posición del Cursor**: `mouse.get_position()`.
*   **Verificar Estado del Botón**: `mouse.is_pressed(button)`.
*   **Grabar y Reproducir Eventos**: `mouse.record()` y `mouse.play()`. Esta es una función incorporada única.
*   **Manejador de Clic Simple**: `mouse.on_click(handler)`.

### Ejemplos de Uso

```python
import mouse
import time

# Mover y hacer clic
mouse.move(200, 300, absolute=True, duration=0.2)
mouse.click('left')
print("Movimiento y clic realizados.")

# Grabar y reproducir (requiere entrada interactiva)
print("Comienza la grabación. Presiona el botón derecho para detener.")
# events = mouse.record()
# print("Grabación finalizada. Reproduciendo...")
# mouse.play(events[:-1]) # Reproducir todo excepto el último evento (soltar el botón derecho)
# print("Reproducción finalizada.")

# Desplazar
mouse.wheel(-2)
print("Desplazamiento hacia abajo realizado.")
```

### ¿Cuándo usar mouse?

✅ Ideal para:
- Grabar y reproducir acciones rutinarias.
- Scripts de automatización simples sin retroalimentación.
- Ejemplos educativos y demostraciones donde la máxima simplicidad es clave.

❌ No es adecuado para:
- Analizar el comportamiento del usuario (los manejadores no reciben coordenadas).
- Crear filtros o bloqueadores de entrada.
- Integración de teclado.
- El proyecto no se ha actualizado desde 2021, lo que puede ser un riesgo para proyectos a largo plazo.

## 4. Otras Librerías Notables

Aunque `PyAutoGUI`, `pynput` y `mouse` son las más versátiles, existen otras librerías para tareas más específicas:

*   **PyDirectInput**: Una librería especializada diseñada como alternativa a `PyAutoGUI` para la automatización de juegos. Puede evitar problemas en los que algunos juegos no registran la entrada de `PyAutoGUI` debido a sus mecanismos específicos de manejo de entrada.
*   **pywinauto**: Centrada en la automatización de la interfaz de usuario de Windows. Interactúa con los controles de Windows utilizando marcos de accesibilidad y automatización de UI, lo que la convierte en una opción confiable para automatizar aplicaciones nativas de Windows al apuntar a elementos en lugar de coordenadas de pantalla.

## 5. Tabla Comparativa

| Característica / Librería | PyAutoGUI | pynput | mouse |
|---------------------------|:---------:|:------:|:-----:|
| **Soporte de SO**        | Windows, macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux |
|---------------------------|:---------:|:------:|:-----:|
| **Instalación**           | `pip install pyautogui` | `pip install pynput` | `pip install mouse` |
| **Movimiento del Cursor** | ✅ Abs./Rel. | ✅ Abs./Rel. | ✅ Abs./Rel. |
| **Clics del Ratón**       | ✅ Todos los tipos | ✅ Todos los tipos | ✅ Todos los tipos |
| **Arrastrar y Soltar**    | ✅ `dragTo()` | ⚠️ Manual | ✅ `drag()` |
| **Rueda de Desplazamiento** | ✅ Sí       | ✅ Sí    | ✅ Sí   |
| **Obtener Posición**      | ✅ Sí       | ✅ Sí    | ✅ Sí   |
| **Verificar Estado del Botón** | ❌ No       | ⚠️ Via Listener | ✅ Sí   |
| **Grabar/Reproducir**     | ❌ No       | ❌ No (solo manual) | ✅ Incorporado |
| **Coordenadas en Manejador** | ❌ No       | ✅ Sí    | ❌ No   |
| **Bloqueo de Eventos**    | ❌ No       | ✅ Sí (`return False`) | ❌ No   |
| **Integración con Teclado** | ✅ Sí       | ✅ Sí    | ❌ No   |
| **Soporte Activo**        | ✅ Sí       | ✅ Sí    | ❌ No (desde 2021) |
| **Failsafe**              | ✅ Sí       | ❌ No    | ❌ No   |
| **Complejidad API**       | Media       | Media/Alta | Baja  |

## Conclusión

La elección de una librería de control del ratón en Python depende de tus necesidades específicas:

*   **PyAutoGUI**: Tu elección predeterminada para la automatización GUI de alto nivel cuando necesitas simular acciones de usuario, incluyendo teclado y capturas de pantalla, sin un análisis profundo de eventos.
*   **pynput**: Ideal para proyectos que requieren un control preciso sobre los eventos del ratón (y teclado), monitoreo, análisis, así como la capacidad de bloquear o modificar la entrada en tiempo real. Es una herramienta profesional para sistemas complejos.
*   **mouse**: Más adecuada para tareas simples de grabación y reproducción de macros, donde la máxima simplicidad y el código mínimo son importantes. Sin embargo, debe considerarse la falta de soporte activo.

Para nuevos proyectos que requieren flexibilidad y soporte a largo plazo, se recomienda `pynput`. Si tu tarea es la automatización rápida de acciones rutinarias, `PyAutoGUI` será una excelente opción.
