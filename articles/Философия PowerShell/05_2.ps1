$global:appName = "My Awesome App"

function Show-AppName {
    $appName = "My Function App"
    Write-Host "Local Scope: $appName"
    Write-Host "Global Scope: $global:appName"
}

Show-AppName
Write-Host "Outside function: $appName"