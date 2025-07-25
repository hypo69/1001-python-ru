Import-Module -Path C:\Scripts\Modules\MyLogUtils\MyLogUtils.psd1 -Force
# -Force полезен при разработке для переимпортирования измененного модуля

# Теперь наша функция доступна как обычный командлет
Write-MyLog -Message "Модуль успешно импортирован!"