Start-Job -ScriptBlock {
    # Симулируем очень долгую операцию
    Start-Sleep -Seconds 60
    # Сохраняем результат в файл
    Get-Process | Out-File -FilePath "C:\Temp\proclist.txt"
}