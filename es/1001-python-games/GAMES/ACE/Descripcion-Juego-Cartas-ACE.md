ACE:
=================
Dificultad: 7
-----------------
El juego "ACE" es un juego en el que dos jugadores se turnan para sacar cartas de una baraja e intentar sumar más puntos. Un As cuenta como 1 punto, las cartas del 2 al 10 cuentan por su valor nominal, y la Jota, la Reina y el Rey cuentan como 10. El jugador con más puntos gana. El juego continúa hasta que se juega un cierto número de rondas.

Reglas del juego:
1. Juegan dos jugadores.
2. Los jugadores se turnan para sacar cartas de la baraja.
3. Cada carta tiene un cierto número de puntos: As - 1, cartas del 2 al 10 - valor nominal, Jota, Reina y Rey - 10.
4. Cada jugador intenta sumar la mayor cantidad de puntos posible por ronda.
5. Al final de la ronda, se comparan las puntuaciones de los jugadores.
6. El juego consta de un cierto número de rondas.
7. El jugador con más puntos en todas las rondas es declarado ganador del juego.
-----------------
Algoritmo:
1. Inicializar las puntuaciones del jugador 1 y del jugador 2 a cero.
2. Solicitar el número de rondas.
3. Iniciar un bucle para el número de rondas:
    3.1. El jugador 1 saca una carta.
    3.2. Mostrar la carta del jugador 1 y los puntos de la carta.
    3.3. Sumar los puntos de la carta a la puntuación total del jugador 1.
    3.4. El jugador 2 saca una carta.
    3.5. Mostrar la carta del jugador 2 y los puntos de la carta.
    3.6. Sumar los puntos de la carta a la puntuación total del jugador 2.
    3.7. Si la puntuación del jugador 1 es mayor que la puntuación del jugador 2, mostrar "PLAYER 1 WINS THE ROUND".
    3.8. Si la puntuación del jugador 2 es mayor que la puntuación del jugador 1, mostrar "PLAYER 2 WINS THE ROUND".
    3.9. Si la puntuación del jugador 1 es igual a la puntuación del jugador 2, mostrar "TIE GAME THIS ROUND".
4. Mostrar la puntuación total del jugador 1.
5. Mostrar la puntuación total del jugador 2.
6. Si la puntuación total del jugador 1 es mayor que la puntuación total del jugador 2, mostrar "PLAYER 1 WINS THE GAME".
7. Si la puntuación total del jugador 2 es mayor que la puntuación total del jugador 1, mostrar "PLAYER 2 WINS THE GAME".
8. Si la puntuación total del jugador 1 es igual a la puntuación total del jugador 2, mostrar "TIE GAME".
9. Fin del juego.
-----------------
Diagrama de flujo:
```mermaid
flowchart TD
    Start["Inicio"] --> InitializeScores["<p align='left'>Inicializar variables:<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["Introducir número de rondas: <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"Iniciar bucle de rondas"}
    RoundLoopStart -- Sí --> Player1DrawsCard["Jugador 1 saca carta: <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["Mostrar carta y puntos del jugador 1: <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["Jugador 2 saca carta: <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["Mostrar carta y puntos del jugador 2: <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"Comparar puntuaciones de ronda: <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- Sí --> OutputPlayer1RoundWin["Mostrar: <b>PLAYER 1 WINS THE ROUND</b>"]
    CompareScores -- No --> CompareScores2{"Comparar puntuaciones de ronda: <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- Sí --> OutputPlayer2RoundWin["Mostrar: <b>PLAYER 2 WINS THE ROUND</b>"]
    CompareScores2 -- No --> OutputTieRound["Mostrar: <b>TIE GAME THIS ROUND</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
     RoundLoopEnd --> RoundLoopStart {"Iniciar bucle de rondas"}

    RoundLoopStart -- No --> OutputTotalPlayer1Score["Mostrar puntuación total del jugador 1: <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["Mostrar puntuación total del jugador 2: <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"Comparar puntuaciones totales: <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- Sí --> OutputPlayer1GameWin["Mostrar: <b>PLAYER 1 WINS THE GAME</b>"]
    CompareTotalScores -- No --> CompareTotalScores2{"Comparar puntuaciones totales: <code><b>player2Score > player1Score?</b></code>"}
     CompareTotalScores2 -- Sí --> OutputPlayer2GameWin["Mostrar: <b>PLAYER 2 WINS THE GAME</b>"]
    CompareTotalScores2 -- No --> OutputTieGame["Mostrar: <b>TIE GAME</b>"]
    OutputPlayer1GameWin --> End["Fin"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```
**Leyenda**
    Start - Inicio del programa.
    InitializeScores - Inicializar las variables player1Score y player2Score a cero.
    InputRounds - Solicitar al usuario el número de rondas numberOfRounds para el juego.
    RoundLoopStart - Iniciar el bucle para cada ronda del juego. El bucle se ejecuta numberOfRounds veces.
    Player1DrawsCard - El jugador 1 saca la carta card1 y se determina su valor card1Value.
    OutputPlayer1Card - Mostrar información sobre la carta card1 del jugador 1 y su valor card1Value.
    UpdatePlayer1Score - Actualizar la puntuación total del jugador 1, sumando card1Value a player1Score.
    Player2DrawsCard - El jugador 2 saca la carta card2 y se determina su valor card2Value.
    OutputPlayer2Card - Mostrar información sobre la carta card2 del jugador 2 y su valor card2Value.
    UpdatePlayer2Score - Actualizar la puntuación total del jugador 2, sumando card2Value a player2Score.
    CompareScores - Comparar los valores de las cartas card1Value y card2Value para determinar el ganador de la ronda.
    OutputPlayer1RoundWin - Mostrar mensaje sobre la victoria del jugador 1 en la ronda.
    CompareScores2 - Comparar los valores de las cartas card2Value y card1Value para determinar el ganador de la ronda.
    OutputPlayer2RoundWin - Mostrar mensaje sobre la victoria del jugador 2 en la ronda.
    OutputTieRound - Mostrar mensaje sobre un empate en la ronda.
    RoundLoopEnd - Fin del bucle de rondas.
    OutputTotalPlayer1Score - Mostrar la puntuación total del jugador 1 player1Score.
    OutputTotalPlayer2Score - Mostrar la puntuación total del jugador 2 player2Score.
    CompareTotalScores - Comparar las puntuaciones totales de los jugadores player1Score y player2Score para determinar el ganador del juego.
    OutputPlayer1GameWin - Mostrar mensaje sobre la victoria del jugador 1 en el juego.
     CompareTotalScores2 - Comparar las puntuaciones totales de los jugadores player2Score y player1Score para determinar el ganador del juego.
    OutputPlayer2GameWin - Mostrar mensaje sobre la victoria del jugador 2 en el juego.
    OutputTieGame - Mostrar mensaje sobre un empate en el juego.
    End - Fin del programa.