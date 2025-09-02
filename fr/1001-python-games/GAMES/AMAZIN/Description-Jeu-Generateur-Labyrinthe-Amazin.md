# **Amazin** (Générateur de labyrinthes)

#### Description
Le jeu est un générateur de labyrinthes qui crée à chaque fois un labyrinthe unique avec un seul chemin correct. Le joueur définit les dimensions du labyrinthe, et le programme le construit en tenant compte des paramètres spécifiés.

- **Caractéristiques :**
  - Le joueur saisit la largeur et la hauteur du labyrinthe.
  - Le programme garantit un chemin unique à travers le labyrinthe.
  - Le labyrinthe est affiché à l'écran.

---

### Instructions étape par étape pour l'implémentation :

#### 1. **Initialisation du jeu**
   - Demander au joueur de saisir les dimensions du labyrinthe (largeur et hauteur).
   - Vérifier que les dimensions saisies sont valides (par exemple, supérieures à un).

#### 2. **Logique principale de génération du labyrinthe**
   - Créer une matrice de la taille spécifiée, représentant une grille de cellules.
   - Utiliser un algorithme de génération de labyrinthes, par exemple, *l'algorithme de recherche en profondeur récursive (DFS)* :
     - Commencer par une cellule initiale aléatoire.
     - Se déplacer vers les cellules adjacentes, en supprimant les murs entre la cellule actuelle et la suivante.
     - Si tous les voisins ont été visités, revenir à la cellule précédente et continuer.
     - Terminer le processus lorsque toutes les cellules ont été visitées.
   - Garantir un chemin unique à travers le labyrinthe.

#### 3. **Affichage du labyrinthe**
   - Utiliser des symboles pour l'affichage :
     - `+`, `-`, `|` pour les murs.
     - Espaces pour les passages.
   - Afficher le labyrinthe généré sous forme de texte.

#### 4. **Fonctionnalités supplémentaires**
   - Possibilité de définir une taille prédéfinie (par exemple, 10x10) si l'utilisateur a saisi des données invalides.
   - Avertissement concernant les tailles de labyrinthe excessivement grandes pour éviter la surcharge de mémoire.

---

### Exemple d'exécution du programme

1. **Début** :
   ```
   Entrez la largeur et la hauteur du labyrinthe :
   > 10 8
   ```

2. **Affichage du labyrinthe** :
   ```
   +--+--+--+--+--+--+--+--+--+--+
   |        |        |           |
   +  +--+  +  +--+  +  +--+--+  +
   |     |     |     |        |  |
   +--+  +  +--+  +  +  +--+  +  +
   |     |        |     |     |  |
   +--+--+--+--+--+--+--+--+--+--+
   ```

3. **Sortie du programme** :
   ```
   Générer un nouveau labyrinthe ? (oui/non) :
   > non
   Au revoir !
   ```

---