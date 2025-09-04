![1]('assets/Screenshot 2025-09-02 074636.png')

Sfortunatamente, nell'interfaccia di GitHub non esiste un pulsante per eliminare tutte le esecuzioni del workflow con un solo clic. Tuttavia, questo può essere fatto in diversi modi.

### Utilizzo di GitHub CLI (metodo consigliato per l'eliminazione in blocco)

Questo è il modo più efficace per eliminare un gran numero di esecuzioni.
Dovrai avere [GitHub CLI](https://cli.github.com/) installato.

1.  **Autenticazione (se non l'hai già fatto):**
    ```bash
    gh auth login
    ```

2.  **Eliminazione delle esecuzioni:**
    Puoi usare un comando per ottenere un elenco di tutte le esecuzioni e poi eliminarle. Ecco un esempio di script per `bash`:

    ```bash
    gh run list --json databaseId -q '.[].databaseId' | xargs -IID gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" -X DELETE
    ```

    Questo comando ottiene gli ID di tutte le esecuzioni e per ciascuna di esse esegue il comando di eliminazione tramite l'API di GitHub.

    Per PowerShell, lo script sarà simile a questo:
    ```powershell
    $workflowRuns = gh api "repos/$OWNER/$REPO/actions/runs" --paginate --jq '.workflow_runs[].id'
    foreach ($runId in $workflowRuns) {
      Write-Host "Eliminazione dell'esecuzione del workflow ID: $runId"
      gh api "repos/$OWNER/$REPO/actions/runs/$runId" -X DELETE
    }
    ```
    Dovrai sostituire `$OWNER` e `$REPO` con il nome del proprietario e il nome del tuo repository, rispettivamente.

### Eliminazione manuale tramite l'interfaccia web di GitHub

Questo metodo è adatto se hai un piccolo numero di esecuzioni da eliminare.

1.  Vai alla pagina principale del tuo repository su GitHub.
2.  Sotto il nome del repository, clicca sulla scheda **Actions**.
3.  Nella barra laterale sinistra, seleziona il workflow di cui vuoi eliminare le esecuzioni.
4.  Vedrai un elenco delle esecuzioni per quel workflow.
5.  Per ogni esecuzione che vuoi eliminare, clicca sul menu "..." a destra e seleziona **Delete workflow run**.
6.  Conferma l'eliminazione.

È da notare che dopo aver eliminato tutte le esecuzioni, il workflow stesso potrebbe scomparire dall'elenco se il file `.yml` corrispondente non esiste più nel repository.

### Utilizzo di GitHub Actions predefinite

Esistono azioni predefinite nel [GitHub Marketplace](https://github.com/marketplace?type=actions) che possono essere configurate per eliminare automaticamente le esecuzioni più vecchie. Ad esempio, `delete-workflow-runs` consente di eliminare le esecuzioni in base a una pianificazione o dopo un certo periodo di tempo. Questo è un modo conveniente per mantenere puliti i log delle tue Actions senza intervento manuale.
