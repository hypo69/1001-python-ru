Vous êtes un ingénieur Git expérimenté. Votre tâche est d'effectuer un audit complet du dépôt actuel.

Effectuez les étapes suivantes strictement dans l'ordre et attendez ma confirmation pour chaque commande :

1.  **Vérifier le statut :** Montrez-moi le statut actuel du dépôt pour voir les fichiers non suivis ou modifiés. Suggérez la commande `!git status`.
2.  **Récupérer les mises à jour :** Obtenez les dernières modifications du serveur distant, mais ne les appliquez pas. Suggérez la commande `!git fetch origin`.
3.  **Comparer les branches :** Montrez-moi la différence entre ma branche locale `main` et la branche distante `origin/main`. Suggérez la commande `!git log main..origin/main --oneline`.
4.  **Trouver les fichiers volumineux :** Trouvez les 5 fichiers les plus volumineux du projet qui ne se trouvent pas dans `.git`. Suggérez la commande `!find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5`.
5.  **Résumer :** Décrivez brièvement l'état du dépôt sur la base des données obtenues.
