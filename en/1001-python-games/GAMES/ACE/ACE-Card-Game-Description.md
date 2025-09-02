ACE:
=================
Difficulty: 7
-----------------
The game "ACE" is a game in which two players take turns drawing cards from a deck and try to score more points. An Ace counts as 1 point, cards from 2 to 10 count as their face value, and Jack, Queen, and King count as 10. The player with more points wins. The game continues until a certain number of rounds are played.

Game rules:
1. Two players play.
2. Players take turns drawing cards from the deck.
3. Each card has a certain number of points: Ace - 1, cards from 2 to 10 - face value, Jack, Queen, and King - 10.
4. Each player tries to score as many points as possible per round.
5. At the end of the round, players' scores are compared.
6. The game consists of a certain number of rounds.
7. The player with more points across all rounds is declared the winner of the game.
-----------------
Algorithm:
1. Initialize player 1 and player 2 scores to zero.
2. Prompt for the number of rounds.
3. Start a loop for the number of rounds:
    3.1. Player 1 draws a card.
    3.2. Display player 1's card and card points.
    3.3. Add card points to player 1's total score.
    3.4. Player 2 draws a card.
    3.5. Display player 2's card and card points.
    3.6. Add card points to player 2's total score.
    3.7. If player 1's score is greater than player 2's score, display "PLAYER 1 WINS THE ROUND".
    3.8. If player 2's score is greater than player 1's score, display "PLAYER 2 WINS THE ROUND".
    3.9. If player 1's score is equal to player 2's score, display "TIE GAME THIS ROUND".
4. Display player 1's total score.
5. Display player 2's total score.
6. If player 1's total score is greater than player 2's total score, display "PLAYER 1 WINS THE GAME".
7. If player 2's total score is greater than player 1's total score, display "PLAYER 2 WINS THE GAME".
8. If player 1's total score is equal to player 2's total score, display "TIE GAME".
9. End of game.
-----------------
Flowchart:
```mermaid
flowchart TD
    Start["Start"] --> InitializeScores["<p align='left'>Initialize variables:<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["Input number of rounds: <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"Start round loop"}
    RoundLoopStart -- Yes --> Player1DrawsCard["Player 1 draws card: <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["Display player 1's card and points: <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["Player 2 draws card: <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["Display player 2's card and points: <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"Compare round scores: <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- Yes --> OutputPlayer1RoundWin["Display: <b>PLAYER 1 WINS THE ROUND</b>"]
    CompareScores -- No --> CompareScores2{"Compare round scores: <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- Yes --> OutputPlayer2RoundWin["Display: <b>PLAYER 2 WINS THE ROUND</b>"]
    CompareScores2 -- No --> OutputTieRound["Display: <b>TIE GAME THIS ROUND</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
     RoundLoopEnd --> RoundLoopStart {"Start round loop"}

    RoundLoopStart -- No --> OutputTotalPlayer1Score["Display player 1's total score: <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["Display player 2's total score: <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"Compare total scores: <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- Yes --> OutputPlayer1GameWin["Display: <b>PLAYER 1 WINS THE GAME</b>"]
    CompareTotalScores -- No --> CompareTotalScores2{"Compare total scores: <code><b>player2Score > player1Score?</b></code>"}
     CompareTotalScores2 -- Yes --> OutputPlayer2GameWin["Display: <b>PLAYER 2 WINS THE GAME</b>"]
    CompareTotalScores2 -- No --> OutputTieGame["Display: <b>TIE GAME</b>"]
    OutputPlayer1GameWin --> End["End"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```
**Legend**
    Start - Program start.
    InitializeScores - Initialize player1Score and player2Score variables to zero.
    InputRounds - Prompt user for the number of rounds numberOfRounds for the game.
    RoundLoopStart - Start loop for each game round. The loop executes numberOfRounds times.
    Player1DrawsCard - Player 1 draws card card1 and its value card1Value is determined.
    OutputPlayer1Card - Display information about player 1's card card1 and its value card1Value.
    UpdatePlayer1Score - Update player 1's total score, adding card1Value to player1Score.
    Player2DrawsCard - Player 2 draws card card2 and its value card2Value is determined.
    OutputPlayer2Card - Display information about player 2's card card2 and its value card2Value.
    UpdatePlayer2Score - Update player 2's total score, adding card2Value to player2Score.
    CompareScores - Compare card values card1Value and card2Value to determine the round winner.
    OutputPlayer1RoundWin - Display message about player 1 winning the round.
    CompareScores2 - Compare card values card2Value and card1Value to determine the round winner.
    OutputPlayer2RoundWin - Display message about player 2 winning the round.
    OutputTieRound - Display message about a tie in the round.
    RoundLoopEnd - End of round loop.
    OutputTotalPlayer1Score - Display player 1's total score player1Score.
    OutputTotalPlayer2Score - Display player 2's total score player2Score.
    CompareTotalScores - Compare total scores of players player1Score and player2Score to determine the game winner.
    OutputPlayer1GameWin - Display message about player 1 winning the game.
     CompareTotalScores2 - Compare total scores of players player2Score and player1Score to determine the game winner.
    OutputPlayer2GameWin - Display message about player 2 winning the game.
    OutputTieGame - Display message about a tie in the game.
    End - Program end.