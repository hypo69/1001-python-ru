# MyFirstScript.ps1
# Этот скрипт выводит приветствие и показывает 3 самых ресурсоемких процесса.

# Выводим приветственное сообщение
Write-Host "--- Мониторинг системы запущен ---" -ForegroundColor Green

# Получаем имя текущего пользователя и компьютера
$currentUser = $env:USERNAME
$computerName = $env:COMPUTERNAME
Write-Host "Скрипт запущен пользователем '$currentUser' на компьютере '$computerName'."

# Получаем текущую дату и время
$currentDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Host "Текущее время: $currentDate"

Write-Host "" # Пустая строка для разделения

# Находим и выводим 3 процесса, которые больше всего используют процессор
Write-Host "Топ-3 процессов по загрузке CPU:"
Get-Process | Sort-Object -Property CPU -Descending | Select-Object -First 3 -Property ProcessName, Id, CPU

Write-Host "--- Мониторинг завершен ---"