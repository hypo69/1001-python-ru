![1]('assets/Screenshot 2025-09-02 074636.png')

Malheureusement, il n'y a pas de bouton dans l'interface GitHub pour supprimer toutes les exécutions de workflow en un seul clic. Cependant, cela peut être fait de plusieurs manières.

### Utilisation de GitHub CLI (méthode recommandée pour la suppression en masse)

C'est le moyen le plus efficace de supprimer un grand nombre d'exécutions.
Vous aurez besoin d'avoir [GitHub CLI](https://cli.github.com/) installé.

1.  **Authentification (si ce n'est pas déjà fait) :**
    ```bash
    gh auth login
    ```

2.  **Suppression des exécutions :**
    Vous pouvez utiliser une commande pour obtenir une liste de toutes les exécutions, puis les supprimer. Voici un exemple de script pour `bash` :

    ```bash
    gh run list --json databaseId -q '.[].databaseId' | xargs -IID gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" -X DELETE
    ```

    Cette commande obtient les identifiants de toutes les exécutions et pour chacune d'elles exécute la commande de suppression via l'API GitHub.

    Pour PowerShell, le script ressemblera à ceci :
    ```powershell
    $workflowRuns = gh api "repos/$OWNER/$REPO/actions/runs" --paginate --jq '.workflow_runs[].id'
    foreach ($runId in $workflowRuns) {
      Write-Host "Suppression de l'exécution du workflow ID : $runId"
      gh api "repos/$OWNER/$REPO/actions/runs/$runId" -X DELETE
    }
    ```
    Vous devrez remplacer `$OWNER` et `$REPO` par le nom du propriétaire et le nom de votre dépôt respectivement.

### Suppression manuelle via l'interface web de GitHub

Cette méthode convient si vous avez un petit nombre d'exécutions à supprimer.

1.  Accédez à la page principale de votre dépôt sur GitHub.
2.  Sous le nom du dépôt, cliquez sur l'onglet **Actions**.
3.  Dans la barre latérale gauche, sélectionnez le workflow dont vous souhaitez supprimer les exécutions.
4.  Vous verrez une liste des exécutions de ce workflow.
5.  Pour chaque exécution que vous souhaitez supprimer, cliquez sur le menu "..." à droite et sélectionnez **Delete workflow run**.
6.  Confirmez la suppression.

Il convient de noter qu'après la suppression de toutes les exécutions, le workflow lui-même peut disparaître de la liste si le fichier `.yml` correspondant n'existe plus dans le dépôt.

### Utilisation d'actions GitHub prêtes à l'emploi

Il existe des actions prêtes à l'emploi sur le [GitHub Marketplace](https://github.com/marketplace?type=actions) qui peuvent être configurées pour supprimer automatiquement les anciennes exécutions. Par exemple, `delete-workflow-runs` vous permet de supprimer des exécutions selon un calendrier ou après une certaine période. C'est un moyen pratique de garder vos journaux d'Actions propres sans intervention manuelle.