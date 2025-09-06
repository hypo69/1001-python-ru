![1]('assets/Screenshot 2025-09-02 074636.png')

Niestety, interfejs GitHub nie posiada przycisku do usuwania wszystkich uruchomień przepływów pracy jednym kliknięciem. Można to jednak zrobić na kilka sposobów.

### Użycie GitHub CLI (zalecana metoda do masowego usuwania)

Jest to najbardziej efektywny sposób na usunięcie dużej liczby uruchomień.
Będziesz potrzebować zainstalowanego [GitHub CLI](https://cli.github.com/).

1.  **Uwierzytelnianie (jeśli jeszcze tego nie zrobiłeś):**
    ```bash
    gh auth login
    ```

2.  **Usuwanie uruchomień:**
    Możesz użyć polecenia, aby uzyskać listę wszystkich uruchomień, a następnie je usunąć. Oto przykład skryptu dla `bash`:

    ```bash
    gh run list --json databaseId -q '.[].databaseId' | xargs -IID gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" -X DELETE
    ```

    To polecenie pobiera identyfikatory wszystkich uruchomień i dla każdego z nich wykonuje polecenie usunięcia za pośrednictwem API GitHub.

    Dla PowerShell, skrypt będzie wyglądał tak:
    ```powershell
    $workflowRuns = gh api "repos/$OWNER/$REPO/actions/runs" --paginate --jq '.workflow_runs[].id'
    foreach ($runId in $workflowRuns) {
      Write-Host "Deleting workflow run ID: $runId"
      gh api "repos/$OWNER/$REPO/actions/runs/$runId" -X DELETE
    }
    ```
    Będziesz musiał zastąpić `$OWNER` i `$REPO` nazwą właściciela i nazwą swojego repozytorium, odpowiednio.

### Ręczne usuwanie za pośrednictwem interfejsu webowego GitHub

Ta metoda jest odpowiednia, jeśli masz niewielką liczbę uruchomień do usunięcia.

1.  Przejdź do głównej strony swojego repozytorium na GitHub.
2.  Pod nazwą repozytorium kliknij zakładkę **Actions**.
3.  W lewym panelu bocznym wybierz przepływ pracy, którego uruchomienia chcesz usunąć.
4.  Zobaczysz listę uruchomień dla tego przepływu pracy.
5.  Dla każdego uruchomienia, które chcesz usunąć, kliknij menu "..." po prawej stronie i wybierz **Delete workflow run**.
6.  Potwierdź usunięcie.

Warto zauważyć, że po usunięciu wszystkich uruchomień, sam przepływ pracy może zniknąć z listy, jeśli odpowiedni plik `.yml` nie istnieje już w repozytorium.

### Użycie gotowych GitHub Actions

Istnieją gotowe akcje w [GitHub Marketplace](https://github.com/marketplace?type=actions), które można skonfigurować do automatycznego usuwania starych uruchomień. Na przykład, `delete-workflow-runs` pozwala na usuwanie uruchomień według harmonogramu lub po upływie określonego czasu. Jest to wygodny sposób na utrzymanie czystości w logach Twoich Actions bez ręcznej interwencji.
