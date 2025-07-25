# Приводим содержимое файла к типу [xml]
[xml]$xmlConfig = Get-Content -Path C:\data\config.xml

# Теперь навигируем по структуре как по объекту
$apiUrl = $xmlConfig.Configuration.AppSettings.add | Where-Object { $_.key -eq "ApiUrl" } | Select-Object -ExpandProperty value
$adminRole = $xmlConfig.Configuration.Users.User.role

Write-Host "API URL: $apiUrl"
Write-Host "Admin role: $adminRole"