# Файл: MyLogUtils.psm1

# Это "приватная" вспомогательная функция.
# Она не будет экспортирована и видна пользователю модуля.
function Get-FormattedTimestamp {
    return "[{0}]" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
}

# Это "публичная" функция, которую мы хотим предоставить пользователю.
function Write-MyLog {
    param (
        [string]$Message,
        [string]$Level = "INFO"
    )
    $timestamp = Get-FormattedTimestamp
    $logEntry = "$timestamp [$Level] - $Message"
    Add-Content -Path "C:\Temp\app.log" -Value $logEntry
}

# Явно указываем, какие функции мы экспортируем из модуля.
# Все остальные функции останутся внутренними.
Export-ModuleMember -Function Write-MyLog