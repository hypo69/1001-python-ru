# Получаем объекты служб, выбираем только нужные свойства
Get-Service | Select-Object -Property Name, DisplayName, Status | Export-Csv -Path C:\data\services_report.csv -NoTypeInformation