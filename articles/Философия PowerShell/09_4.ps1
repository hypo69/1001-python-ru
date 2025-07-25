# Создаем сложный объект с помощью хеш-таблиц и массивов
$dataObject = @{
    User = "jdoe"
    SessionID = (Get-Random)
    Permissions = @("Read", "Write")
    LastLogin = @{
        Timestamp = Get-Date
        IPAddress = "192.168.1.100"
    }
}

# Преобразуем в JSON и выводим на экран
$jsonData = $dataObject | ConvertTo-Json
Write-Output $jsonData