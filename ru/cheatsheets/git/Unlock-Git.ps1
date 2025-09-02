unlock_git_script = """
function Unlock-Git {
    <#
    .SYNOPSIS
    Removes the .git/index.lock file to unlock a Git repository.

    .DESCRIPTION
    This function checks for the presence of a .git/index.lock file in the current directory
    and deletes it if found. This is useful when a Git operation is interrupted and leaves
    the repository in a locked state.

    .EXAMPLE
    Unlock-Git

    Deletes the .git/index.lock file in the current working directory if it exists.
    #>

    [CmdletBinding()]
    param ()

    $projectRoot = Get-Location
    $lockFile = Join-Path $projectRoot ".git\\index.lock"

    if (-not (Test-Path ".git")) {
        Write-Warning "❌ Current directory is not a Git repository."
        return
    }

    if (Test-Path $lockFile) {
        try {
            Remove-Item $lockFile -Force
            Write-Host "✅ Git lock file removed: $lockFile"
        }
        catch {
            Write-Error "❌ Failed to remove Git lock file: $lockFile"
        }
    }
    else {
        Write-Host "ℹ️ No lock file found. Repository is already unlocked."
    }
}

# Automatically run the function on script execution
Unlock-Git
"""

# Save to .ps1 file
output_path = Path("/mnt/data/Unlock-Git.ps1")
output_path.write_text(unlock_git_script.strip(), encoding="utf-8")
output_path.name
