$serverList = @("google.com", "yandex.ru", "non-existent-host")

foreach ($server in $serverList) {
    if (Test-Connection -ComputerName $server -Count 1 -Quiet) {
        Write-Host "$server - доступен" -ForegroundColor Green
    }
    else {
        Write-Host "$server - НЕ доступен" -ForegroundColor Red
    }
}