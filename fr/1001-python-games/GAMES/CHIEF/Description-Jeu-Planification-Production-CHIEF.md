CHIEF :
=================
Difficulté : 4
-----------------
Le jeu "CHIEF" est un jeu dans lequel le joueur agit en tant que chef d'usine, planifiant la production. Le joueur définit la quantité de produits fabriqués de chaque type, et l'ordinateur détermine si ces valeurs répondent aux exigences nécessaires. Si ce n'est pas le cas, le joueur est informé des valeurs incorrectes. Le but du jeu est d'atteindre une production optimale, en devinant correctement la quantité de produits.

Règles du jeu :
1. L'ordinateur devine trois valeurs dans la plage de 1 à 10 : `targetA`, `targetB` et `targetC`.
2. Le joueur saisit ses suppositions pour les valeurs `userA`, `userB` et `userC`.
3. L'ordinateur vérifie si les valeurs saisies correspondent aux valeurs devinées.
4. Si les trois valeurs sont devinées correctement, le jeu se termine par une victoire.
5. Si au moins une valeur ne correspond pas, l'ordinateur indique quelles valeurs étaient incorrectes.
6. Le jeu continue jusqu'à ce que le joueur devine les trois valeurs.
-----------------
Algorithme :
1.  Générer des nombres entiers aléatoires `targetA`, `targetB` et `targetC` dans la plage de 1 à 10.
2.  Démarrer une boucle "tant que tous les nombres ne sont pas devinés" :
    2.1. Demander au joueur de saisir trois nombres entiers : `userA`, `userB` et `userC`.
    2.2. Initialiser la chaîne `message` comme vide.
    2.3. Si `userA` n'est pas égal à `targetA`, ajouter "A" à `message`.
    2.4. Si `userB` n'est pas égal à `targetB`, ajouter "B" à `message`.
    2.5. Si `userC` n'est pas égal à `targetC`, ajouter "C" à `message`.
    2.6. Si `message` n'est pas vide, afficher le message "WRONG ON " et `message`.
    2.7. Sinon, afficher le message "YOU GOT IT!".
3. Fin du jeu.
-----------------
Organigramme :
```mermaid
flowchart TD
    Start["Début"] --> InitializeVariables["<p align='left'>Initialisation des variables :
    <code><b>
    targetA = random(1, 10)
    targetB = random(1, 10)
    targetC = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Début de la boucle : tant que non deviné"}
    LoopStart --> InputValues["<p align='left'>Saisie des nombres par l'utilisateur :
    <code><b>
    userA
    userB
    userC
    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"Vérification : <code><b>userA == targetA?</b></code>"}
    CheckA -- Non --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"Vérification : <code><b>userB == targetB?</b></code>"}
    CheckA -- Oui --> CheckB
    CheckB -- Non --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"Vérification : <code><b>userC == targetC?</b></code>"}
    CheckB -- Oui --> CheckC
    CheckC -- Non --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"Vérification : <code><b>message != "" ?</b></code>"}
    CheckC -- Oui --> CheckMessage
    CheckMessage -- Oui --> OutputWrong["Afficher le message : <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- Non --> OutputWin["Afficher le message : <b>YOU GOT IT!</b>"]
    OutputWin --> End["Fin"]
    LoopStart -- Non --> End
```
Légende :
    Start - Début du programme.
    InitializeVariables - Initialisation des variables : `targetA`, `targetB`, `targetC` sont générées aléatoirement de 1 à 10.
    LoopStart - Début de la boucle, qui continue tant que le joueur n'a pas deviné tous les nombres.
    InputValues - Demande à l'utilisateur de saisir trois nombres `userA`, `userB`, `userC`.
    InitializeMessage - Initialisation d'une chaîne vide `message`.
    CheckA - Vérifie si le nombre saisi `userA` est égal au nombre caché `targetA`.
    AppendA - Ajout de 'A' à `message`, si `userA` n'est pas égal à `targetA`.
    CheckB - Vérifie si le nombre saisi `userB` est égal au nombre caché `targetB`.
    AppendB - Ajout de 'B' à `message`, si `userB` n'est pas égal à `targetB`.
    CheckC - Vérifie si le nombre saisi `userC` est égal au nombre caché `targetC`.
    AppendC - Ajout de 'C' à `message`, si `userC` n'est pas égal à `targetC`.
    CheckMessage - Vérifie si la chaîne `message` est vide.
    OutputWrong - Affiche le message "WRONG ON" et le contenu de `message`, si la chaîne n'est pas vide.
    OutputWin - Affiche le message "YOU GOT IT!", si la chaîne `message` est vide.
    End - Fin du programme.