# Импортируем данные в переменную. $serverObjects теперь - массив объектов.
$serverObjects = Import-Csv -Path C:\data\servers.csv

# Посмотрим на первый объект
$serverObjects[0]

# И на его структуру
$serverObjects[0] | Get-Member