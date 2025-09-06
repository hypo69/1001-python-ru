![1]('assets/Screenshot 2025-09-02 074636.png')

Leider gibt es in der GitHub-Oberfläche keinen Button, um alle Workflow-Läufe mit einem Klick zu löschen. Dies kann jedoch auf verschiedene Arten erfolgen.

### Verwendung von GitHub CLI (empfohlene Methode für Massenlöschung)

Dies ist die effizienteste Methode, um eine große Anzahl von Läufen zu löschen.
Sie benötigen das installierte [GitHub CLI](https://cli.github.com/).

1.  **Authentifizierung (falls noch nicht geschehen):**
    ```bash
    gh auth login
    ```

2.  **Löschen von Läufen:**
    Sie können einen Befehl verwenden, um eine Liste aller Läufe zu erhalten und diese dann zu löschen. Hier ist ein Skriptbeispiel für `bash`:

    ```bash
    gh run list --json databaseId -q '.[].databaseId' | xargs -IID gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" -X DELETE
    ```

    Dieser Befehl ruft die IDs aller Läufe ab und führt für jeden von ihnen den Löschbefehl über die GitHub API aus.

    Für PowerShell sieht das Skript so aus:
    ```powershell
    $workflowRuns = gh api "repos/$OWNER/$REPO/actions/runs" --paginate --jq '.workflow_runs[].id'
    foreach ($runId in $workflowRuns) {
      Write-Host "Deleting workflow run ID: $runId"
      gh api "repos/$OWNER/$REPO/actions/runs/$runId" -X DELETE
    }
    ```
    Sie müssen `$OWNER` und `$REPO` durch den Namen des Besitzers und den Namen Ihres Repositorys ersetzen.

### Manuelles Löschen über die GitHub-Weboberfläche

Diese Methode eignet sich, wenn Sie eine kleine Anzahl von Läufen löschen müssen.

1.  Gehen Sie zur Hauptseite Ihres Repositorys auf GitHub.
2.  Unter dem Repository-Namen klicken Sie auf den Tab **Actions**.
3.  Wählen Sie in der linken Seitenleiste den Workflow aus, dessen Läufe Sie löschen möchten.
4.  Sie sehen eine Liste der Läufe für diesen Workflow.
5.  Für jeden Lauf, den Sie löschen möchten, klicken Sie auf das "..."-Menü rechts und wählen Sie **Delete workflow run**.
6.  Bestätigen Sie das Löschen.

Es ist zu beachten, dass nach dem Löschen aller Läufe der Workflow selbst aus der Liste verschwinden kann, wenn die entsprechende `.yml`-Datei im Repository nicht mehr existiert.

### Verwendung von vorgefertigten GitHub Actions

Es gibt vorgefertigte Aktionen im [GitHub Marketplace](https://github.com/marketplace?type=actions), die so konfiguriert werden können, dass alte Läufe automatisch gelöscht werden. Zum Beispiel ermöglicht `delete-workflow-runs` das Löschen von Läufen nach Zeitplan oder nach einer bestimmten Zeitspanne. Dies ist eine bequeme Möglichkeit, Ihre Actions-Protokolle ohne manuelles Eingreifen sauber zu halten.
