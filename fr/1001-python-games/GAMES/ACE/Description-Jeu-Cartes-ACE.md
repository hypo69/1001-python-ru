ACE:
=================
Difficulté : 7
-----------------
Le jeu "ACE" est un jeu dans lequel deux joueurs tirent à tour de rôle des cartes d'un paquet et tentent de marquer le plus de points. Un As compte pour 1 point, les cartes de 2 à 10 comptent pour leur valeur faciale, et le Valet, la Dame et le Roi comptent pour 10. Le joueur avec le plus de points gagne. Le jeu continue jusqu'à ce qu'un certain nombre de manches soient jouées.

Règles du jeu :
1. Deux joueurs jouent.
2. Les joueurs tirent à tour de rôle des cartes du paquet.
3. Chaque carte a un certain nombre de points : As - 1, cartes de 2 à 10 - valeur faciale, Valet, Dame et Roi - 10.
4. Chaque joueur essaie de marquer le plus de points possible par manche.
5. À la fin de la manche, les scores des joueurs sont comparés.
6. Le jeu se compose d'un certain nombre de manches.
7. Le joueur avec le plus de points sur toutes les manches est déclaré vainqueur du jeu.
-----------------
Algorithme :
1. Initialiser les scores des joueurs 1 et 2 à zéro.
2. Demander le nombre de manches.
3. Démarrer une boucle pour le nombre de manches :
    3.1. Le joueur 1 tire une carte.
    3.2. Afficher la carte du joueur 1 et les points de la carte.
    3.3. Ajouter les points de la carte au score total du joueur 1.
    3.4. Le joueur 2 tire une carte.
    3.5. Afficher la carte du joueur 2 et les points de la carte.
    3.6. Ajouter les points de la carte au score total du joueur 2.
    3.7. Si le score du joueur 1 est supérieur au score du joueur 2, afficher "PLAYER 1 WINS THE ROUND".
    3.8. Si le score du joueur 2 est supérieur au score du joueur 1, afficher "PLAYER 2 WINS THE ROUND".
    3.9. Si le score du joueur 1 est égal au score du joueur 2, afficher "TIE GAME THIS ROUND".
4. Afficher le score total du joueur 1.
5. Afficher le score total du joueur 2.
6. Si le score total du joueur 1 est supérieur au score total du joueur 2, afficher "PLAYER 1 WINS THE GAME".
7. Si le score total du joueur 2 est supérieur au score total du joueur 1, afficher "PLAYER 2 WINS THE GAME".
8. Si le score total du joueur 1 est égal au score total du joueur 2, afficher "TIE GAME".
9. Fin du jeu.
-----------------
Organigramme :
```mermaid
flowchart TD
    Start["Début"] --> InitializeScores["<p align='left'>Initialisation des variables :<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["Saisir le nombre de manches : <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"Début de la boucle des manches"}
    RoundLoopStart -- Oui --> Player1DrawsCard["Le joueur 1 tire une carte : <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["Afficher la carte et les points du joueur 1 : <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["Le joueur 2 tire une carte : <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["Afficher la carte et les points du joueur 2 : <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"Comparer les scores de la manche : <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- Oui --> OutputPlayer1RoundWin["Afficher : <b>PLAYER 1 WINS THE ROUND</b>"]
    CompareScores -- Non --> CompareScores2{"Comparer les scores de la manche : <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- Oui --> OutputPlayer2RoundWin["Afficher : <b>PLAYER 2 WINS THE ROUND</b>"]
    CompareScores2 -- Non --> OutputTieRound["Afficher : <b>TIE GAME THIS ROUND</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
     RoundLoopEnd --> RoundLoopStart {"Début de la boucle des manches"}

    RoundLoopStart -- Non --> OutputTotalPlayer1Score["Afficher le score total du joueur 1 : <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["Afficher le score total du joueur 2 : <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"Comparer les scores totaux : <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- Oui --> OutputPlayer1GameWin["Afficher : <b>PLAYER 1 WINS THE GAME</b>"]
    CompareTotalScores -- Non --> CompareTotalScores2{"Comparer les scores totaux : <code><b>player2Score > player1Score?</b></code>"}
     CompareTotalScores2 -- Oui --> OutputPlayer2GameWin["Afficher : <b>PLAYER 2 WINS THE GAME</b>"]
    CompareTotalScores2 -- Non --> OutputTieGame["Afficher : <b>TIE GAME</b>"]
    OutputPlayer1GameWin --> End["Fin"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```
**Légende**
    Start - Début du programme.
    InitializeScores - Initialisation des variables player1Score et player2Score à zéro.
    InputRounds - Demande à l'utilisateur du nombre de manches numberOfRounds pour le jeu.
    RoundLoopStart - Début de la boucle pour chaque manche du jeu. La boucle s'exécute numberOfRounds fois.
    Player1DrawsCard - Le joueur 1 tire la carte card1 et sa valeur card1Value est déterminée.
    OutputPlayer1Card - Affichage des informations sur la carte card1 du joueur 1 et sa valeur card1Value.
    UpdatePlayer1Score - Mise à jour du score total du joueur 1, en ajoutant card1Value à player1Score.
    Player2DrawsCard - Le joueur 2 tire la carte card2 et sa valeur card2Value est déterminée.
    OutputPlayer2Card - Affichage des informations sur la carte card2 du joueur 2 et sa valeur card2Value.
    UpdatePlayer2Score - Mise à jour du score total du joueur 2, en ajoutant card2Value à player2Score.
    CompareScores - Comparaison des valeurs des cartes card1Value et card2Value pour déterminer le vainqueur de la manche.
    OutputPlayer1RoundWin - Affichage du message concernant la victoire du joueur 1 dans la manche.
    CompareScores2 - Comparaison des valeurs des cartes card2Value et card1Value pour déterminer le vainqueur de la manche.
    OutputPlayer2RoundWin - Affichage du message concernant la victoire du joueur 2 dans la manche.
    OutputTieRound - Affichage du message concernant une égalité dans la manche.
    RoundLoopEnd - Fin de la boucle des manches.
    OutputTotalPlayer1Score - Affichage du score total du joueur 1 player1Score.
    OutputTotalPlayer2Score - Affichage du score total du joueur 2 player2Score.
    CompareTotalScores - Comparaison des scores totaux des joueurs player1Score et player2Score pour déterminer le vainqueur du jeu.
    OutputPlayer1GameWin - Affichage du message concernant la victoire du joueur 1 dans le jeu.
     CompareTotalScores2 - Comparaison des scores totaux des joueurs player2Score et player1Score pour déterminer le vainqueur du jeu.
    OutputPlayer2GameWin - Affichage du message concernant la victoire du joueur 2 dans le jeu.
    OutputTieGame - Affichage du message concernant une égalité dans le jeu.
    End - Fin du programme.