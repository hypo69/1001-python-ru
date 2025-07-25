$servers = "SERVER01", "SERVER02", "SERVER03"
$servers.Count
$servers -contains "SERVER02"

$servers | ForEach-Object { Write-Host "Checking $_" }