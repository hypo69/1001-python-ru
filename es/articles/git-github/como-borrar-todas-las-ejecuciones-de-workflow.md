![1]('assets/Screenshot 2025-09-02 074636.png')

Lamentablemente, no hay un botón en la interfaz de GitHub para eliminar todas las ejecuciones de flujo de trabajo (workflow runs) con un solo clic. Sin embargo, esto se puede hacer de varias maneras.

### Uso de GitHub CLI (método recomendado para eliminación masiva)

Esta es la forma más efectiva de eliminar una gran cantidad de ejecuciones.
Necesitarás tener instalado [GitHub CLI](https://cli.github.com/).

1.  **Autenticación (si aún no lo has hecho):**
    ```bash
    gh auth login
    ```

2.  **Eliminar ejecuciones:**
    Puedes usar un comando para obtener una lista de todas las ejecuciones y luego eliminarlas. Aquí tienes un ejemplo de script para `bash`:

    ```bash
    gh run list --json databaseId -q '.[].databaseId' | xargs -IID gh api "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/actions/runs/ID" -X DELETE
    ```

    Este comando obtiene los ID de todas las ejecuciones y para cada una de ellas ejecuta el comando de eliminación a través de la API de GitHub.

    Para PowerShell, el script se verá así:
    ```powershell
    $workflowRuns = gh api "repos/$OWNER/$REPO/actions/runs" --paginate --jq '.workflow_runs[].id'
    foreach ($runId in $workflowRuns) {
      Write-Host "Eliminando ejecución de flujo de trabajo ID: $runId"
      gh api "repos/$OWNER/$REPO/actions/runs/$runId" -X DELETE
    }
    ```
    Deberás reemplazar `$OWNER` y `$REPO` con el nombre del propietario y el nombre de tu repositorio, respectivamente.

### Eliminación manual a través de la interfaz web de GitHub

Este método es adecuado si tienes un pequeño número de ejecuciones que necesitas eliminar.

1.  Ve a la página principal de tu repositorio en GitHub.
2.  Debajo del nombre del repositorio, haz clic en la pestaña **Actions**.
3.  En la barra lateral izquierda, selecciona el flujo de trabajo cuyas ejecuciones deseas eliminar.
4.  Verás una lista de las ejecuciones de ese flujo de trabajo.
5.  Para cada ejecución que desees eliminar, haz clic en el menú "..." a la derecha y selecciona **Delete workflow run**.
6.  Confirma la eliminación.

Cabe señalar que después de eliminar todas las ejecuciones, el propio flujo de trabajo puede desaparecer de la lista si el archivo `.yml` correspondiente ya no existe en el repositorio.

### Uso de GitHub Actions predefinidas

Existen acciones predefinidas en el [GitHub Marketplace](https://github.com/marketplace?type=actions) que se pueden configurar para eliminar automáticamente las ejecuciones antiguas. Por ejemplo, `delete-workflow-runs` te permite eliminar ejecuciones según un cronograma o después de un cierto período de tiempo. Esta es una forma conveniente de mantener limpios los registros de tus Acciones sin intervención manual.