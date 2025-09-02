CHIEF:
=================
Difficulty: 4
-----------------
The game "CHIEF" is a game in which the player acts as a factory manager, planning production. The player sets the quantity of each type of product, and the computer determines whether these values meet the required specifications. If not, the player is informed which values were incorrect. The goal of the game is to achieve optimal production by correctly guessing the quantity of products.

Game rules:
1. The computer guesses three values in the range of 1 to 10: `targetA`, `targetB`, and `targetC`.
2. The player enters their guesses for `userA`, `userB`, and `userC`.
3. The computer checks if the entered values match the guessed ones.
4. If all three values are guessed correctly, the game ends with a win.
5. If at least one value does not match, the computer outputs which values were incorrect.
6. The game continues until the player guesses all three values.
-----------------
Algorithm:
1.  Generate random integers `targetA`, `targetB`, and `targetC` in the range of 1 to 10.
2.  Start a loop "while not all numbers are guessed":
    2.1. Prompt the player to enter three integers: `userA`, `userB`, and `userC`.
    2.2. Initialize the `message` string as empty.
    2.3. If `userA` is not equal to `targetA`, add "A" to `message`.
    2.4. If `userB` is not equal to `targetB`, add "B" to `message`.
    2.5. If `userC` is not equal to `targetC`, add "C" to `message`.
    2.6. If `message` is not empty, display "WRONG ON " and `message`.
    2.7. Otherwise, display "YOU GOT IT!".
3. End of game.
-----------------
Flowchart:
```mermaid
flowchart TD
    Start["Start"] --> InitializeVariables["<p align='left'>Initialize variables:
    <code><b>
    targetA = random(1, 10)
    targetB = random(1, 10)
    targetC = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Start loop: until guessed"}
    LoopStart --> InputValues["<p align='left'>User inputs numbers:
    <code><b>
    userA
    userB
    userC
    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"Check: <code><b>userA == targetA?</b></code>"}
    CheckA -- No --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"Check: <code><b>userB == targetB?</b></code>"}
    CheckA -- Yes --> CheckB
    CheckB -- No --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"Check: <code><b>userC == targetC?</b></code>"}
    CheckB -- Yes --> CheckC
    CheckC -- No --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"Check: <code><b>message != "" ?</b></code>"}
    CheckC -- Yes --> CheckMessage
    CheckMessage -- Yes --> OutputWrong["Display message: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- No --> OutputWin["Display message: <b>YOU GOT IT!</b>"]
    OutputWin --> End["End"]
    LoopStart -- No --> End
```
Legend:
    Start - Program start.
    InitializeVariables - Initialize variables: `targetA`, `targetB`, `targetC` are randomly generated from 1 to 10.
    LoopStart - Start of the loop, which continues until the player guesses all numbers.
    InputValues - Prompt the user for three numbers `userA`, `userB`, `userC`.
    InitializeMessage - Initialize an empty string `message`.
    CheckA - Check if the entered number `userA` is equal to the hidden number `targetA`.
    AppendA - Add 'A' to `message` if `userA` is not equal to `targetA`.
    CheckB - Check if the entered number `userB` is equal to the hidden number `targetB`.
    AppendB - Add 'B' to `message` if `userB` is not equal to `targetB`.
    CheckC - Check if the entered number `userC` is equal to the hidden number `targetC`.
    AppendC - Add 'C' to `message` if `userC` is not equal to `targetC`.
    CheckMessage - Check if the `message` string is empty.
    OutputWrong - Display "WRONG ON" message and `message` content if the string is not empty.
    OutputWin - Display "YOU GOT IT!" message if the `message` string is empty.
    End - End of program.