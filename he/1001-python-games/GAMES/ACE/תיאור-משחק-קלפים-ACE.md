ACE:
=================
קושי: 7
-----------------
המשחק "ACE" הוא משחק שבו שני שחקנים מושכים בתורם קלפים מחפיסה ומנסים לצבור יותר נקודות. אס נחשב לנקודה אחת, קלפים מ-2 עד 10 נחשבים לפי ערכם הנקוב, וג'ק, קווין ומלך נחשבים ל-10. השחקן עם יותר נקודות מנצח. המשחק נמשך עד שמספר מסוים של סיבובים משוחקים.

כללי המשחק:
1. שני שחקנים משחקים.
2. שחקנים מושכים בתורם קלפים מהחפיסה.
3. לכל קלף יש מספר נקודות מסוים: אס - 1, קלפים מ-2 עד 10 - לפי ערכם הנקוב, ג'ק, קווין ומלך - 10.
4. כל שחקן מנסה לצבור כמה שיותר נקודות בסיבוב.
5. בסוף הסיבוב, ציוני השחקנים מושווים.
6. המשחק מורכב ממספר מסוים של סיבובים.
7. השחקן עם יותר נקודות בכל הסיבובים מוכרז כמנצח המשחק.
-----------------
אלגוריתם:
1. אתחל את ציוני שחקן 1 ושחקן 2 לאפס.
2. בקש את מספר הסיבובים.
3. התחל לולאה עבור מספר הסיבובים:
    3.1. שחקן 1 מושך קלף.
    3.2. הצג את קלף שחקן 1 ונקודות הקלף.
    3.3. הוסף את נקודות הקלף לציון הכולל של שחקן 1.
    3.4. שחקן 2 מושך קלף.
    3.5. הצג את קלף שחקן 2 ונקודות הקלף.
    3.6. הוסף את נקודות הקלף לציון הכולל של שחקן 2.
    3.7. אם ציון שחקן 1 גדול מציון שחקן 2, הצג "PLAYER 1 WINS THE ROUND".
    3.8. אם ציון שחקן 2 גדול מציון שחקן 1, הצג "PLAYER 2 WINS THE ROUND".
    3.9. אם ציון שחקן 1 שווה לציון שחקן 2, הצג "TIE GAME THIS ROUND".
4. הצג את הציון הכולל של שחקן 1.
5. הצג את הציון הכולל של שחקן 2.
6. אם הציון הכולל של שחקן 1 גדול מהציון הכולל של שחקן 2, הצג "PLAYER 1 WINS THE GAME".
7. אם הציון הכולל של שחקן 2 גדול מהציון הכולל של שחקן 1, הצג "PLAYER 2 WINS THE GAME".
8. אם הציון הכולל של שחקן 1 שווה לציון הכולל של שחקן 2, הצג "TIE GAME".
9. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeScores["<p align='left'>אתחול משתנים:<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["הכנס מספר סיבובים: <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"התחל לולאת סיבובים"}
    RoundLoopStart -- כן --> Player1DrawsCard["שחקן 1 מושך קלף: <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["הצג קלף ונקודות שחקן 1: <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["שחקן 2 מושך קלף: <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["הצג קלף ונקודות שחקן 2: <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"השווה ציוני סיבוב: <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- כן --> OutputPlayer1RoundWin["הצג: <b>PLAYER 1 WINS THE ROUND</b>"]
    CompareScores -- לא --> CompareScores2{"השווה ציוני סיבוב: <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- כן --> OutputPlayer2RoundWin["הצג: <b>PLAYER 2 WINS THE ROUND</b>"]
    CompareScores2 -- לא --> OutputTieRound["הצג: <b>TIE GAME THIS ROUND</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
     RoundLoopEnd --> RoundLoopStart {"התחל לולאת סיבובים"}

    RoundLoopStart -- לא --> OutputTotalPlayer1Score["הצג ציון כולל של שחקן 1: <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["הצג ציון כולל של שחקן 2: <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"השווה ציונים כוללים: <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- כן --> OutputPlayer1GameWin["הצג: <b>PLAYER 1 WINS THE GAME</b>"]
    CompareTotalScores -- לא --> CompareTotalScores2{"השווה ציונים כוללים: <code><b>player2Score > player1Score?</b></code>"}
     CompareTotalScores2 -- כן --> OutputPlayer2GameWin["הצג: <b>PLAYER 2 WINS THE GAME</b>"]
    CompareTotalScores2 -- לא --> OutputTieGame["הצג: <b>TIE GAME</b>"]
    OutputPlayer1GameWin --> End["סיום"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```
**מקרא**
    Start - התחלת התוכנית.
    InitializeScores - אתחול משתני ציוני שחקן 1 ושחקן 2 לאפס.
    InputRounds - בקשת מספר הסיבובים numberOfRounds מהמשתמש עבור המשחק.
    RoundLoopStart - התחלת לולאה עבור כל סיבוב במשחק. הלולאה מבוצעת numberOfRounds פעמים.
    Player1DrawsCard - שחקן 1 מושך קלף card1 וערכו card1Value נקבע.
    OutputPlayer1Card - הצגת מידע על קלף שחקן 1 card1 וערכו card1Value.
    UpdatePlayer1Score - עדכון הציון הכולל של שחקן 1, על ידי הוספת card1Value ל-player1Score.
    Player2DrawsCard - שחקן 2 מושך קלף card2 וערכו card2Value נקבע.
    OutputPlayer2Card - הצגת מידע על קלף שחקן 2 card2 וערכו card2Value.
    UpdatePlayer2Score - עדכון הציון הכולל של שחקן 2, על ידי הוספת card2Value ל-player2Score.
    CompareScores - השוואת ערכי קלפים card1Value ו-card2Value לקביעת מנצח הסיבוב.
    OutputPlayer1RoundWin - הצגת הודעה על ניצחון שחקן 1 בסיבוב.
    CompareScores2 - השוואת ערכי קלפים card2Value ו-card1Value לקביעת מנצח הסיבוב.
    OutputPlayer2RoundWin - הצגת הודעה על ניצחון שחקן 2 בסיבוב.
    OutputTieRound - הצגת הודעה על תיקו בסיבוב.
    RoundLoopEnd - סיום לולאת הסיבובים.
    OutputTotalPlayer1Score - הצגת הציון הכולל של שחקן 1 player1Score.
    OutputTotalPlayer2Score - הצגת הציון הכולל של שחקן 2 player2Score.
    CompareTotalScores - השוואת ציונים כוללים של שחקנים player1Score ו-player2Score לקביעת מנצח המשחק.
    OutputPlayer1GameWin - הצגת הודעה על ניצחון שחקן 1 במשחק.
     CompareTotalScores2 - השוואת ציונים כוללים של שחקנים player2Score ו-player1Score לקביעת מנצח המשחק.
    OutputPlayer2GameWin - הצגת הודעה על ניצחון שחקן 2 במשחק.
    OutputTieGame - הצגת הודעה על תיקו במשחק.
    End - סיום התוכנית.