Get-Process -Name "notepad" | ForEach-Object {
    Write-Host "Останавливаю процесс с ID: $($_.Id)..."
    # $_.Stop() - это вызов метода Stop() для текущего объекта процесса
    # В реальном скрипте лучше использовать Stop-Process -Id $_.Id
    Stop-Process -Id $_.Id
}