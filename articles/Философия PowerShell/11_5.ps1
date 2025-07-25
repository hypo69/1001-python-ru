# Создаем и сохраняем сессии в переменную
$mySessions = New-PSSession -ComputerName "SERVER01", "SERVER02"

# Теперь можно многократно использовать эти готовые сессии
Invoke-Command -Session $mySessions -ScriptBlock { Get-EventLog -LogName System -Newest 5 }
Invoke-Command -Session $mySessions -ScriptBlock { Restart-Service -Name Spooler -WhatIf }

# По завершении работы сессии нужно закрыть, чтобы освободить ресурсы на серверах
Remove-PSSession -Session $mySessions