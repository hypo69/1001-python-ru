$latestEvent = Get-WinEvent -LogName System -MaxEvents 1

switch ($latestEvent.LevelDisplayName) {
    "Information" {
        Write-Host "Последнее событие - информационное. Все в порядке." -ForegroundColor Gray
    }
    "Warning" {
        Write-Host "Последнее событие - предупреждение. Стоит обратить внимание." -ForegroundColor Yellow
    }
    "Error" {
        Write-Host "КРИТИЧЕСКАЯ ОШИБКА! Последнее событие - ошибка!" -ForegroundColor Red
    }
    default {
        Write-Host "Последнее событие имеет уровень: $($latestEvent.LevelDisplayName)"
    }
}