![1]('assets/Screenshot 2025-09-02 074636.png')

Unfortunately, the GitHub interface does not have a button to delete all workflow runs with one click. However, this can be done in several ways.

### Using GitHub CLI (recommended method for bulk deletion)

This is the most efficient way to delete a large number of runs.
You will need installed [GitHub CLI](https://cli.github.com/).

1.  **Authentication (if you haven't already):**
    ```bash
    gh auth login
    ```

2.  **Deleting runs:**
    You can use a command to get a list of all runs and then delete them. Here's a script example for `bash`:

    ```bash
    gh run list --json databaseId -q '.[].databaseId' | xargs -IID gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" -X DELETE
    ```

    This command gets the IDs of all runs and for each of them executes the delete command via the GitHub API.

    For PowerShell, the script will look like this:
    ```powershell
    $workflowRuns = gh api "repos/$OWNER/$REPO/actions/runs" --paginate --jq '.workflow_runs[].id'
    foreach ($runId in $workflowRuns) {
      Write-Host "Deleting workflow run ID: $runId"
      gh api "repos/$OWNER/$REPO/actions/runs/$runId" -X DELETE
    }
    ```
    You will need to replace `$OWNER` and `$REPO` with the owner name and your repository name, respectively.

### Manual deletion via GitHub web interface

This method is suitable if you have a small number of runs to delete.

1.  Go to the main page of your repository on GitHub.
2.  Under the repository name, click on the **Actions** tab.
3.  In the left sidebar, select the workflow whose runs you want to delete.
4.  You will see a list of runs for that workflow.
5.  For each run you want to delete, click the "..." menu on the right and select **Delete workflow run**.
6.  Confirm deletion.

It is worth noting that after deleting all runs, the workflow itself may disappear from the list if the corresponding `.yml` file no longer exists in the repository.

### Using ready-made GitHub Actions

There are ready-made actions in the [GitHub Marketplace](https://github.com/marketplace?type=actions) that can be configured to automatically delete old runs. For example, `delete-workflow-runs` allows you to delete runs by schedule or after a certain period of time. This is a convenient way to keep your Actions logs clean without manual intervention.
