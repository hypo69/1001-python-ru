CHIEF:
=================
Dificultad: 4
-----------------
El juego "CHIEF" es un juego en el que el jugador actúa como jefe de fábrica, planificando la producción. El jugador establece la cantidad de productos fabricados de cada tipo, y la computadora determina si estos valores cumplen con los requisitos necesarios. Si no, se le informa al jugador qué valores fueron incorrectos. El objetivo del juego es lograr una producción óptima, adivinando correctamente la cantidad de productos.

Reglas del juego:
1. La computadora adivina tres valores en el rango de 1 a 10: `targetA`, `targetB` y `targetC`.
2. El jugador ingresa sus suposiciones para los valores `userA`, `userB` y `userC`.
3. La computadora verifica si los valores ingresados coinciden con los adivinados.
4. Si los tres valores se adivinan correctamente, el juego termina con una victoria.
5. Si al menos un valor no coincide, la computadora muestra qué valores fueron incorrectos.
6. El juego continúa hasta que el jugador adivina los tres valores.
-----------------
Algoritmo:
1.  Generar números enteros aleatorios `targetA`, `targetB` y `targetC` en el rango de 1 a 10.
2.  Iniciar un bucle "mientras no se adivinen todos los números":
    2.1. Solicitar al jugador que ingrese tres números enteros: `userA`, `userB` y `userC`.
    2.2. Inicializar la cadena `message` como vacía.
    2.3. Si `userA` no es igual a `targetA`, agregar "A" a `message`.
    2.4. Si `userB` no es igual a `targetB`, agregar "B" a `message`.
    2.5. Si `userC` no es igual a `targetC`, agregar "C" a `message`.
    2.6. Si `message` no está vacía, mostrar el mensaje "WRONG ON " y `message`.
    2.7. De lo contrario, mostrar el mensaje "YOU GOT IT!".
3. Fin del juego.
-----------------
Diagrama de flujo:
```mermaid
flowchart TD
    Start["Inicio"] --> InitializeVariables["<p align='left'>Inicialización de variables:
    <code><b>
    targetA = random(1, 10)
    targetB = random(1, 10)
    targetC = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Iniciar bucle: mientras no se adivine"}
    LoopStart --> InputValues["<p align='left'>El usuario ingresa números:
    <code><b>
    userA
    userB
    userC
    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"Comprobar: <code><b>userA == targetA?</b></code>"}
    CheckA -- No --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"Comprobar: <code><b>userB == targetB?</b></code>"}
    CheckA -- Sí --> CheckB
    CheckB -- No --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"Comprobar: <code><b>userC == targetC?</b></code>"}
    CheckB -- Sí --> CheckC
    CheckC -- No --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"Comprobar: <code><b>message != "" ?</b></code>"}
    CheckC -- Sí --> CheckMessage
    CheckMessage -- Sí --> OutputWrong["Mostrar mensaje: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- No --> OutputWin["Mostrar mensaje: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Fin"]
    LoopStart -- No --> End
```
Leyenda:
    Start - Inicio del programa.
    InitializeVariables - Inicialización de variables: `targetA`, `targetB`, `targetC` se generan aleatoriamente del 1 al 10.
    LoopStart - Inicio del bucle, que continúa hasta que el jugador adivina todos los números.
    InputValues - Solicitar al usuario que ingrese tres números `userA`, `userB`, `userC`.
    InitializeMessage - Inicialización de una cadena vacía `message`.
    CheckA - Comprobar si el número ingresado `userA` es igual al número oculto `targetA`.
    AppendA - Agregar 'A' a `message` si `userA` no es igual a `targetA`.
    CheckB - Comprobar si el número ingresado `userB` es igual al número oculto `targetB`.
    AppendB - Agregar 'B' a `message` si `userB` no es igual a `targetB`.
    CheckC - Comprobar si el número ingresado `userC` es igual al número oculto `targetC`.
    AppendC - Agregar 'C' a `message` si `userC` no es igual a `targetC`.
    CheckMessage - Comprobar si la cadena `message` está vacía.
    OutputWrong - Mostrar mensaje "WRONG ON" y el contenido de `message`, si la cadena no está vacía.
    OutputWin - Mostrar mensaje "YOU GOT IT!", si la cadena `message` está vacía.
    End - Fin del programa.