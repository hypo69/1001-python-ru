### Nom du jeu : **Jeu de cartes Acey-Ducey**

#### Description
Il s'agit d'une simulation du jeu de cartes Acey-Ducey. Le joueur place des paris en fonction de la probabilité que la carte suivante tombe entre les deux cartes déjà ouvertes.

- **Capital de départ :** Le joueur commence avec 100 dollars.
- **Règles du jeu :**
  1. L'ordinateur distribue deux cartes.
  2. Le joueur peut décider de placer un pari ou non.
  3. Si un pari est placé, une troisième carte est tirée.
  4. Si la valeur de la troisième carte tombe entre les deux premières cartes, le joueur gagne le pari. Sinon, le pari est perdu.
- Le jeu se termine lorsque le joueur perd tout son capital ou le termine manuellement.

#### Implémentation

**Données d'entrée :**
- Saisie de l'utilisateur pour :
  - Taille du pari initial.
  - Décision de placer un pari ou de passer.

**Données de sortie :**
- Message sur le capital actuel du joueur.
- Informations sur les résultats du pari (gain/perte).
- État des cartes à chaque tour.

#### Instructions étape par étape pour l'implémentation :

1. **Initialisation du jeu** :
   - Définir le capital initial du joueur (100 dollars).
   - Annoncer les règles du jeu.

2. **Boucle de jeu principale** :
   - Générer deux cartes aléatoires (plage 2–14, où 11 = valet, 12 = dame, 13 = roi, 14 = as).
   - Afficher les cartes au joueur.
   - Demander un pari (peut passer le tour en pariant 0).
   - Vérifier : le pari ne doit pas dépasser le capital actuel.

3. **Résultat du tour** :
   - Générer une troisième carte.
   - Vérifier si sa valeur tombe dans la plage entre les deux premières cartes.
   - Modifier le capital du joueur en fonction du résultat.

4. **Fin du jeu** :
   - Si le capital du joueur est de 0, le jeu se termine avec un message approprié.
   - Proposer au joueur de commencer une nouvelle partie ou de quitter.

#### Limitations
- Toutes les cartes sont uniques au sein d'un même tour.
- Prise en charge des fonctionnalités de base du jeu sans effets visuels complexes.
