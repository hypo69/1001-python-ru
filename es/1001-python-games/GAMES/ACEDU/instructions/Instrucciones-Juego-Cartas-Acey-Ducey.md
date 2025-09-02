### Nombre del juego: **Juego de cartas Acey-Ducey**

#### Descripción
Esta es una simulación del juego de cartas Acey-Ducey. El jugador realiza apuestas basándose en la probabilidad de que la siguiente carta caiga entre dos cartas ya abiertas.

- **Capital inicial:** El jugador comienza con 100 dólares.
- **Reglas del juego:**
  1. La computadora reparte dos cartas.
  2. El jugador puede decidir si apostar o no.
  3. Si se realiza una apuesta, se saca una tercera carta.
  4. Si el valor de la tercera carta cae entre las dos primeras cartas, el jugador gana la apuesta. De lo contrario, la apuesta se pierde.
- El juego termina cuando el jugador pierde todo su capital o lo finaliza manualmente.

#### Implementación

**Datos de entrada:**
- Entrada del usuario para:
  - Tamaño de la apuesta inicial.
  - Decisión de apostar o pasar.

**Datos de salida:**
- Mensaje sobre el capital actual del jugador.
- Información sobre los resultados de la apuesta (ganancia/pérdida).
- Estado de las cartas en cada ronda.

#### Instrucciones paso a paso para la implementación:

1. **Inicialización del juego**:
   - Establecer el capital inicial del jugador (100 dólares).
   - Anunciar las reglas del juego.

2. **Bucle principal del juego**:
   - Generar dos cartas aleatorias (rango 2–14, donde 11 = Jota, 12 = Reina, 13 = Rey, 14 = As).
   - Mostrar las cartas al jugador.
   - Solicitar una apuesta (se puede saltar la ronda apostando 0).
   - Comprobar: la apuesta no debe exceder el capital actual.

3. **Resultado de la ronda**:
   - Generar una tercera carta.
   - Comprobar si su valor cae dentro del rango entre las dos primeras cartas.
   - Cambiar el capital del jugador según el resultado.

4. **Fin del juego**:
   - Si el capital del jugador es 0, el juego termina con un mensaje apropiado.
   - Ofrecer al jugador comenzar un nuevo juego o salir.

#### Limitaciones
- Todas las cartas son únicas dentro de una sola ronda.
- Soporte para la funcionalidad básica del juego sin efectos visuales complejos.
